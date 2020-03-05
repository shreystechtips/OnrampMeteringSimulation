import numpy as np



class Road:
    def __init__(self, start, end, right_lanes=1, left_lanes=1):
        # CONSTANTS        
        self.LANE_WIDTH = 50
        self.DRIVES_LEFT = False

        # fields
        self.id = 'blah'
        self.right_lanes = right_lanes
        self.left_lanes = left_lanes

        self.start = np.array(start)
        self.end = np.array(end)
    
        self.numpy_form = np.array(
            np.array(())
        )
    
