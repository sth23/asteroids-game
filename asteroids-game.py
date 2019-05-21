from ggame import App, RectangleAsset, PolygonAsset, CircleAsset, LineAsset, ImageAsset, Frame, Sprite, LineStyle, Color
import math
import random

# Colors & lines
black = Color(0x000000, 1.0)
noline = LineStyle(0, black)
blackline = LineStyle(1, black)

class BigAsteroid(Sprite):
    def __init__(self, width, height):
        self.x1 = 30 + random.randint(-10,10)
        self.y1 = 0 + random.randint(-10,10)
        self.x2 = 60 + random.randint(-10,10)
        self.y2 = 0 + random.randint(-10,10)
        self.x3 = 90 + random.randint(-10,10)
        self.y3 = 30 + random.randint(-10,10)
        self.x4 = 90 + random.randint(-10,10)
        self.y4 = 60 + random.randint(-10,10)
        self.x5 = 60 + random.randint(-10,10)
        self.y5 = 90 + random.randint(-10,10)
        self.x6 = 30 + random.randint(-10,10)
        self.y6 = 90 + random.randint(-10,10)
        self.x7 = 0 + random.randint(-10,10)
        self.y7 = 60 + random.randint(-10,10)
        self.x8 = 0 + random.randint(-10,10)
        self.y8 = 30 + random.randint(-10,10)
        self.points = [(self.x1,self.y1), (self.x2,self.y2), (self.x3,self.y3), (self.x4,self.y4), (self.x5,self.y5), (self.x6,self.y6), (self.x7,self.y7), (self.x8,self.y8)]
        self.poly = PolygonAsset(self.points, noline, black)
        
        super().__init__(self.poly, (100,100))
        self.speed = 1
        self.rotation = 0
        self.vx = self.speed * math.sin(self.rotation)
        self.vy = self.speed * math.cos(self.rotation)
        self.vr = 0.025 * random.random()
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
    
#class MediumAsteroid(Sprite):
    
#class SmallAsteroid(Sprite):

class Bullet(Sprite):
    circ = CircleAsset(2, noline, black)
    
    def __init__(self, position, rotation):
        super().__init__(Bullet.circ, position)
        self.speed = 10
        self.rotation = rotation
        self.fxcenter = self.fycenter = 0
        self.vx = -self.speed * math.sin(self.rotation)
        self.vy = -self.speed * math.cos(self.rotation)
        
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
        Bullet((self.x - 15 * math.sin(self.rotation), self.y - 15 * math.cos(self.rotation)), self.rotation)

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
        
        BigAsteroid(self.width, self.height)
        
    def step(self):
        self.player1.step()
        
        for big in self.getSpritesbyClass(BigAsteroid):
            big.step()
        
        for bullet in self.getSpritesbyClass(Bullet):
            bullet.step()
            
            if bullet.x > self.width + 5 or bullet.x < -5:
                bullet.destroy()
            elif bullet.y > self.height + 5 or bullet.y < -5:
                bullet.destroy()
            else:
                for big in bullet.collidingWithSprites(BigAsteroid):
                    big.destroy()
                    bullet.destroy()
        
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