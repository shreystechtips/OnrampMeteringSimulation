import numpy as np
import pygame as pg
from road_segment import Road_Segment
from projection_viewer import ProjectionViewer

def main():
    pv = ProjectionViewer(1000, 1000)
    r_0 = Road_Segment((0, 0), (400, 400))
    r_1 = Road_Segment((400, 400), (300, 200))
    pv.roads.append(r_0)
    pv.roads.append(r_1)
    # for i in range(0,500,10):
        # pv.roads.append(Road_Segment((i,i),(10+i,10+i)))

    pv.run()


if __name__ == "__main__":
    main()