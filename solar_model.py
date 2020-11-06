# coding: utf-8
# license: GPLv3
import pygame

RED = (255, 0, 0)

gravitational_constant = 6.67408E-11

class Body:
    """��� ������, ����������� ������.
    �������� �����, ����������, �������� ������,
    � ����� ���������� ������ ������ � �������� � � ����.
    """
    def __init__(self, m=0, x=0, y=0, Vx=0, Vy=0, Fx=0, Fy=0, R=5, color= RED):# ��������� ������ ������ ���������, � �� ���� ��������� ������ ������. 
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
        self.R = R
        self.color = color# �������� screen � type (������ ��� ������) ��� ��������� ������.
        
    def calculate_force(self, space_objects):
        """��������� ����, ����������� �� ����.
        ���������:
        **space_objects** � ������ ��������, ������� ������������ �� ����.
        """
        
        self.Fx = self.Fy = 0
        for obj in space_objects:
            r = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
            self.Fx += gravitational_constant*self.m*obj.m*(obj.x - self.x)/(r*r*r)
            self.Fy += gravitational_constant*self.m*obj.m*(obj.y - self.y)/(r*r*r)        

    def move_space_object(self, dt):
        """���������� ���� � ������������ � ����������� �� ���� �����.
        ���������:
        **body** � ����, ������� ����� �����������.
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
    #�������� �� ������� � �������� ������.