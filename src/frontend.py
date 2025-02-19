from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QEvent
from .utils import btnFullScreen, execute

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 40, 1000, 1000)
        self.setWindowTitle("Better Desktop")

        self.btnToggle = QPushButton("toggle", self)
        self.btnToggle.clicked.connect(self.toggle_fullscreen)

        self.tbCL = QTextEdit(self)
        self.tbCL.setGeometry(50, 50, 300, 300)
        self.tbCL.installEventFilter(self)
        self.tbCL.setPlainText("./Desktop ~ ")

    def toggle_fullscreen(self):
        btnFullScreen(self)

    def eventFilter(self, obj, event):
        if obj == self.tbCL and event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            execute(self)
            return True
        return super().eventFilter(obj, event)
    
    
        