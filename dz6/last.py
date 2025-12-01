import random
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout,
    QWidget, QPushButton, QMessageBox
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt


class PutinApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Самый лучший президент")
        self.setGeometry(100, 100, 600, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        title = QLabel("Владимир Владимирович Путин")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)


        self.load_image()

        caption = QLabel("Президент Российской Федерации")
        caption.setFont(QFont("Arial", 12))
        caption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(caption)


        info_btn = QPushButton("Информация")
        info_btn.setFont(QFont("Arial", 11))
        info_btn.clicked.connect(self.show_info)
        layout.addWidget(info_btn)

    def load_image(self):

        images_array=["putin.jpg","putin2.jpg","putin3.jpeg"]
        pixmap = QPixmap(random.choice(images_array)).scaled(
            400, 500,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.image_label.setPixmap(pixmap)

    def show_info(self):

        info_text = """
        <b>Владимир Владимирович Путин</b><br><br>
        Президент Российской Федерации<br>
        Родился: 7 октября 1952 года<br>
        Место рождения: Ленинград, СССР<br><br>
        Образование: Юридический факультет<br>Ленинградского государственного университета
        """

        msg = QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText(info_text)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()


def main():
    app = QApplication(sys.argv)
    window = PutinApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()