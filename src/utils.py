from PyQt5.QtCore import Qt

def btnFullScreen(window):
    if window.isFullScreen():
        window.showNormal()
    else:
        window.showFullScreen()

def execute(window):
        print("Enter Key pressed! Running script.")
        # Add your script logic here