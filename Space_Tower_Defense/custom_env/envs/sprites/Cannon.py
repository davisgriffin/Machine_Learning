import pygame


class Cannon():
    def __init__(self, pos):
        super().__init__()

        self.x, self.y = pos

        self.image = pygame.image.load('../../graphics/cannon.png') \
            .convert_alpha()
        # self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=pos)

        self.theta = 0
        self.delta_theta = 1

        self.lives = 3
        self.is_alive = True

        # self.pivot = (self.rect.centerx, self.rect.bottom)

    def rotate_cannon(self):
        pass

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.theta < 90:
            self.theta += self.delta_theta
        elif keys[pygame.K_LEFT] and self.theta > -90:
            self.theta -= self.delta_theta

    def update(self):
        pass
