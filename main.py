import pygame as pg
import random
import time
import sys
from car import Car


def update_rects(iterator_x, cars, iterator_y=0, x_screen = 1000, update_time = 50/100):
    for car in cars:
        if car.x_velocity < 1:
            car.x_velocity = random.randint(1, 10)
        car.rect.left = (car.rect.left + car.x_velocity*update_time)%x_screen
        car.rect.top += car.y_velocity*update_time


def create_rects(num_rects, size_x=30, size_y=30, lanes=[50, 100], x_screen=690):
    cars = []
    for i in range(num_rects):
        cars.append(Car(size_x, size_y, 1 , random.randint(10, x_screen), random.randint(1, 10), 0))
    return cars
