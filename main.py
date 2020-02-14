import pygame as pg
import random
import time
from projection_viewer import ProjectionViewer as main_thread
import sys


def update_rects(iterator_x, rects, iterator_y=0):
    print(pg.Rect(10,
                  random.randint(10, 690), 10, 10))
    for rect in rects:
        rect.left += iterator_x
        rect.top += iterator_y


def create_rects(num_rects, size_x=30, size_y=30, lanes=[50, 100], x_screen=690):
    rects = []
    for i in range(num_rects):
        rects.append(pg.Rect(random.randint(10, x_screen),
                             random.choice(lanes), size_x, size_y))
    return rects
