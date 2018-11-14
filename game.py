#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
from pyglet.window.key import MOD_CTRL, DOWN, UP, LEFT, RIGHT
import random
from math import sin, cos, radians, pi

window = pyglet.window.Window(1000, 800)
batch = pyglet.graphics.Batch()   # pro optimalizované vyreslování objektů


class SpaceObject(object):

    def __init__(self, img_file,
                 x=None, y=None,
                 direction=None,
                 speed=None, rspeed=None):

        # nečtu obrázek
        self.image = pyglet.image.load(img_file)
        # střed otáčení dám na střed obrázku
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        # z obrázku vytvořím sprite
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

        # pokud není atribut zadán vytvořím ho náhodně
        self._x = x if x is not None else random.randint(0, window.width)
        self._y = y if y is not None else random.randint(0, window.height)
        # musím správně nastavit polohu sprite
        self.x = self._x
        self.y = self._y
        
        self.direction = direction \
            if direction is not None else random.randint(0, 359)
        # rychlost pohybu
        self.speed = speed \
            if speed is not None else random.randint(130, 180)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new):
        self._x = self.sprite.x = new

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new):
        self._y = self.sprite.y = new

    def tick(self, dt):
        self.x += dt * self.speed * cos(pi / 2 - radians(self.direction))
        self.sprite.x = self.x
        self.y += dt * self.speed * sin(pi / 2 - radians(self.direction))
        self.sprite.y = self.y
        
        
        
    """
    def tick(self, dt):
        self.bounce()

        # do promenne dt se uloží doba od posledního tiknutí
        self.x += dt * self.speed * cos(pi / 2 - radians(self.direction))
        self.sprite.x = self.x
        self.y += dt * self.speed * sin(pi / 2 - radians(self.direction))
        self.sprite.y = self.y
        self.sprite.rotation += 0.01 * self.rspeed
    """

a = SpaceObject('SpaceShooterRedux/PNG/playerShip1_red.png', x=500,y=400)
pyglet.clock.schedule_interval(a.tick, 1 / 30)

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(sym, mod):
    if sym == UP:
        a.direction = 0
        a.rotation = 0
    elif sym == DOWN:
        a.direction = 180
        a.rotation = 180
    elif sym == LEFT:
        a.direction = 270
        a.rotation = 270
    elif sym == RIGHT:
        a.direction = 90
        a.rotation = 90
    


pyglet.app.run()
