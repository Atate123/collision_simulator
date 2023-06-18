from driver import animate_point, TIME_STEP, BOUNDS
import numpy as np
G = np.array([0,9.81])
RHO = 1.2466

PHYSICS_TIME_STEP = TIME_STEP * 0.5

class Simulation:
    #1 has list of balls
    #2 a function to generate list of balls (init)
    #3 a function to check for collisions 
    #4 a function to iterate throguh the balls and update their positions
    
        # once you do 3 and 4 you can set it up to return one frame every time its called. 

    #
    pass

class Ball2:
    def __init__(self, params, mass, CdA):
        self.x = params[0]      # m
        self.v = params[1]      # m/s
        self.a = params[2]      # m/s^2
        self.mass = mass        # kg
        self.CdA = CdA          # unitless

    def get_next_position(self):
        self.x = self.x + self.v * PHYSICS_TIME_STEP + 0.5 * self.a * PHYSICS_TIME_STEP ** 2
        for i, position in enumerate(self.x):
            if position > BOUNDS or position < -BOUNDS:
                self.v[i] *= -1.0
        if abs(self.x[0]) < 0.25 and (self.x[1] < -1.5 or self.x[1] > 1.5):
            self.v[0] *= -1.0
        

        self.v += self.a * PHYSICS_TIME_STEP
        drag = 0.5 * RHO * self.v ** 2 * self.CdA 
        sum_forces = drag - self.mass * G
        self.a = sum_forces / self.mass  
        return self.x

class Ball:
    def __init__(self, params, mass, CdA):
        self.x = params[0]      # m
        self.v = params[1]      # m/s
        self.a = params[2]      # m/s^2
        self.mass = mass        # kg
        self.CdA = CdA          # unitless

    def get_next_position(self):
        self.x = self.x + self.v * TIME_STEP + 0.5 * self.a * TIME_STEP ** 2
        for i, position in enumerate(self.x):
            if position > BOUNDS or position < -BOUNDS:
                self.v[i] *= -1.0
            #    print(f"CURRENTLY OUT OF BOUNDS: {self.x=} {self.v=}")
        self.v += self.a * TIME_STEP
        drag = 0.5 * RHO * self.v ** 2 * self.CdA 
        sum_forces = drag - self.mass * G
        self.a = sum_forces / self.mass  
        return self.x
 

