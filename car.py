import pygame as pg
import random

lanes = range(50,1000,50)
class Car:
    def __init__(self, size_x, size_y, lane, horizontal, x_velocity, y_velocity):
        self.lane = lane
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.horizontal = horizontal
        self.rect =  pg.Rect(random.randint(10,1000), random.choice(lanes), size_x, size_y)