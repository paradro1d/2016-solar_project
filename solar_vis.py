# coding: utf-8
# license: GPLv3

from pygame.draw import *
import pygame

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране,
принимают физические координаты
"""

window_width = 800
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = None
"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр."""


def init():
    '''
    Инициализирует модуль pygame и создает главную поверхность screen.
    также создает шрифт myfont для рисования текста.
    '''
    global screen
    global myfont
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    myfont = pygame.font.SysFont('Arial', 40)


def get_screen():
    '''
    Возвращает главную поверхность. Предназначен для использования
    в других модулях.
    '''
    global screen
    return screen


def fill():
    '''
    Заливает белым фон экрана
    '''
    global screen
    screen.fill((0, 0, 0))


def quit_():
    '''
    Выход из модуля pygame
    '''
    pygame.quit()


class button:
    '''
    Кнопка на поверности surface цвета color, являющаяся
    прямоугольником rect c текстом text.
    '''

    def __init__(self, color, rectan, text):
        '''
        Объявление объекта класса кнопки. Surface - поверхность,
        на которой она отображается. color - её цвет. rectan -
        прямоугольник, в который она вписана.
        text - текст на кнопке.
        '''
        global screen
        self.surface = screen
        self.color = color
        self.rect = rectan
        self.text = text

    def check(self):
        '''
        Проверяет положение курсора по отношению к кнопке.
        Если она внутри, то возвращает True. Иначе - False.
        '''
        x, y = pygame.mouse.get_pos()
        x0, y0, dx, dy = self.rect
        return ((x > x0) and (x < x0 + dx) and (y > y0) and (y < y0 + dy))

    def draw(self):
        '''
        Функция отрисовывает кнопку
        '''
        global myfont
        rect(self.surface, self.color, self.rect)
        if self.check():
            rect(self.surface, (65, 74, 76), self.rect)
        textsurface = myfont.render(self.text, False, (0, 0, 0))
        surf = pygame.Surface(textsurface.get_size(), pygame.SRCALPHA)
        surfscaled = pygame.Surface(
            (self.rect[2], self.rect[3]), pygame.SRCALPHA)
        surf.blit(textsurface, (0, 0))
        pygame.transform.smoothscale(
            surf, (self.rect[2], self.rect[3]), surfscaled)
        self.surface.blit(surfscaled, (self.rect[0], self.rect[1]))


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor**
    по данной характерной длине"""
    global scale_factor
    scale_factor = 0.4 * min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return int(x*scale_factor) + window_width//2


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

    Параметры:

    **y** — y-координата модели.
    """

    return int(y*scale_factor) + window_height//2


def write_text(text, coords):
    """Создает на экране текст.
    **space** - поверхность текста.
    **text** - строка текста.
    **coords** - коодрдинаты текста"""
    global myfont
    global screen
    textsurface = myfont.render(text, False, (255, 255, 255))
    x, y = textsurface.get_size()
    surf = pygame.Surface(textsurface.get_size(), pygame.SRCALPHA)
    surfscaled = pygame.Surface(
            (x // 2, y // 2), pygame.SRCALPHA)
    surf.blit(textsurface, (0, 0))
    pygame.transform.smoothscale(
            surf, (x // 2, y // 2), surfscaled)
    screen.blit(surfscaled, coords)


def key_check(string, text, alphabet):
    '''
    Обработка нажатия клавиши при вводе текста.
    Возвращает текст после нажатия клавиши.
    **text** - строка набираемого текста.
    **string** - текст вводимой клавиши.
    **aplhabet** - алфавит (допустимые для ввода символы).
    '''
    if string in alphabet:
        text = text + string
    elif string == 'backspace':
        text = text[0:len(text)-1]
    return text


def draw_objects(space_objects):
    '''
    Прорисовка массива space_objects объектов класса body.
    '''
    for body in space_objects:
        body.draw_object()


if __name__ == "__main__":
    print("This module is not for direct call!")
