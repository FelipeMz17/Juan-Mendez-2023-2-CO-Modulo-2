import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(2, 5)
        self.power_up_disminution = 0
    
    def generate_power_up(self):
        power_up = random.choice([Shield(), Hammer()])
        self.power_ups.append(power_up)

    def update(self, game):
        self.duration -= 0.01

        if self.duration < 0 - self.power_up_disminution:
            self.generate_power_up()
            self.duration = random.randint(2, 5)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                game.player.power_up_sound.play()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up =  10
                self.power_up_disminution += 0.2
                self.power_ups.remove(power_up)
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset(self):
        self.power_ups = []
        self.duration = random.randint(2, 5)
        self.power_up_disminution = 0