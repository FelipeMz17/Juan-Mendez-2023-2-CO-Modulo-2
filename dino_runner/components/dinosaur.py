import pygame

from pygame.sprite import Sprite
from dino_runner.components.power_ups.hammer_throw import HammerThrow
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER, JUMP_SOUND, THROW_SOUND, DIE_SOUND, POWER_UP_SOUND, HEART, LESS_HEART_SOUND

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}


class Dinosaur(Sprite):

    X_POS = 150
    Y_POS = 300

    def __init__(self):
        self.jump_sound = pygame.mixer.Sound(JUMP_SOUND)
        self.jump_sound.set_volume(0.8)
        self.throw_sound = pygame.mixer.Sound(THROW_SOUND)
        self.throw_sound.set_volume(0.8)
        self.die_sound = pygame.mixer.Sound(DIE_SOUND)
        self.die_sound.set_volume(0.6)
        self.power_up_sound = pygame.mixer.Sound(POWER_UP_SOUND)
        self.power_up_sound.set_volume(0.6)
        self.less_heart_sound = pygame.mixer.Sound(LESS_HEART_SOUND)
        self.less_heart_sound.set_volume(0.6)
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect_x = self.X_POS
        self.dino_rect_y = self.Y_POS
        self.time_animation = 0
        self.jump_speed = -10
        self.in_jump = False
        self.has_power_up = False
        self.power_time_up = 0
        self.hammers = []
        self.can_throw = 0
        self.hearts = 5
    
    def update(self, user_input):
        # acciones por teclado
        if self.can_throw <= 0 and self.type == HAMMER_TYPE:
            if user_input[pygame.K_SPACE]:
                self.throw_sound.play()
                self.throw_hammer()
                self.can_throw = 40
        else:
            self.can_throw -= 1

        if self.in_jump:
            if user_input[pygame.K_DOWN]:
                self.jump_speed += 2
            self.jump()
        else:
            self.dino_rect_y = self.Y_POS + (user_input[pygame.K_DOWN] * 40)
            #print(self.jump_speed)
            if user_input[pygame.K_DOWN]:
                self.duck()
            elif user_input[pygame.K_UP]:
                self.in_jump = True
                self.jump_sound.play()
            else:
                self.run()
        #sumar animacion
        self.time_animation = self.time_animation + 1 if self.time_animation < 10 else 0
        #actualizar martillos
        for hammer in self.hammers:
            hammer.update(self.hammers)
            #print(hammer)

    def run(self):
        self.image = RUN_IMG[self.type][self.time_animation < 5] 

    def duck(self):
        self.image = DUCK_IMG[self.type][self.time_animation < 5]    

    def jump(self):
        self.image = JUMP_IMG[self.type]
        #aceleracion de salto y caida lobre
        self.dino_rect_y += self.jump_speed * 3
        self.jump_speed += 1
        #aterrizaje
        if self.dino_rect_y >= self.Y_POS:
            self.dino_rect_y = self.Y_POS
            self.in_jump = False
            self.jump_speed = -10

    def draw(self, screen): #dibujar el dinosaurio
        screen.blit(self.image, (self.dino_rect_x, self.dino_rect_y)) 
        self.dino_rect = self.image.get_rect() #obtener rectangulo de colosion
        #modificar el rectangulo de colision para hacerlo mas pequeño
        self.dino_rect.y = self.dino_rect_y + 15
        self.dino_rect.x = self.dino_rect_x + 25
        self.dino_rect.w -= 50
        self.dino_rect.h -= 40
        #screen.fill((255, 0, 255), self.dino_rect)
        for heart in range(0, self.hearts +1):
            screen.blit(HEART, (25 + (heart * 30), 30)) 

        for hammer in self.hammers:
            hammer.draw(screen)
    
    def reset_dinosaur(self):
        #volver al principio
        self.image = RUN_IMG[self.type][0]
        self.dino_rect_y = self.Y_POS
        self.time_animation = 0
        self.jump_speed = -10
        self.in_jump = False
        self.has_power_up = False
        self.power_time_up = 0
        self.hearts = 5

    def throw_hammer(self):
        hammer = HammerThrow(self.dino_rect_x +20, self.dino_rect_y + 20)
        self.hammers.append(hammer)
