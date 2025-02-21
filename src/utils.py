from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton
import os


def btnFullScreen(window):
    if window.isFullScreen():
        window.showNormal()
    else:
        window.showFullScreen()

def execute(window):
        
    text = window.tbCL.toPlainText()
    lastLine = text.split("\n")[-1]

    command = lastLine.split("~")[-1]

    window.tbCL.append("running script...")

#/////////////////////////////////////////////////////////////////////////////////

    match command:
        case "test":
            print("it works.")
        
        case _:
            print("invalid input.")
        
#//////////////////////////////////////////////////////////////////////////////////
    window.tbCL.append("")
    window.tbCL.append("")
    window.tbCL.insertPlainText("./Desktop ~")

    print(lastLine)


def listWindows():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    items = os.listdir(desktop)

    arr = []

    for item in items:
        arr.append(f"{item}     ")
    
    return items



def open_file(file_name):
    current_directory = os.path.join(os.path.expanduser("~"), "Desktop")
    path_to_file = os.path.join(current_directory, file_name)

    if os.path.exists(path_to_file):
        os.startfile(path_to_file)
    else:
        print("error")

    print(path_to_file)
