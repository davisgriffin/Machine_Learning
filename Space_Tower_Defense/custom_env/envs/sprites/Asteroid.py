import pygame
import random
import math


class Asteroid():
    def __init__(self, screen_width, cannon_pos):
        self.radius = 20

        # -x axis, +x axis, +y axis
        self.spawn_points = (
            -self.radius,
            screen_width + self.radius,
            -self.radius
        )

        self.x = random.randint(
            self.spawn_points[0], self.spawn_points[1])
        self.y = self.spawn_points[2]

        self.speed = 20
        self.get_speed(cannon_pos)
        self.paused = True

    def get_speed(self, cannon_pos):
        self.theta = 1.2 * \
            math.atan(self.y - cannon_pos[1] / self.x - cannon_pos[0])

        if self.x < cannon_pos[0]:
            self.speedy = math.sin(self.theta) * self.speed
            self.speedx = math.cos(self.theta) * self.speed
        else:
            self.speedy = math.sin(self.theta) * self.speed
            self.speedx = -math.cos(self.theta) * self.speed
