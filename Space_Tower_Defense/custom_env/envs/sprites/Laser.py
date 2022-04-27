import math

class Laser():
    def __init__(self, theta, start_pos, screen_size):
        self.length = math.sqrt(screen_size[0]**2 + screen_size[1]**2)
        self.startx, self.starty = start_pos
        self.theta = theta

        self.tracer_time = 15

        self.init_end_point()

    def init_end_point(self):
        self.endx = self.startx + math.cos(self.theta) * self.length
        self.endy = self.starty + math.sin(self.theta) * self.length
        
    def set_end_point(self, x, y):
        self.endx = x
        self.endy = y