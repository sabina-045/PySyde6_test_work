import sys

from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QFileDialog, QDialog, QMessageBox)
from PySide6.QtCore import QAbstractTableModel
from PySide6 import QtWidgets
from PySide6 import QtCore

from gui.main_window import Ui_MainWindow
from gui.download_file_in_db import Ui_Dialog
from app.db import DataBase
from utils import convert_data_to_json


class TableModel(QAbstractTableModel):
    """Класс таблицы."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = DataBase()
        self.data_table = self.db.data_from_table_total_results()

    def update(self):
        self.beginResetModel()
        self.data_table = self.db.data_from_table_total_results()
        self.endResetModel()

    def rowCount(self, *args, **kwargs):
        """Подсчет количеста строк"""

        return len(self.data_table)

    def columnCount(self, *args, **kwargs):
        """Подсчет количеста колонок"""

        return 5

    def data(self, index, role=QtCore.Qt.ItemDataRole):
        """Вывод двнных в таблицу"""
        if not index.isValid():

            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            lines = self.data_table[index.row()]
            column = index.column()
            if column == 0:

                return lines[0]
            if column == 1:

                return lines[1]
            if column == 2:

                return lines[2]
            if column == 3:

                return lines[3]
            if column == 4:

                return lines[4]
            if column == 5:

                return lines[5]

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation.Horizontal, role=QtCore.Qt.ItemDataRole):
        """Добавление заголовков стоблцов в таблицу."""
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'Занятое место',
                    1: 'Нагрудный номер',
                    2: 'Имя',
                    3: 'Фамилия',
                    4: 'Результат',
                }.get(section)


class Runners(QMainWindow):
    """Класс главного окна."""
    def __init__(self):
        super(Runners, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog = DownloadWindow(self)
        self.db = DataBase()
        self.table = TableModel(parent=None)
        self.ui.table_results.setModel(self.table)

        self.ui.pushButton_download_in_db.clicked.connect(
            self.dialog.show)
        self.ui.pushButton_count_results.clicked.connect(
            self.count_results)
        self.ui.pushButton_save_results_json.clicked.connect(
            self.download_results_in_json)

    def count_results(self):
        """Подсчитываем общие результы."""
        self.db.total_results_count()
        self.table.update()

    def download_results_in_json(self):
        """Выгружаем результаты подсчета в файл json."""
        self.db.check_table_is_not_empty('total_results')
        data = self.db.data_from_table_total_results()

        return convert_data_to_json(data)


class DownloadWindow(QDialog):
    """Класс диалогового окна для загрузки файлов в бд."""
    def __init__(self, parent=None):
        super(DownloadWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = DataBase()

        self.ui.pushButton_open_file.clicked.connect(self.choose_file)
        self.ui.pushButton_download.clicked.connect(
            self.get_data_from_window)

    def choose_file(self):
        """Выбор файла json/text для загрузки в бд."""
        file = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "c:/Dev/11-03-2024-sabina-045",
            "Text files(*.txt);; Json files(*.json)")
        if file:
            self.ui.lineEdit_path.setText(file[0])

    def get_data_from_window(self):
        """Передача данных после выбора файла в бд."""
        file = self.ui.lineEdit_path.text()

        if not file:
            QtWidgets.QMessageBox.warning(
                self,
                'File not selected',
                'Вы не выбрали файл для загрузки',
                QMessageBox.Ok)

        self.db.take_values_from_files(file)
        self.ui.lineEdit_path.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Runners()
    window.show()
    sys.exit(app.exec())
