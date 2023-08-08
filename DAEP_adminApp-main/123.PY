import requests
import json
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTabWidget,
    QTextEdit,
    QLineEdit
)

appData = {}
ibData = {}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        directions_list_name = QLabel('Напрвления')
        main_layout.addWidget(directions_list_name)

        directions_list = QTabWidget()

        for direction in ibData['local_data'].keys():

            direction_widget = QWidget()
            direction_widget.setObjectName(direction)
            direction_layout = QVBoxLayout()

            type_activities_list_name = QLabel('Виды активности')
            direction_layout.addWidget(type_activities_list_name)

            type_activities_list = QTabWidget()
            type_activities_list.setObjectName(direction)

            for type_activity in ibData['local_data'][direction]['local']:

                type_activity_widget = QWidget()
                type_activity_widget.setObjectName(type_activity)

                type_activity_layout = QVBoxLayout()
                subject_tasks_list_name = QLabel('Предметные задачи')
                type_activity_layout.addWidget(subject_tasks_list_name)

                subject_tasks_list = QTabWidget()
                subject_tasks_list.setObjectName(f'{direction}_{type_activity}')

                for subject_task in ibData['local_data'][direction]['local'][type_activity]['subject_tasks']:

                    subject_task_widget = QWidget()
                    subject_task_widget.setObjectName(f'{direction}_{type_activity}_{subject_task}')

                    subject_task_layout = QVBoxLayout()

                    module_edit_line_name = QLabel('Модуль')
                    subject_task_layout.addWidget(module_edit_line_name)

                    module_edit_line = QLineEdit(
                        ibData['local_data'][direction]['local'][type_activity]['subject_tasks'][subject_task]
                        ['module'])
                    module_edit_line.setObjectName(f'{direction}_{type_activity}_{subject_task}_module')
                    module_edit_line.textChanged.connect(self.change_subject_task_data)
                    subject_task_layout.addWidget(module_edit_line)

                    duration_edit_line_name = QLabel('Длительность программы в часах')
                    subject_task_layout.addWidget(duration_edit_line_name)

                    duration_edit_line = QLineEdit(
                        str(ibData['local_data'][direction]['local'][type_activity]['subject_tasks']
                            [subject_task]['duration']))
                    duration_edit_line.setObjectName(f'{direction}_{type_activity}_{subject_task}_duration')
                    duration_edit_line.textChanged.connect(self.change_subject_task_data)
                    subject_task_layout.addWidget(duration_edit_line)

                    theory_edit_line_name = QLabel('Теория')
                    subject_task_layout.addWidget(theory_edit_line_name)

                    theory_edit_line = QTextEdit(
                        ibData['local_data'][direction]['local'][type_activity]['subject_tasks']
                        [subject_task]['theory'])
                    theory_edit_line.setObjectName(f'{direction}_{type_activity}_{subject_task}_theory')
                    theory_edit_line.textChanged.connect(self.change_subject_task_data)
                    subject_task_layout.addWidget(theory_edit_line)

                    practice_edit_line_name = QLabel('Практика')
                    subject_task_layout.addWidget(practice_edit_line_name)

                    practice_edit_line = QTextEdit(
                        ibData['local_data'][direction]['local'][type_activity]['subject_tasks']
                        [subject_task]['practice'])
                    practice_edit_line.setObjectName(f'{direction}_{type_activity}_{subject_task}_practice')
                    practice_edit_line.textChanged.connect(self.change_subject_task_data)
                    subject_task_layout.addWidget(practice_edit_line)

                    result_edit_line_name = QLabel('Результат')
                    subject_task_layout.addWidget(result_edit_line_name)

                    result_edit_line = QTextEdit(
                        ibData['local_data'][direction]['local'][type_activity]['subject_tasks']
                        [subject_task]['result'])
                    result_edit_line.setObjectName(f'{direction}_{type_activity}_{subject_task}_result')
                    result_edit_line.textChanged.connect(self.change_subject_task_data)
                    subject_task_layout.addWidget(result_edit_line)

                    subject_task_widget.setLayout(subject_task_layout)

                    subject_tasks_list.addTab(subject_task_widget, subject_task)

                type_activity_layout.addWidget(subject_tasks_list)
                type_activity_widget.setLayout(type_activity_layout)
                type_activities_list.addTab(type_activity_widget, type_activity)

            direction_layout.addWidget(type_activities_list)
            direction_widget.setLayout(direction_layout)
            directions_list.addTab(direction_widget, direction)

        main_layout.addWidget(directions_list)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

    def change_subject_task_data(self):
        global ibData
        sender = self.sender()
        changed_element_name = sender.objectName().split('_')
        changed_element_data = sender.text()
        if changed_element_name[-1] == 'duration':
            changed_element_data = int(changed_element_data)
        ibData['local_data'][changed_element_name[0]]['local'][changed_element_name[1]]['subject_tasks'][changed_element_name[2]][changed_element_name[3]] = changed_element_data


def load_congig():
    global appData
    with open('appConfig.json') as config:
        appData = json.load(config)


def update_or_load_Data():
    global appData, ibData
    ibData = requests.get(f'{appData["server_url"]}get_ib_back').json()


def first_start():
    load_congig()
    update_or_load_Data()
    return True


def start():
    if first_start():
        app = QApplication(sys.argv)
        w = MainWindow()
        w.show()
        app.exec()


if __name__ == "__main__":
    start()
