import pygame
import os
import parameters
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, power, angle, shoot):
        self.image= image
        self.x = x
        self.y = y
        self.power= power
        self.angle= angle
        self.shoot = False
        self.time = 0