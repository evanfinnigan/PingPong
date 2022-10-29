# Author: Evan Finnigan, October 10 2022

import pygame
from random import randint
import math

# Gamesprite will be a subclass of Sprite
class GameSprite(sprite.Sprite):
    def __init__(self, speed, x, y, w, h, img):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


