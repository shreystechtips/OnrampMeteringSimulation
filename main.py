import numpy as np
import random
import pygame as pg
import time
import sys
from pygame.locals import *


pg.init()
lanes = 2
lane_const = 20
lanes = [200, 300]
car_location = np.zeros([10, 10])
rects = []
w = pg.display.set_mode((700, 700))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


def init():
    # for i in range(10):
    #     rects.append(pg.Rect(random.choice(lanes),
    #                          random.randint(10, 690), 10, 10))
    #random.randint(10, 690)
    # random.choice(lanes)

    print(rects)


init()


w.fill(WHITE)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    for i in range(10):
        pg.draw.rect(w, BLUE, pg.Rect(30,
                                      30, 60, 60))
    w.fill(WHITE)
    pg.display.flip()
