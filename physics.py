from driver import animate_point
from driver import TIME_STEP
import numpy as np
G = np.array([0,9.81])
RHO = 1.2466
CdA = 0.045708296 * 0.54


class Ball:
    def __init__(self, x0, v0, a0, mass):
        self.x = x0       # m
        self.v = v0       # m/s
        self.a = a0       # m/s^2
        self.mass = mass  # kg

    def get_next_position(self):
        self.x = self.x + self.v * TIME_STEP + 0.5 * self.a * TIME_STEP ** 2
        self.v += self.a * TIME_STEP
        drag = 0.5 * RHO * self.v ** 2 * CdA 
        sum_forces = drag - self.mass * G
        self.a = sum_forces / self.mass  
        print (self.v)
        return self.x
 

