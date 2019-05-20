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
    circ = RectangleAsset(1, noline, black)
    
    def __init__(self, position, rotation):
        super().__init__(Bullet.circ, rotation)
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
        self.rotatespeed = 0.05
        self.speedlimit = 10
        self.thrust = 1
        self.vx = 0
        self.vy = 0
        self.vr = 0
        
        print(self.rotation)
        
        SpaceInvadersGame.listenKeyEvent("keydown", "space", self.shoot)

        AsteroidsGame.listenKeyEvent("keydown", "right arrow", self.rotateRightOn)
        AsteroidsGame.listenKeyEvent("keyup", "right arrow", self.rotateRightOff)
        AsteroidsGame.listenKeyEvent("keydown", "left arrow", self.rotateLeftOn)
        AsteroidsGame.listenKeyEvent("keyup", "left arrow", self.rotateLeftOff)
        AsteroidsGame.listenKeyEvent("keydown", "up arrow", self.thurstOn)
        AsteroidsGame.listenKeyEvent("keyup"), "up arrow", self.thrustOff)
        

    def shoot(self, event):
        Bullet((self.x + 15, self.y - 15))

    def rotateRightOn(self, event):
        self.vr = self.rotatespeed
        
    def rotateRightOff(self, event):
        self.vr = 0
        
    def rotateLeftOn(self, event):
        self.vr = -self.rotatespeed
        
    def moveLeftOff(self, event):
        self.vr = 0
        
    def thrustOn(self, event):
        self.vx = self.thrust
        self.vy = self.thrust
        
    def thurstOff(self, event):
        self.vx = 0
        self.vy = 0

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
class AsteroidsGame(App):
    def __init__(self):
        super().__init__()
        self.player1 = Ship((self.width / 2, self.height / 2))
        
    def step(self):
        self.player1.step()
        
myapp = AsteroidsGame()
myapp.run()