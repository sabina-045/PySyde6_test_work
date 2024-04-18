import json
import re

from PySide6 import QtWidgets, QtSql
from PySide6.QtSql import QSqlQuery

from app.utils import (count_time_diff, sort_dict,
                       time_format_for_total_result_table)


class DataBase:
    """Класс для работы с бд."""
    def __init__(self):
        super(DataBase, self).__init__()
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('runners.db')
        self.db.open()

        if not self.db.open():
            QtWidgets.QMessageBox.critical(
                None,
                'Connection to database denied',
                'Please, click cancel to exit',
                QtWidgets.QMessageBox.Cancel)

        create_table_query = QSqlQuery()
        create_table_query.exec(
            'CREATE TABLE IF NOT EXISTS competitors ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'number INTEGER UNIQUE,'
            'name VARCHAR(60),'
            'surname VARCHAR(100))')
        create_table_query.exec(
            'CREATE TABLE IF NOT EXISTS race_results ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'number INTEGER,'
            'status VARCHAR(10),'
            'time VARCHAR(20))')
        create_table_query.exec(
            'CREATE TABLE IF NOT EXISTS total_results ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'number INTEGER UNIQUE,'
            'name VARCHAR(60),'
            'surname VARCHAR(100),'
            'result VARCHAR(20))')

    def execute_query_with_params(self, sql_query, query_values=None):
        """Передаем запрос в бд."""
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        query.exec()

        return query

    def take_values_from_files(self, file_path=None):
        """"Загружаем файлы в бд."""

        if re.match(r'^.*\.json$', file_path):
            with open(file_path, encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    values = [key, value.get('Name'), value.get('Surname')]
                    sql_query = (
                        'INSERT INTO competitors (number, name, surname) VALUES (?, ?, ?)')

                    self.execute_query_with_params(sql_query, values)

        if re.match(r'^.*\.txt$', file_path):
            with open(file_path, encoding='utf-8-sig') as f:
                data = f.read()
                lines = data.strip().split('\n')
                for line in lines:
                    new_line = line.split()
                    values = [int(new_line[0]), new_line[1], new_line[2]]
                    sql_query = (
                         'INSERT INTO race_results (number, status, time) VALUES (?, ?, ?)')

                    self.execute_query_with_params(sql_query, values)

    def check_table_is_not_empty(self, table_name):
        """Проверяем, что таблица не пустая."""
        query = QSqlQuery()
        query.exec(f'SELECT * FROM {table_name} LIMIT 2')
        if not query.next():
            if table_name == 'total_results':
                QtWidgets.QMessageBox.warning(
                    None,
                    'Empty table',
                    f'Пожалуйста, загрузите данные'
                    f' в таблицы "competitors" и "race_results",'
                    f' потом произведите подсчет результатов',
                    QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.warning(
                    None,
                    'Empty table',
                    f'Пожалуйста, загрузите данные в таблицу {table_name}',
                    QtWidgets.QMessageBox.Ok)

        return True

    def total_results_count(self):
        """Подсчитываем общий результат забега."""
        self.check_table_is_not_empty('competitors')
        self.check_table_is_not_empty('race_results')
        query = QSqlQuery()
        query.exec('SELECT DISTINCT number FROM race_results')
        nums = []
        res_dict = {}
        while query.next():
            nums.append(query.value(0))
        for num in nums:
            times = []
            query.exec(f"SELECT time FROM race_results WHERE number == {num} and status == 'start'")
            while query.next():
                times.append(query.value(0))
            query.exec(f"SELECT time FROM race_results WHERE number == {num} and status == 'finish'")
            while query.next():
                times.append(query.value(0))
            total_result = count_time_diff(times)
            res_dict[num] = total_result

        for key, value in sort_dict(res_dict).items():
            query = QSqlQuery()
            values = []
            query.exec(
                f"SELECT name, surname FROM competitors WHERE competitors.number == {key}")
            total_time = time_format_for_total_result_table(value)
            while query.next():
                values.extend((key, query.value(1), query.value(0), total_time))
            sql_query = (
                'INSERT INTO total_results (number, name, surname, result) VALUES (?, ?, ?, ?)')
            self.execute_query_with_params(sql_query, values)

    def data_from_table_total_results(self):
        """Получем данные из таблицы с итоговыми результатами."""
        data = []
        query = QSqlQuery()
        query.exec("SELECT * FROM total_results")
        while query.next():
            data.extend(
                [(query.value(0), query.value(1), query.value(2), query.value(3), query.value(4))])

        return data
