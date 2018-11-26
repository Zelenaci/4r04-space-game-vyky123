#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
from pyglet.window.key import DOWN, UP, LEFT, RIGHT
from random import randint, choice
from math import sin, cos, radians, pi
import glob

window = pyglet.window.Window(1000, 800)
batch = pyglet.graphics.Batch()   # pro optimalizované vyreslování objektů

class SpaceObject(object):
    def __init__(self, img_file,
                 x=None, y=None, direction=None, speed=None):

        # nečtu obrázek
        self.image = pyglet.image.load(img_file)
        # střed otáčení dám na střed obrázku
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        # z obrázku vytvořím sprite
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

        # pokud není atribut zadán vytvořím ho náhodně
        self._x = x if x is not None else randint(0, window.width)
        self._y = y if y is not None else randint(0, window.height)
        # musím správně nastavit polohu sprite
        self.x = self._x
        self.y = self._y
        
        self.direction = direction \
            if direction is not None else randint(0, 359)
        # rychlost pohybu
        self.speed = speed \
            if speed is not None else randint(130, 180)
                
        self.klavesy = set()

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
        
        for sym in a.klavesy:
            if 32 in a.klavesy:
                meet.add_laser()
                
            if UP in a.klavesy:
                if LEFT in a.klavesy:
                    a.direction = 315
                    a.speed = 180
                elif RIGHT in a.klavesy:
                    a.direction = 45
                    a.speed = 180
                else:
                    a.direction = 0
                    a.speed = 180
            elif DOWN in a.klavesy:
                if LEFT in a.klavesy:
                    a.direction = 225
                    a.speed = 180
                elif RIGHT in a.klavesy:
                    a.direction = 115
                    a.speed = 180
                else:
                    a.direction = 180
                    a.speed = 180
            elif LEFT in a.klavesy:
                a.direction = 270
                a.speed = 180
            elif RIGHT in a.klavesy:
                a.direction = 90
                a.speed = 180
            
        
        if a.x < 50:
            a.x += 1
        elif a.x > window.width-50:
            a.x -= 1
        if a.y < 40:
            a.y += 1 
        elif a.y > window.height-40:
            a.y -= 1
        
        #print(pyglet.clock.get_fps())
        
        
class Meteor(SpaceObject):
    def __init__(self, x=None, y=None, direction=None,
                 speed=None, rspeed=None):
        y = window.height + 50
        file_list = glob.glob('img/meteor*.png')
        img_file = choice(file_list)
        super().__init__(img_file, x, y)
        self.speed = speed if speed is not None else randint(50, 200)
        self.rspeed = rspeed if rspeed is not None else randint(- 40, 40)
        self.direction = direction if direction is not None else randint(120, 240)

class Laser(SpaceObject):
    def __init__(self, img_file='img/laser.png', speed=800):
        # načtu obrázek
        self.image = pyglet.image.load(img_file)
        # střed otáčení dám na střed obrázku
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height
        # z obrázku vytvořím sprite
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)
        self.sprite.z = 0
        self.direction = 0
        self.speed = speed

        self.x = a.x
        self.y = a.y + 100

        
class Meet():
    meteors = []
    lasers = []
    def __init__(self, count):
        for _ in range(count):
            self.add_meteor()
    
    def add_meteor(self, dt=None):
        self.meteors.append(Meteor())
        
    def add_laser(self, dt=None):
        self.lasers.append(Laser())
        
        
           
    def tick(self, dt):
        for meteor in self.meteors:
            meteor.tick(dt)
            if meteor.x < -50 or meteor.y < -50 or meteor.x > window.width+50:
                meteor.sprite.delete()
                self.meteors.remove(meteor)
                
        
        
        pos = a.x, a.y
        metpos = m.x, m.y





a = SpaceObject('SpaceShooterRedux/PNG/playerShip1_red.png', x=500,y=100,speed=0,direction=0)
m = Meteor()


meet = Meet(10)
pyglet.clock.schedule_interval(meet.tick, 1 / 30)
pyglet.clock.schedule_interval(meet.add_meteor, 1/2)
pyglet.clock.schedule_interval(a.tick, 1 / 30)

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(sym, mod):
    print(sym)
    a.klavesy.add(sym)

@window.event
def on_key_release(sym, mod):
    a.klavesy.remove(sym)
    a.speed = 0

pyglet.app.run()
