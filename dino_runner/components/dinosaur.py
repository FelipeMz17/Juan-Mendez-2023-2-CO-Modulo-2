import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING

class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING
        self.dino_rect = self.image[0].get_rect()
        self.dino_rect_x = 100
        self.dino_rect_y = 300
        self.time_animation = 0
        self.step_animation = 5
    
    def update(self):
        pass

    def run(self):
        pass

    def jump(self):
        pass

    def duck(self):
        pass

    def draw(self, screen):
        if self.time_animation < self.step_animation: #10 frames usando la primera imagen
            screen.blit(self.image[0], (self.dino_rect_x, self.dino_rect_y))
        elif self.time_animation < self.step_animation*2: #10 frames usando la segunda imagen
            screen.blit(self.image[1], (self.dino_rect_x, self.dino_rect_y))
        else: #retoma la animacion desde el principio
            self.time_animation = 0
            screen.blit(self.image[1], (self.dino_rect_x, self.dino_rect_y))
        #incrementar la animacion
        self.time_animation += 1
