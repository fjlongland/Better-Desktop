from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QEvent
from .utils import btnFullScreen, execute

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Better Desktop")
        self.setWindowIcon(QIcon("src/graphics/lolfunny.png"))

#//////////////////////////////////////////////////////////////////////////////////////

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

#/////////////////////////////////////////////////////////////////////////////////////

        top_layout = QHBoxLayout()

        top_right_layout = QVBoxLayout()

        self.btnToggle = QPushButton("toggle", self)
        self.btnToggle.clicked.connect(self.toggle_fullscreen)
        self.btnToggle.setFixedWidth(100)
        self.btnToggle.setFixedHeight(40)

        self.btnClose = QPushButton("close", self)
        self.btnClose.clicked.connect(self.close_clicked)
        self.btnClose.setFixedWidth(100)
        self.btnClose.setFixedHeight(40)

        top_right_layout.addWidget(self.btnToggle)
        top_right_layout.addWidget(self.btnClose)

        self.vLinet = QFrame(self)
        self.vLinet.setFrameShape(QFrame.VLine)
        self.vLinet.setFrameShadow(QFrame.Sunken)

        top_layout.addStretch()
        top_layout.addWidget(self.vLinet)
        top_layout.addLayout(top_right_layout)

#//////////////////////////////////////////////////////////////////////////////////////////////////

        self.hLine = QFrame(self)
        self.hLine.setFrameShape(QFrame.HLine)
        self.hLine.setFrameShadow(QFrame.Sunken)

#/////////////////////////////////////////////////////////////////////////////////////////////////

        bottom_layout = QHBoxLayout()

        self.tbCL = QTextEdit(self)
        self.tbCL.setGeometry(50, 50, 300, 300)
        self.tbCL.installEventFilter(self)
        self.tbCL.setPlainText("./Desktop ~")

        self.vLinel = QFrame(self)
        self.vLinel.setFrameShape(QFrame.VLine)
        self.vLinel.setFrameShadow(QFrame.Sunken)

        self.vLiner = QFrame(self)
        self.vLiner.setFrameShape(QFrame.VLine)
        self.vLiner.setFrameShadow(QFrame.Sunken)

        bottom_layout.addStretch()
        bottom_layout.addWidget(self.vLinel)
        bottom_layout.addWidget(self.tbCL)
        bottom_layout.addWidget(self.vLiner)
        bottom_layout.addStretch()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        layout.addLayout(top_layout)
        layout.addStretch()
        layout.addWidget(self.hLine)
        layout.addLayout(bottom_layout)
     
#////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def toggle_fullscreen(self):
        btnFullScreen(self)

    def close_clicked(self):
        self.close()

    def eventFilter(self, obj, event):
        if obj == self.tbCL and event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            execute(self)
            return True
        return super().eventFilter(obj, event)
    
    
        