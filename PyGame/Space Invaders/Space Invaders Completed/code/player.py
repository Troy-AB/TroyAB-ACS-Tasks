import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, constraint, speed):
        #inherits data from pygame.sprite.Sprite

        super().__init__()
        self.image = pygame.image.load('D:\Documents\GitHub\TroyAB-ACS-Tasks\PyGame\Space Invaders\Space Invaders Completed\graphics\player.png').convert_alpha()
        self.rect  = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True

        self.laser_time = 0
        self.laser_cooldown = 600
        self.lasers = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks() # records time when button pressed

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown: # checks if 600ms has passed since laser pressed
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, -8, self.rect.bottom))

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()
