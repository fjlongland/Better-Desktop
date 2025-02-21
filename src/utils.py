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
    print(desktop) 
    items = os.listdir(desktop)

    #files = [f for f in os.listdir(desktop) if os.path.isfile(os.path.join(desktop, f))]
    #folders = [f for f in os.listdir(desktop) if os.path.isdir(os.path.join(desktop, f))]

    arr = []

    for item in items:
        arr.append(f"{item}     ")
    
    return items



