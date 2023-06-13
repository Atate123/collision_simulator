from physics import Ball, G
from driver import animate_point, TIME_STEP
import numpy as np

# functions and classes go here


def get_points(time):
    myBall = Ball(np.array([2,10.0]), np.array([5.0,0]), np.array([0,0]), 1.0)
    points = []
    for i in range(int(time / TIME_STEP)):
        points.append(myBall.get_next_position())
    return points

    
if __name__ == "__main__":

    animate_point(get_points(10))
