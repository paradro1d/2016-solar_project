# coding: utf-8
# license: GPLv3

from tkinter.filedialog import *
from solar_vis import *
from solar_model import *
from solar_input import *

init()


def execution(dt, space_objects, physical_time, actual_time, time_step):
    """Функция исполнения. Просчитывает движения тел в массиве space_objects
    с шагом dt за временной период time_step. physical_time, actual_time -
    Физическое время и время наблюдения на компьютере(в кадрах). Возвращает
    physical_time, space_objects, actual_time после обработки
    """
    if dt != 0:
        actual_time += 1
        while physical_time < actual_time * time_step:
            for body in space_objects:
                body.calcuate_force(space_objects)
                body.move_space_object(dt)
                if body.check():
                    space_objects.remove(body)
            physical_time += dt
    return (physical_time, space_objects, actual_time)


def open_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Возвращает список небесных тел с их параметрами, пригодный
    для обработки.
    """
    in_filename = askopenfilename()
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)
    for obj in space_objects:
        if (obj.type != 'star') and (obj.type != 'planet'):
            AssertionError()
    return space_objects


def save_file_dialog(space_objects):
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию сохранения параметров системы небесных тел в данный файл.
    """
    out_filename = asksaveasfilename()
    write_space_objects_data_to_file(out_filename, space_objects)


def main():
    finished = False
    """Флаг цикличности выполнения программы"""

    color_buttons = (66, 145, 255)
    """Цвета кнопок"""

    physical_time = 0
    """Физическое время моделирования в секундах"""

    time_step = 0
    """Количество проходящего физического времени за кадр.
    Равно нулю при остановке моделирования"""

    time_field = ''
    """Поле для ввода time_step"""

    FPS = 30
    """Число кадров в секунду"""

    actual_time = 0
    """Счетчик кадров"""

    start_button = button(color_buttons, (10, 10, 50, 25), 'Start')
    save_system_button = button(
        color_buttons, (10, 35, 150, 25), 'Save into file')
    set_system_button = button(color_buttons, (10, 60, 75, 25), 'Set file')
    """Кнопки старта/остановки, сохранения, загрузги соответственно"""

    space_objects = []
    """Массив небесных тел"""

    clock = pygame.time.Clock()

    dt = 0.001
    """Шаг моделирования (вляет на точность)"""
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check():
                    if (time_step == 0) and (time_field != ''):
                        if float(time_field) != 0:
                            time_step = float(time_field)
                            start_button.text = 'Pause'
                    else:
                        time_step = 0
                        start_button.text = 'Start'
                if set_system_button.check():
                    space_objects = open_file_dialog()
                    time_step = 0
                    physical_time = 0
                    actual_time = 0
                if save_system_button.check():
                    save_file_dialog(space_objects)
                    time_step = 0
            elif event.type == pygame.KEYDOWN:
                time_field = key_check(
                    pygame.key.name(event.key), time_field, '0123456789.')

            physical_time, space_objects, actual_time = execution(
                dt, space_objects, physical_time,
                actual_time, time_step
            )

            start_button.draw()
            set_system_button.draw()
            save_system_button.draw()

            write_text(
                'Enter time step per frame (30 frames per second): ' + str(
                    time_field), (150, 10))
            write_text('Time:' + str(physical_time), (150, 65))

            draw_objects(space_objects)

            pygame.display.update()
            clock.tick(FPS)
            fill()


if __name__ == "__main__":
    main()

quit_()
