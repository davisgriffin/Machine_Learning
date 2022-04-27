# https://github.com/monokim/framework_tutorial/blob/master/gym_game/envs/pygame_2d.py

import pygame
import numpy as np
import math
import random
from sprites.Cannon import Cannon
from sprites.Tower import Tower
from sprites.Asteroid import Asteroid

screen_width = 800
screen_height = 600


class SpaceTowerDefense():
    def __init__(self, screen):
        self.screen = screen

        self.tower = Tower((screen_width/2, screen_height))
        self.cannon = Cannon(
            (self.tower.rect.centerx, self.tower.rect.top),
            (screen_width, screen_height)
        )
        self.asteroids = [
            Asteroid(screen_width, self.cannon.rect.center)
        ] * 100

        self.hit_reward = 100
        self.game_over_reward = -100

        self.hit_target = False

    def run(self):
        self.cannon.get_input()
        self.screen.blit(self.cannon.image, self.cannon.rect)
        self.screen.blit(self.tower.image, self.tower.rect)

    def action(self, action):
        if action != 2:
            self.cannon.rotate_cannon(action)

        self.cannon.update()

        if action == 2:
            # check for reload and fire
            self.cannon.fire()

        self.cannon.check_hit()

    def get_asteroid_positions(self):
        return [(asteroid.x, asteroid.y) if not asteroid.paused else () for asteroid in self.asteroids]

    def get_reward(self):
        if self.hit_target:
            return self.hit_reward
        elif not self.cannon.is_alive:
            return self.game_over_reward

        return 0

    def is_done(self):
        if not self.cannon.is_alive or len(self.asteroids) == 0:
            return True

        return False


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = SpaceTowerDefense(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
