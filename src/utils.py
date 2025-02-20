from PyQt5.QtCore import Qt


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


        