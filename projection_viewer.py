# imports
import pygame as pg
import numpy as np
# modules

class ProjectionViewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption('Traffic Simulation v1')
        self.background = (10, 10, 50)


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
    
    
    def display(self):
        self.screen.fill(self.background)

        # this is the place to draw the components of the simulation

        test = pg.Rect(10 + self.iterator, 50, 50, 50)
        self.iterator += 1
        pg.draw.rect(self.screen, (50, 40, 30), test)


    def draw_road(road):
        pass