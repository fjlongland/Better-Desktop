import sys 
from PyQt5.QtWidgets import QApplication
from .frontend import MainWindow

def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()