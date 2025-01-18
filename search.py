from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QWidget
from PyQt5.QtCore import Qt
import os
import sys
import subprocess


class FileSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("جستجوی فایل‌ها")
        self.setGeometry(200, 200, 600, 400)

        # Layout
        layout = QVBoxLayout()

        self.directory_input = QLineEdit(self)
        self.directory_input.setPlaceholderText("مسیر فولدر را وارد کنید یا انتخاب کنید...")
        layout.addWidget(self.directory_input)

        browse_button = QPushButton("انتخاب فولدر")
        browse_button.clicked.connect(self.browse_folder)
        layout.addWidget(browse_button)

        self.keyword_input = QLineEdit(self)
        self.keyword_input.setPlaceholderText("کلمه کلیدی را وارد کنید...")
        layout.addWidget(self.keyword_input)

        search_button = QPushButton("جستجو")
        search_button.clicked.connect(self.search_files)
        layout.addWidget(search_button)

        self.results_list = QListWidget(self)
        self.results_list.itemDoubleClicked.connect(self.open_file)
        layout.addWidget(self.results_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "انتخاب فولدر")
        if folder:
            self.directory_input.setText(folder)

    def search_files(self):
        directory = self.directory_input.text()
        keyword = self.keyword_input.text()

        if not directory or not keyword:
            self.results_list.clear()
            self.results_list.addItem("لطفاً مسیر فولدر و کلمه کلیدی را وارد کنید.")
            return

        if not os.path.exists(directory):
            self.results_list.clear()
            self.results_list.addItem("مسیر وارد شده معتبر نیست.")
            return

        self.results_list.clear()
        for root, dirs, files in os.walk(directory):
            for file in files:
                if keyword.lower() in file.lower():
                    full_path = os.path.join(root, file)
                    self.results_list.addItem(full_path)

        if self.results_list.count() == 0:
            self.results_list.addItem("هیچ فایلی پیدا نشد.")

    def open_file(self, item):
        file_path = item.text()
        if os.path.exists(file_path):
            subprocess.Popen([file_path], shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSearchApp()
    window.show()
    sys.exit(app.exec_())
