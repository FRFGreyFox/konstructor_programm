from PyQt6.QtWidgets import QTabWidget, QApplication, QWidget, QHBoxLayout, QLineEdit, QTextEdit, QMainWindow, QPushButton
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        main = QWidget(self)
        main.resize(500, 500)
        box = QHBoxLayout()
        main.setLayout(box)
        line = QLineEdit(self, text='button caption', objectName='button1')
        line.textChanged.connect(self.doSomething)

    def doSomething(self):
        sender = self.sender()
        print(sender.objectName())
        print(sender.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()