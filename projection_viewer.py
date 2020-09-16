# imports
import pygame as pg
import numpy as np
import main as rects
import constants as const
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
        '''
        self.cars = rects.create_rects(250, size_x=10, size_y=10, lanes = range(50,800, 50))
        self.roads = []
        self.cars_x,self.cars_y,self.velocity_x,self.velocity_y = rects.create_rects(50, size_x=const.CONST_CAR_SIZE_X, size_y=const.CONST_CAR_SIZE_Y, lanes = range(50,800, 50))
        '''
        self.map = []

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
            pg.time.delay(const.CONST_FRAME_TIME_MS)
    
 
    def display(self):
        self.screen.fill(self.background)
        self.draw_simpleroad()
        # this is the place to draw the components of the simulation

       

    def draw_simpleroad(self):
        for road in self.map['road']:
            pg.draw.aaline(
                self.screen,
                self.edge_color,
                road[0],
                road[1]
            )

        for lane in self.map['lane']:
            pg.draw.aaline(
                self.screen,
                [255,255,0],
                lane[0],
                lane[1]
            )
    '''
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
        # self.iterator += 1
        # self.cars_x,self.cars_y,self.velocity_x,self.velocity_y = rects.update_rects(self.cars_x,self.cars_y,self.velocity_x,self.velocity_y, self.iterator)
        # iter = 0
        # while iter < len(self.cars_x):
            # pg.draw.rect(self.screen, (50, 40, 30), pg.Rect(self.cars_x[iter][0],self.cars_y[iter][0],const.CONST_CAR_SIZE_X,const.CONST_CAR_SIZE_Y))
            # iter += 1
        translate = np.array([road.start[0], -road.start[1]])
        graphic_points = (pre_rotated  - translate) @ rot_matrix(angle) + translate 
        # print(graphic_points[0])
        graphic_points[:,1] *= -1 # invert the y coordinates of the points bc pygame position has inverted y axis
        print(graphic_points)
        # print('rot: ', rot_matrix(angle))
        pg.draw.aaline(self.screen, self.edge_color,
        graphic_points[0], graphic_points[3])
        pg.draw.aaline(self.screen, self.edge_color,
        graphic_points[1], graphic_points[2])
        '''        
