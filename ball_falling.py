from physics import Ball, G, BOUNDS, Ball2, Simulation
from driver import animate_point, TIME_STEP
import numpy as np
import random
DEFAULT_CdA = 0.045708296 * 0.54

# functions and classes go here

'''def get_points(time):
    myBall = Ball(np.array([[-4.0,10.0],  
                           [25.0,10.0],  
                           [0.0, 0.0]]), 
                            1.0,       
                            DEFAULT_CdA)          
    points = []
    for i in range(int(time / TIME_STEP)):
        points.append(myBall.get_next_position())   
    return points
'''
def f():
    return random.random() * BOUNDS / 1.25 * random.choice([-1,1])



def get_points(time):
    balls = [Ball2(np.array([[abs(f()), abs(f())],
                            [4 * f(), 4 *f()],
                            [0.0, 0.0]]),1.0, 0) for _ in range(100)]
    points_matrix = []
    for ball in balls:
        points = []
        for _ in range(int(time / TIME_STEP)):
            points.append(ball.get_next_position())
        points_matrix.append(points)
    
    
    return np.array(points_matrix)


if __name__ == "__main__":
   # points_matrix = get_points(20)
    sim = Simulation(10,10)
    points_matrix = sim.generate_points_matrix()
    
    print(points_matrix.shape)

    animate_point(points_matrix[:,::2,:])
