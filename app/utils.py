from datetime import datetime
import json
import os


def count_time_diff(times):
    """Находим разницу во времени."""
    time_format = '%H:%M:%S,%f'
    start_time = datetime.strptime(times[0], time_format)
    finish_time = datetime.strptime(times[1], time_format)
    diff = finish_time - start_time

    return diff


def sort_dict(res_dict):
    """Сортируем словарь."""
    sorted_list = sorted(res_dict.items(), key=lambda x: x[1])
    sorted_dict = dict(sorted_list)

    return sorted_dict


def time_format_for_total_result_table(value):
    """Конвертируем время."""
    str_value = str(value)
    new_value = str_value[2:10].replace('.', ',')

    return new_value


def convert_data_to_json(data):
    """Конвертируем данные в json."""
    dict_for_json = {}
    for elem in data:
        dict_for_json[elem[0]] = {'Нагрудный номер': elem[1],
                                  'Имя': elem[2],
                                  'Фамилия': elem[3],
                                  'Результат': elem[4],
                                  }
    cwd = f'{os.getcwd()}/results_json'
    file_name = "total_results.json"
    path = os.path.join(cwd, file_name)
    with open(path, "w", encoding='utf-8') as wf:
        json.dump(dict_for_json, wf, ensure_ascii=False)
