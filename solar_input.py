# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import *

import yaml

def read_space_objects_data_from_file(input_filename):
    """Считывает данные с файла input_filename формата yaml и возвращает массив
    объектов класса body. ФОРМАТ ЗАПИСИ СМОТРИ В ФАЙЛЕ solar_system.yml!!!
    ДЛЯ ПОЛУЧЕНИЯ ПОВЕРХНОСТИ ШАРОВ В СОЗДАВАЕМОМ МАССИВЕ ИСПОЛЬЗУЙ ФУНКЦИЮ
    get_screen()(возвращает поверхность на которой будут все шары)
    """
    
    return objects


def write_space_objects_data_to_file(output_filename, space_objects):
    """Записывает данные о планетах из массива space_objects в файл
    output_filename формата yaml. ФОРМАТ ЗАПИСИ СМОТРИ В ФАЙЛЕ solar_system.yml!!!
    """
    

if __name__ == "__main__":
    print("This module is not for direct call!")
