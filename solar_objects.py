# coding: utf-8
# license: GPLv3
import pygame
from solar_vis import *

gravitational_constant = 6.67408E-11


class Body:
    """Тип данных, описывающий звезду.
    содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, type, R, color, m, x, y, Vx, Vy, screen, name):
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = 0
        self.Fy = 0
        self.R = R
        self.color = color
        self.type = type
        self.screen = screen
        self.name = name

    def calculate_force(self, space_objects):
        """Вычисляет силу, действующую на тело.
        ѕараметры:
        **space_objects** Ч список объектов, которые воздействуют на тело.
        """
        self.Fx = self.Fy = 0
        for obj in space_objects:
            if obj != self:
                r = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
                self.Fx += gravitational_constant * self.m * obj.m * (
                    obj.x - self.x) / (r ** 3)
                self.Fy += gravitational_constant * self.m * obj.m * (
                    obj.y - self.y) / (r ** 3)

    def move_space_object(self, dt):
        """Перемещает тело в соответствии с действующей на него силой.
        ѕараметры:
        **body** - тело, которое нужно переместить.
        """
        ax = self.Fx/self.m
        self.x += self.Vx*dt
        self.Vx += ax*dt
        ay = self.Fy/self.m
        self.y += self.Vy*dt
        self.Vy += ay*dt

    def draw_object(self):
        """Прорисовка объекта"""
        pygame.draw.circle(self.screen, self.color, (
            scale_x(self.x), scale_y(self.y)), self.R)

    def check(self):
        """Проверка объекта на наличие в пределах экрана"""
        x = self.screen.get_width()
        y = self.screen.get_height()
        return (scale_x(self.x) < 0) or (scale_x(self.x) > x) or (
            scale_y(self.y) > y) or (scale_y(self.y) < 0)
