# coding: utf-8
# license: GPLv3

from solar_objects import *
from solar_vis import *
import yaml

colors = {
    'red': (255, 0, 0), 'orange': (255, 91, 0), 'blue': (0, 0, 255),
    'green': (0, 255, 0), 'yellow': (255, 255, 0), 'white': (255, 255, 255),
    'gray': (120, 120, 120), 'cyan': (0, 255, 255)
    }
"""Словарь цветов"""


def read_space_objects_data_from_file(input_filename):
    """Считывает данные с файла input_filename формата yaml и возвращает массив
    объектов класса body. Формат записи массива для планеты:
    [<тип тела> <радиус в пикселях> <цвет> <масса> <x> <y> <Vx> <Vy>]
    """
    planets = yaml.load(open(input_filename), Loader=yaml.Loader)
    objects = []
    screen = get_screen()
    for body in planets.keys():
        b = Body(*planets[body], screen, body)
        b.dictcolor = b.color
        b.color = colors[b.color]
        b.x = float(b.x)
        b.y = float(b.y)
        b.Vx = float(b.Vx)
        b.Vy = float(b.Vy)
        b.m = float(b.m)
        objects.append(b)
    return objects


def write_space_objects_data_to_file(output_filename, space_objects):
    """Записывает данные о планетах из массива space_objects в файл
    output_filename формата yaml. Формат записи массива для планеты:
    [<тип тела> <радиус в пикселях> <цвет> <масса> <x> <y> <Vx> <Vy>]
    """
    data_dict = {}
    for body in space_objects:
        data_dict.update({body.name: [
            body.type, body.R, body.dictcolor, body.m,
            body.x, body.y, body.Vx, body.Vy
        ]})
    with open(output_filename, 'w') as yaml_file:
        yaml.dump(data_dict, yaml_file)


if __name__ == "__main__":
    print("This module is not for direct call!")
