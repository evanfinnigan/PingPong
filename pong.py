# Author: Evan Finnigan, October 10 2022

from pygame import *
from random import randint
import math

colors = {
    "red" : (240,50,50),
    "blue" : (50,50,240),
}

rand_color = lambda : (randint(100,255),randint(100,255),randint(100,255))

# Gamesprite will be a subclass of Sprite
class GameSprite(sprite.Sprite):
    def __init__(self, speed, x, y, w, h, img):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = randint(speed-1,speed+1)
        self.y_speed = randint(speed-1,speed+1)
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Paddle(sprite.Sprite):
    def __init__(self, x, y, w, h, c, up, down):
        super().__init__()
        self.width = w
        self.height = h
        self.image = Surface((self.width,self.height))
        self.image.fill(c)
        self.col = c
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.up_key = up
        self.down_key = down
    def update(self):
        keys = key.get_pressed()
        if keys[self.down_key] and self.rect.y < 700 - 64:
            self.rect.y += self.speed
        if keys[self.up_key] and self.rect.y > 0:
            self.rect.y -= self.speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.x_speed > 0 and self.rect.x > 700-12:
            self.x_speed = -self.x_speed
        if self.x_speed < 0 and self.rect.x < 0:
            self.x_speed = -self.x_speed
        if self.y_speed > 0 and self.rect.y > 500-12:
            self.y_speed = -self.y_speed
        if self.y_speed < 0 and self.rect.y < 0:
            self.y_speed = -self.y_speed

window = display.set_mode((700,500))
background = transform.scale(image.load("img/banner.png"), (700,500))

b = Ball(2,100,100,12,12,"img/red_circle.png")
p1 = Paddle(50, 100, 15, 100, rand_color(), K_w, K_s)
p2 = Paddle(700 - 75, 100, 15, 100, rand_color(), K_UP, K_DOWN)

clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None,80)
p1_win = font.render("Player 1 Wins!", True, p1.col)
p2_win = font.render("Player 2 Wins!", True, p2.col)

# Game Loop
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
        b.update()
        b.draw()
        p1.update()
        p1.draw()
        p2.update()
        p2.draw()

        if sprite.collide_rect(p1, b) or sprite.collide_rect(p2, b):
            b.x_speed = -b.x_speed
            b.y_speed = randint(b.y_speed - 1, b.y_speed + 1)

        if b.rect.x <= 0:
            finished = True
            window.blit(p2_win, (170,200))

        if b.rect.x >= 700-12:
            finished = True
            window.blit(p1_win, (170,200))

    display.update()
    clock.tick(FPS)