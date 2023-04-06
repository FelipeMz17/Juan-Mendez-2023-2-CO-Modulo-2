import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, HAMMER


class HammerThrow(Sprite):
    def __init__(self, x_pos, y_pos):
        self.image = HAMMER
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_pos
        self.image_rect.y = y_pos + 15
        self.image_rect.w -= 30
        self.image_rect.h -= 30 
        self.hammer_y = y_pos
        self.rotate = 0
    
    def update(self, hammers):
        self.image_rect.x += 10
        self.rotate += -15

        if self.image_rect.x > SCREEN_WIDTH:
            hammers.remove(self)

    def draw(self, screen):
        screen.blit(pygame.transform.rotate(self.image, self.rotate), (self.image_rect.x, self.hammer_y))
        #screen.fill((255, 0, 255), self.image_rect)