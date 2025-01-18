from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, \
    QWidget
import os
import sys


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

        self.results_box = QTextEdit(self)
        layout.addWidget(self.results_box)

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
            self.results_box.setText("لطفاً مسیر فولدر و کلمه کلیدی را وارد کنید.")
            return

        if not os.path.exists(directory):
            self.results_box.setText("مسیر وارد شده معتبر نیست.")
            return

        results = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if keyword.lower() in file.lower():
                    results.append(os.path.join(root, file))

        if results:
            self.results_box.setText("\n".join(results))
        else:
            self.results_box.setText("هیچ فایلی پیدا نشد.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSearchApp()
    window.show()
    sys.exit(app.exec_())
