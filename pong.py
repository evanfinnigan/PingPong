# Author: Evan Finnigan, October 10 2022

from pygame import *
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

window = display.set_mode((700,500))
background = transform.scale(image.load("img/banner.png"), (700,500))

clock = time.Clock()
FPS = 60

finished = False
run = True
while run:
    # Quitting the Game
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finished:

        # Render Content to the Display
        window.blit(background, (0,0))

    display.update()
    clock.tick(FPS)