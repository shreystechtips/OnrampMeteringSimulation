import numpy as np
import pygame as pg
from road_segment import Road_Segment
from projection_viewer import ProjectionViewer
import maps

def main():
    pv = ProjectionViewer(1000, 1000)
    pv.map = maps.map1
    
    pv.run()


if __name__ == "__main__":
    main()