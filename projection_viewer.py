# imports
import pygame as pg
import numpy as np
import main as rects
# modules

class ProjectionViewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption('Traffic Simulation v1')
        self.background = (10, 10, 50)
        self.cars = rects.create_rects(250, size_x=10, size_y=10, lanes = range(50,800, 50))


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
            pg.time.delay(50)
    
    
    def display(self):
        self.screen.fill(self.background)

        # this is the place to draw the components of the simulation

        test = pg.Rect(10 + self.iterator, 50, 50, 50)
        self.iterator += 1
        rects.update_rects(10,self.cars)
        for rect in self.cars:
            pg.draw.rect(self.screen, (50, 40, 30), rect.rect)


    def draw_road(road):
        pass