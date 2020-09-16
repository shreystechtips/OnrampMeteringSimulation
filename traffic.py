import numpy as np

SPAWN_RATE = 5 # cars / 10 seconds
LIMIT = 15

NUM_ROAD_SEGMENTS = 3

class Traffic:
    def __init__(self, spawn_rate=SPAWN_RATE, limit=LIMIT):
        self.spawn_rate = spawn_rate
        self.positions = []
        self.travel_distance = []
        self.velocities = []
        self.current_road = []



    def time_step(self):
        pass


    # DISCLAIMER: this is a solution for a small amount of road segments (for now, there are 3)
    def sort_roads(self):
        # return array of enumerated numpy arrays
        # each np array contains the cars on a given road in order
        cars_on_road = [self.travel_distance[self.current_road == x] for x in range(NUM_ROAD_SEGMENTS)]
        for road in cars_on_road:
            road.sort()
        # self.travel_distance[self.current_road == 3] get the travel distances of cars on road 3
        