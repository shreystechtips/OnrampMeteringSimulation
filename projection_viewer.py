# imports
import pygame as pg
import numpy as np
# modules
import graphics as gp
'''
KEY_TO_FUNCTION = {
    pg.K_LEFT : (lambda x : x.translate_all((-10,0,0))),
    pg.K_RIGHT : (lambda x : x.translate_all((10,0,0))),
    pg.K_DOWN : (lambda x : x.translate_all((0,10,0))),
    pg.K_UP : (lambda x : x.translate_all((0,-10,0))),
    pg.K_EQUALS : (lambda x : x.scale_all(1.25)),
    pg.K_MINUS : (lambda x : x.scale_all(0.8)),
    pg.K_r : (lambda x : x.rotate_y_all(1.57 / 6))
}
'''
class ProjectionViewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption('Wireframe Display')
        self.background = (10, 10, 50)

        self.

    def run(self):
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    # if event.key in KEY_TO_FUNCTION:
                        # KEY_TO_FUNCTION[event.key](self)
            self.screen.fill(self.background)
            self.display()
            pg.display.flip()
    
    # def add_wireframe(self, name, wireframe):
        # self.wireframes[name] = wireframe
    
    def display(self):
        self.screen.fill(self.background)