from driver import animate_point, TIME_STEP, BOUNDS
import numpy as np
G = np.array([0,9.81])
RHO = 1.2466



class Ball:
    def __init__(self, x0, v0, a0, mass, CdA = 0.045708296 * 0.54):
        self.x = x0       # m
        self.v = v0       # m/s
        self.a = a0       # m/s^2
        self.mass = mass  # kg
        self.CdA = CdA

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
 

