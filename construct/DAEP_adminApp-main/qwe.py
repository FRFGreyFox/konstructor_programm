import requests
import json
appData = {}
ibData = {}


import sys
from random import randint

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        directions_list_layout = QLabel('Напрвления')
        main_layout.addWidget(directions_list_layout)
        self.directions_button_data = {}
        for direction in ibData['local_data'].keys():
            self.directions_button_data[direction] = QPushButton(direction)
            self.directions_button_data[direction].clicked.connect(self.open_direction_data)
            main_layout.addWidget(self.directions_button_data[direction])
        add_new_direction_button = QPushButton('добавить новое направление')
        add_new_direction_button.clicked.connect(self.open_direction_data)
        main_layout.addWidget(add_new_direction_button)
        main_widget = QWidget()

        

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def open_direction_data(self):
        pass


def load_congig():
    global appData
    with open('appConfig.json') as config:
        appData = json.load(config)



def update_or_load_Data():
    global appData, ibData
    ibData = requests.get(f'{appData["server_url"]}get_ib_back').json()


def first_start():
    try:
        load_congig()
        update_or_load_Data()
    except BaseException:
        return False
    return True


def start():
    if first_start():
        print('start App`s work')
        app = QApplication(sys.argv)
        w = MainWindow()
        w.show()
        app.exec()
    else:
        print('Error!!!')


if __name__ == "__main__":
    start()