from driver import animate_point, TIME_STEP, BOUNDS
import numpy as np
import random

G = np.array([0,9.81])
RHO = 1.2466

PHYSICS_TIME_STEP = TIME_STEP * 0.5

def f():
    return random.random() * BOUNDS / 1.25 * random.choice([-1,1])

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
    
    def get_position(self):
        return self.x
    
    def flip_velocity(self):
        self.v *= 1

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
    
    def get_position(self):
        return self.x
    
    def flip_velocity(self):
        self.v *= 1
 

class Simulation:
    def __init__(self, number_of_balls,time):
        self.balls = [Ball2(np.array([[abs(f()), abs(f())],
                            [4 * f(), 4 *f()],
                            [0.0, 0.0]]),1.0, 0) for _ in range(number_of_balls)]
        self.time = time
    
    def check_for_collisions(self):
        for i in range(len(self.balls)):
            for j in range(i, len(self.balls)):
                dist = np.linalg.norm(self.balls[i].get_position() - self.balls[j].get_position())
                if dist < 0.25:
                    self.balls[i].flip_velocity()
                    self.balls[j].flip_velocity()

    def generate_points_matrix(self):
        points_matrix = []
        for ball in self.balls:
            points = []
            for _ in range(int(self.time / TIME_STEP)):
                # check for collisions
                self.check_for_collisions()
                points.append(ball.get_next_position())
            points_matrix.append(points)
        return np.array(points_matrix)
    