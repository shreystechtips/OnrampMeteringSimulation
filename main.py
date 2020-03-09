#imports
import pygame as pg
import random
import time
import sys
import numpy as np 
import constants as const
import math
import numba

@numba.jit
def is_sorted(start_ind, a):
    for i in range(start_ind -1, 0, -1):
         if i >=1 and a[i-1] > a[i] :
               return False, i
    return True, -1

def update_rects(cars_x,cars_y,velocity_x,velocity_y, iterator,  x_screen = 1000, y_screen = 1000, update_time = const.CONST_FRAME_TIME_MS/100):
    print('sort')
    cars_x_temp = np.add(cars_x,velocity_x*update_time) #x_screen
    cars_y_temp = np.add(cars_y,velocity_y*update_time)
    is_sort, index = is_sorted(cars_x_temp.size, cars_x_temp)
    while not is_sort:
        for x in range(0,cars_x_temp.size):
            if x < cars_x_temp.size-1:
                if cars_x_temp[x] > cars_x_temp[x+1]:
                    velocity_x[x] = velocity_x[x+1]
                    is_sort, index = is_sorted(cars_x_temp.size, cars_x_temp)
        print("not sort", index)
        velocity_x[index] = (velocity_x[index]-velocity_y[index+1])/2
        cars_x_temp = np.add(cars_x,velocity_x*update_time)
        is_sort, index = is_sorted(cars_x_temp.size, cars_x_temp)
        print(cars_x_temp)

    return cars_x_temp,cars_y_temp,velocity_x,velocity_y


def create_rects(num_rects, size_x=30, size_y=30, lanes=[50, 100], x_screen=690):
    cars_x = np.zeros(shape=(num_rects, 1))
    cars_y = np.zeros(shape=(num_rects, 1))
    velocity_x = np.zeros(shape=(num_rects, 1))
    velocity_y = np.zeros(shape=(num_rects, 1))
    cars = np.zeros(shape = (num_rects,1))
    iter = 0
    x_start = 5
    while(iter < num_rects):
        cars_x[iter] = x_start + random.randint(10, x_screen) + 0.0
        x_start = cars_x[iter]
        # random.randint(10, x_screen) + 0.0 #horizontal pos
        cars_y[iter] = 40 + 0.0 #vertical pos # random.choice(const.CONST_LANES)
        velocity_x[iter] =  random.randint(1, 10) + 0.0 #init velocity x
        velocity_y[iter] = 0.0 #init velocity y
        cars[iter] = pg.Rect(cars_x[iter], cars_y[iter], size_x, size_y)
        iter += 1 
    # np.sort()
    return cars_x,cars_y,velocity_x,velocity_y, cars