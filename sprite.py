import random

import pygame as pg


class Meteorite(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("Meteorite.png").convert_alpha()
        size = random.randint(70, 150)

        self.image = pg.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (800, random.randint(0, 600 - size))
        self.mask = pg.mask.from_surface(self.image)
        self.speedx = random.randint(3, 8)
        self.speedy = random.randint(-1, 8)


    def update(self):
        self.rect.y -= self.speedy
        self.rect.x -= self.speedx



class Mouse_starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("Mouse_starship.png").convert_alpha()
        size = random.randint(70, 150)

        self.image = pg.transform.scale(self.image, (size, size))
        self.image = pg.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, 600 - size), 0)
        self.mask = pg.mask.from_surface(self.image)
        self.speedy = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speedy


class Laser(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("laser.png").convert_alpha()

        self.image = pg.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect(midbottom=pos)
        self.mask = pg.mask.from_surface(self.image)
        self.speed = 3

    def update(self):
        self.rect.y -= self.speed


class Starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("cat_starship_horizontal.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (100, 100))
        self.image = pg.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midleft = (0, 300)
        self.mask = pg.mask.from_surface(self.image)
        self.mode = "vertical"

    def update(self):
        keys = pg.key.get_pressed()
        if self.mode == "horizontal":
            if keys[pg.K_a]:
                self.rect.x -= 20
            if keys[pg.K_d]:
                self.rect.x += 20

        if self.mode == "vertical":
            if keys[pg.K_w]:
                self.rect.y -= 5
            if keys[pg.K_s]:
                self.rect.y += 5

    def switch_mode(self):
        self.image = pg.image.load("cat_starship.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.midbottom = (400, 580)

        self.mode = "horizontal"


class Captain(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("captain.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (400, 400))

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.topleft = (-30, 600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"


class Alien(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("alien_cat.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (400, 400))

        self.rect = self.image.get_rect()

        self.rect.topleft = (-30, 600)
        self.mask = pg.mask.from_surface(self.image)
        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"
