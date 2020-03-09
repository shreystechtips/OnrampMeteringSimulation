import numpy as np
import pygame as pg

from projection_viewer import ProjectionViewer

def main():
    pv = ProjectionViewer(1000, 1000)
    pv.run()


if __name__ == "__main__":
    main()