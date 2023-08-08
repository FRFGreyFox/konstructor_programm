from PyQt6.QtWidgets import QTabWidget, QApplication, QWidget, QHBoxLayout, QLineEdit
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        main = QWidget(self)
        main.resize(200, 200)
        box = QHBoxLayout()
        main.setLayout(box)

        line = QLineEdit()
        line.textChanged.connect(self.doSomething)
        

        # tabWidgetObjects = QTabWidget(self)
        # tabObjects_1 = QWidget()
        # tabObjects_1.setObjectName("tabObjects_1")
        # tabObjects_2 = QWidget()
        # tabObjects_2.setObjectName("tabObjects_2")

        # tabWidgetObjects.addTab(tabObjects_1, "вкладка 1")
        # tabWidgetObjects.addTab(tabObjects_2, "вкладка 2")
    

    def doSomething(self):
        print(123)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()