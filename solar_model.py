# coding: utf-8
# license: GPLv3
import pygame

RED = (255, 0, 0)

gravitational_constant = 6.67408E-11

class Body:
    """“ип данных, описывающий звезду.
    —одержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и еЄ цвет.
    """
    def __init__(self, m=0, x=0, y=0, Vx=0, Vy=0, Fx=0, Fy=0, R=5, color= RED):# Аттрибуты класса должны вводиться, а не быть заданными внутри класса. 
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
        self.R = R
        self.color = color# Добавить screen и type (звезда или солнце) как аттрибуты класса.
        
    def calculate_force(self, space_objects):
        """¬ычисл€ет силу, действующую на тело.
        ѕараметры:
        **space_objects** Ч список объектов, которые воздействуют на тело.
        """
        
        self.Fx = self.Fy = 0
        for obj in space_objects:
            r = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
            self.Fx += gravitational_constant*self.m*obj.m*(obj.x - self.x)/(r*r*r)
            self.Fy += gravitational_constant*self.m*obj.m*(obj.y - self.y)/(r*r*r)        

    def move_space_object(self, dt):
        """ѕеремещает тело в соответствии с действующей на него силой.
        ѕараметры:
        **body** Ч тело, которое нужно переместить.
        """
            
        ax = self.Fx/self.m
        self.x += self.Vx*dt
        self.Vx += ax*dt
        ay = self.Fy/self.m
        self.y += self.Vy*dt
        self.Vy += ay*dt
        
    def draw_object(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.R)
        
    def check(self):
    #Проверка на наличие в пределах экрана.