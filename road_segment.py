import numpy as np

def rot_matrix(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, -s],
        [s, c]
    ])

class Road_Segment:
    def __init__(self, start, end, right_lanes=1, left_lanes=1):
        # CONSTANTS        
        self.LANE_WIDTH = 10
        self.DRIVES_LEFT = False

        # fields
        self.right_lanes = right_lanes
        self.left_lanes = left_lanes

        self.start = np.array(start)
        self.end = np.array(end)

        self.cars = []


