#imports
import pygame as pg
import random
import time
import sys
import numpy as np 
import constants as const


def update_rects(iterator_x, cars_x,cars_y,velocity_x,velocity_y, iterator_y=0, x_screen = 1000, update_time = const.CONST_FRAME_TIME_MS/100):
    cars_x = np.add(cars_x,velocity_x*update_time)
    cars_y = np.add(cars_y,velocity_y*update_time)
    return cars_x,cars_y


def create_rects(num_rects, size_x=30, size_y=30, lanes=[50, 100], x_screen=690):
    cars_x = np.zeros(shape=(num_rects, 1))
    cars_y = np.zeros(shape=(num_rects, 1))
    velocity_x = np.zeros(shape=(num_rects, 1))
    velocity_y = np.zeros(shape=(num_rects, 1))
    iter = 0
    while(iter < num_rects):
        cars_x[iter] = random.randint(10, x_screen) + 0.0 #horizontal pos
        cars_y[iter] = random.choice(const.CONST_LANES) + 0.0 #vertical pos
        velocity_x[iter] = random.randint(1, 10) + 0.0 #init velocity x
        velocity_y[iter] = 0 + 0.0 #init velocity y
        iter += 1 
    return cars_x,cars_y,velocity_x,velocity_y