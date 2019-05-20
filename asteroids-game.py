from ggame import App, RectangleAsset, PolygonAsset, CircleAsset, LineAsset, ImageAsset, Frame, Sprite, LineStyle, Color
import math
import random

# Colors & lines
red = Color(0xff0000, 1.0)
orange = Color(0xffa500, 1.0)
yellow = Color(0xffff00, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
purple = Color(0x800080, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
gray = Color(0x888888, 0.5)
noline = LineStyle(0, black)
whiteline = LineStyle(1, white)
blackline = LineStyle(1, black)

class Bullet(Sprite):
    circ = CircleAsset(1, noline, black)
    
    def __init__(self, position, rotation):
        super().__init__(Bullet.circ, position)
        self.speed = 5
        self.vy = -1
        self.vx = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy

class Ship(Sprite):
    ship = PolygonAsset([(0,30), (15,0), (30,30), (15,15)], noline, black)
    
    def __init__(self, position, width, height):
        super().__init__(Ship.ship, position)
        self.gamewidth = width
        self.gameheight = height
        self.speedlimit = 7.5
        self.rotatespeed = 0.05
        self.maxspin = 1
        self.thrust = 0.1
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.deltavx = 0
        self.deltavy = 0
        self.speed = 0
        self.fxcenter = self.fycenter = 0.5
        
        AsteroidsGame.listenKeyEvent("keydown", "space", self.shoot)

        AsteroidsGame.listenKeyEvent("keydown", "right arrow", self.rotateRightOn)
        AsteroidsGame.listenKeyEvent("keyup", "right arrow", self.rotateRightOff)
        AsteroidsGame.listenKeyEvent("keydown", "left arrow", self.rotateLeftOn)
        AsteroidsGame.listenKeyEvent("keyup", "left arrow", self.rotateLeftOff)
        AsteroidsGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)

    def shoot(self, event):
        Bullet((self.x - 14 * math.sin(self.rotation), self.y - 15 * math.cos(self.rotation)), self.rotation)

    def rotateRightOn(self, event):
        self.vr = -self.rotatespeed
        
    def rotateRightOff(self, event):
        self.vr = 0
        
    def rotateLeftOn(self, event):
        self.vr = self.rotatespeed
        
    def rotateLeftOff(self, event):
        self.vr = 0
        
    def thrustOn(self, event):
        self.deltavx = -self.thrust * math.sin(self.rotation)
        self.deltavy = -self.thrust * math.cos(self.rotation)
        
        # Check speed limit
        if ((self.vx + self.deltavx)**2 + (self.vy + self.deltavy)**2)**0.5 < self.speedlimit:
            self.vx += self.deltavx
            self.vy += self.deltavy
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
class AsteroidsGame(App):
    def __init__(self):
        super().__init__()
        self.player1 = Ship((self.width / 2, self.height / 2), self.width, self.height)
        
    def step(self):
        self.player1.step()
        
        # Wrap screen for player
        if self.player1.x > self.width + 20:
            self.player1.x = -20
        elif self.player1.x < -20:
            self.player1.x = self.width + 20
        if self.player1.y > self.height + 20:
            self.player1.y = -20
        elif self.player1.y < -20:
            self.player1.y = self.height + 20
        
myapp = AsteroidsGame()
myapp.run()