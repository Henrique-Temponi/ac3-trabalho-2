from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication,QPushButton, QMainWindow

import sys

class MainWindow (QMainWindow):
    def __init__(self ) :
        super().__init__()

        self.setWindowTitle("My app")
        button = QPushButton("Press me!")

        self.setCentralWidget(button)
        # self.setFixedSize(QSize(300, 400))
        # self.setMaximumSize(QSize(400, 300))

app = QApplication(sys.argv)

# window = QPushButton()
window = MainWindow()
window.show() 

app.exec()
