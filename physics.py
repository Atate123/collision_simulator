from driver import animate_point

G = 9.81

class Ball:
    def __init__(self, x0, v0, a0):
        self.x = x0
        self.v = v0
        self.a = a0

    def get_next_position(self):
        # do some math

        return self.x
 

def get_points():
    myBall = Ball([0,10],[0,0],[0, G])
    points = []
    for i in range(10):
        points.append(myBall.get_next_position())
    return points

    
if __name__ == "__main__":
    animate_point(get_points())
