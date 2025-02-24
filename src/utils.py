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

    inp = lastLine.split("~")[-1]

    commands = inp.split(" ")
    command = commands[0].lower()

    if len(commands) >= 2:
        param = commands[1]

#/////////////////////////////////////////////////////////////////////////////////

    match command:
        case "test":
            ret = "It is Working :)"
        
        case "help":
            ret = "current functioning commands are:\ntest\thelp\tls\tcd"

        case "ls":
            ret = '\t\t'.join(listWindows())

        case "cd":
            open_file(param)

        case _:
            ret = "something went wrong, use command 'help' for more information."
        
#//////////////////////////////////////////////////////////////////////////////////

    window.tbCL.append("")

    window.tbCL.append(ret)

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
