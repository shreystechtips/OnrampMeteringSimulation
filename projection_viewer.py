# imports
import pygame as pg
import numpy as np
import main as rects
# modules

def rot_matrix(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, -s],
        [s, c]
    ])

class ProjectionViewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption('Traffic Simulation v1')
        self.background = (10, 10, 50)
        self.cars = rects.create_rects(250, size_x=10, size_y=10, lanes = range(50,800, 50))
        self.roads = []

        self.iterator = 0
        self.edge_color = (200,200,200)
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

        # test = pg.Rect(10 + self.iterator, 50, 50, 50)
        # self.iterator += 1
        # rects.update_rects(10,self.cars)
        # for rect in self.cars:
            # pg.draw.rect(self.screen, (50, 40, 30), rect.rect)
        # pg.draw.circle(self.screen, [255,255,255], r)
        for road in self.roads:
            pg.draw.circle(self.screen, [255,255,255], road.start, 5)
            pg.draw.circle(self.screen, [255,255,255], road.end, 5)
            self.draw_road(road)    

    def draw_road(self, road):
        length = np.linalg.norm(road.end - road.start)
        # print('length: ', length)
        radius = 0.5 * road.LANE_WIDTH * (road.right_lanes + road.left_lanes)
        angle = np.arccos((road.end[0] - road.start[0]) / length)
        pre_rotated = np.array([
            [0, -radius],
            [0, radius],
            [length, radius],
            [length, -radius]
        ])

        graphic_points = (pre_rotated - road.start) @ rot_matrix(angle) + road.start 
        # print(graphic_points[0])
        graphic_points[:,1] *= -1 # invert the y coordinates of the points bc pygame position has inverted y axis
        print(graphic_points)
        # print('rot: ', rot_matrix(angle))
        pg.draw.aaline(self.screen, self.edge_color,
        graphic_points[0], graphic_points[3])
        pg.draw.aaline(self.screen, self.edge_color,
        graphic_points[1], graphic_points[2])
        