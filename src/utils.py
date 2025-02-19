from PyQt5.QtCore import Qt


def btnFullScreen(window):
    if window.isFullScreen():
        window.showNormal()
    else:
        window.showFullScreen()

def execute(window):
        
    text = window.tbCL.toPlainText()
    lastLine = text.split("\n")[-1]

    window.tbCL.append("running script...")
    window.tbCL.append("")
    window.tbCL.append("")
    window.tbCL.insertPlainText("./Desktop ~ ")

    print(lastLine)


        