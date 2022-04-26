import pygame


class Tower():
    def __init__(self, pos):
        self.image = pygame.image.load('../../graphics/tower.png') \
            .convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(
            midbottom=pos
        )
