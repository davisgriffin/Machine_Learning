import pygame
import math
from sprites.Laser import Laser

RIGHT = 1
LEFT = 0

class Cannon():
    def __init__(self, pos, screen_size):
        super().__init__()

        self.x, self.y = pos
        self.screen_size = screen_size

        self.image = pygame.image.load('../../graphics/cannon.png') \
            .convert_alpha()
        # self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=pos)

        self.theta = 0
        self.delta_theta = 1

        self.lives = 3
        self.is_alive = True

        self.reload_time = 30
        self.reload_timer = 0

        # self.pivot = (self.rect.centerx, self.rect.bottom)

    def rotate_cannon(self, direction):
        if direction == 1:
            self.theta += self.delta_theta
            self.x += math.cos(self.theta) * self.rect.width
            if self.theta > 0:
                self.y -= math.sin(self.theta) * self.rect.height
            else:
                self.y += math.sin(self.theta) * self.rect.height
        else:
            self.theta -= self.delta_theta
            self.x -= math.cos(self.theta) * self.rect.width
            if self.theta > 0:
                self.y += math.sin(self.theta) * self.rect.height
            else:
                self.y -= math.sin(self.theta) * self.rect.height
        self.image = pygame.transform.rotozoom(self.image, -self.theta, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def fire(self) -> Laser:
        self.reload_timer = self.reload_time
        return Laser(self.theta, (self.x, self.y), self.screen_size)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.theta < 90:
            self.rotate_cannon(RIGHT)
        elif keys[pygame.K_LEFT] and self.theta > -90:
            self.rotate_cannon(LEFT)
        elif keys[pygame.K_SPACE] and self.reload_timer == 0:
            self.fire()
