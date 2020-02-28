# imports
import pygame as pg
import numpy as np
import main as rects
import constants as const
# modules

class ProjectionViewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption('Traffic Simulation v1')
        self.background = (10, 10, 50)
        self.cars_x,self.cars_y,self.velocity_x,self.velocity_y = rects.create_rects(50, size_x=const.CONST_CAR_SIZE_X, size_y=const.CONST_CAR_SIZE_Y, lanes = range(50,800, 50))


        self.iterator = 0
    def run(self):
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    pass
            self.screen.fill(self.background)
            self.display()
            pg.display.flip()
            pg.time.delay(const.CONST_FRAME_TIME_MS)
    
    
    def display(self):
        self.screen.fill(self.background)

        # this is the place to draw the components of the simulation
        self.iterator += 1
        self.cars_x,self.cars_y,self.velocity_x,self.velocity_y = rects.update_rects(self.cars_x,self.cars_y,self.velocity_x,self.velocity_y, self.iterator)
        iter = 0
        while iter < len(self.cars_x):
            pg.draw.rect(self.screen, (50, 40, 30), pg.Rect(self.cars_x[iter][0],self.cars_y[iter][0],const.CONST_CAR_SIZE_X,const.CONST_CAR_SIZE_Y))
            iter += 1

    def draw_road(road):
        pass