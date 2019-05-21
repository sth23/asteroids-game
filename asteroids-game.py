from ggame import App, RectangleAsset, PolygonAsset, CircleAsset, LineAsset, ImageAsset, Frame, Sprite, LineStyle, Color
import math
import random

# Colors & lines
black = Color(0x000000, 1.0)
noline = LineStyle(0, black)
blackline = LineStyle(1, black)

class BigAsteroid(Sprite):
    def __init__(self, position):
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
        
        super().__init__(self.poly, position, CircleAsset(45))
        self.speed = 1
        self.rotation = random.random() * 2 * math.pi
        self.vx = self.speed * math.sin(self.rotation)
        self.vy = self.speed * math.cos(self.rotation)
        self.vr = 0.02 * random.random()
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
    
class MediumAsteroid(Sprite):
    def __init__(self, position):
        self.x1 = 15 + random.randint(-5,5)
        self.y1 = 0 + random.randint(-5,5)
        self.x2 = 30 + random.randint(-5,5)
        self.y2 = 0 + random.randint(-5,5)
        self.x3 = 45 + random.randint(-5,5)
        self.y3 = 15 + random.randint(-5,5)
        self.x4 = 45 + random.randint(-5,5)
        self.y4 = 30 + random.randint(-5,5)
        self.x5 = 30 + random.randint(-5,5)
        self.y5 = 45 + random.randint(-5,5)
        self.x6 = 15 + random.randint(-5,5)
        self.y6 = 45 + random.randint(-5,5)
        self.x7 = 0 + random.randint(-5,5)
        self.y7 = 30 + random.randint(-5,5)
        self.x8 = 0 + random.randint(-5,5)
        self.y8 = 15 + random.randint(-5,5)
        self.points = [(self.x1,self.y1), (self.x2,self.y2), (self.x3,self.y3), (self.x4,self.y4), (self.x5,self.y5), (self.x6,self.y6), (self.x7,self.y7), (self.x8,self.y8)]
        self.poly = PolygonAsset(self.points, noline, black)
        
        super().__init__(self.poly, position, CircleAsset(22.5))
        
        self.speed = 2
        self.rotation = random.random() * 2 * math.pi
        self.vx = self.speed * math.sin(self.rotation)
        self.vy = self.speed * math.cos(self.rotation)
        self.vr = 0.03 * random.random()
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
    
class SmallAsteroid(Sprite):
    def __init__(self, position):
        self.x1 = 7.5 + random.randint(-3,3)
        self.y1 = 0 + random.randint(-3,3)
        self.x2 = 15 + random.randint(-3,3)
        self.y2 = 0 + random.randint(-3,3)
        self.x3 = 22.5 + random.randint(-3,3)
        self.y3 = 7.5 + random.randint(-3,3)
        self.x4 = 22.5 + random.randint(-3,3)
        self.y4 = 15 + random.randint(-3,3)
        self.x5 = 15 + random.randint(-3,3)
        self.y5 = 22.5 + random.randint(-3,3)
        self.x6 = 7.5 + random.randint(-3,3)
        self.y6 = 22.5 + random.randint(-3,3)
        self.x7 = 0 + random.randint(-3,3)
        self.y7 = 15 + random.randint(-3,3)
        self.x8 = 0 + random.randint(-3,3)
        self.y8 = 7.5 + random.randint(-3,3)
        self.points = [(self.x1,self.y1), (self.x2,self.y2), (self.x3,self.y3), (self.x4,self.y4), (self.x5,self.y5), (self.x6,self.y6), (self.x7,self.y7), (self.x8,self.y8)]
        self.poly = PolygonAsset(self.points, noline, black)
        
        super().__init__(self.poly, position, CircleAsset(11.25))
        
        self.speed = 3
        self.rotation = random.random() * 2 * math.pi
        self.vx = self.speed * math.sin(self.rotation)
        self.vy = self.speed * math.cos(self.rotation)
        self.vr = 0.04 * random.random()
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr

class Bullet(Sprite):
    circ = CircleAsset(2, noline, black)
    
    def __init__(self, position, rotation):
        super().__init__(Bullet.circ, position, CircleAsset(5))
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
        super().__init__(Ship.ship, position, CircleAsset(15))
        self.gamewidth = width
        self.gameheight = height
        self.speedlimit = 7.5
        self.rotatespeed = 0.15
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
        Ship((self.width / 2, self.height / 2), self.width, self.height)
        
        self.bithit = []
        self.mediumhit = []
        self.smallhit = []
        
        self.count = 0
        self.randx = 0
        self.randy = 0
        self.random = 0
        self.score = 0
        self.extralives = 3
        print("Score: " + str(self.score))
        
    def resetScreen(self):
        [big.destroy() for big in self.getSpritesbyClass(BigAsteroid)]
        [medium.destroy() for medium in self.getSpritesbyClass(MediumAsteroid)]
        [small.destroy() for small in self.getSpritesbyClass(SmallAsteroid)]
        Ship((self.width / 2, self.height / 2), self.width, self.height)
        self.count = 0
        
    def step(self):
        # Randomly create big asteroids that drift onto screen
        if self.count % 1000 == 0:
            self.random = random.randint(0,3)
            if self.random == 0:
                BigAsteroid((random.randint(0, self.width), -45))
            elif self.random == 1:
                BigAsteroid((self.width + 45, random.randint(0, self.height)))
            elif self.random == 2:
                BigAsteroid((random.randint(0, self.width), self.height + 45))
            else:
                BigAsteroid((-45, random.randint(0, self.height)))
        self.count += 1
        
        for ship in self.getSpritesbyClass(Ship):
            ship.step()
            # Wrap screen for player
            if ship.x > self.width + 20:
                ship.x = -20
            elif ship.x < -20:
                ship.x = self.width + 20
            if ship.y > self.height + 20:
                ship.y = -20
            elif ship.y < -20:
                ship.y = self.height + 20
                
            if ship.collidingWithSprites(BigAsteroid):
                ship.destroy()
                self.resetScreen()
            elif ship.collidingWithSprites(MediumAsteroid):
                ship.destroy()
                self.resetScreen()
            elif ship.collidingWithSprites(SmallAsteroid):
                ship.destroy()
                self.resetScreen()
        
        for big in self.getSpritesbyClass(BigAsteroid):
            big.step()
            # Wrap screen for big asteroids
            if big.x > self.width + 90:
                big.x = -90
            elif big.x < -90:
                big.x = self.width + 90
            if big.y > self.height + 90:
                big.y = -90
            elif big.y < -90:
                big.y = self.height + 90
            
        for medium in self.getSpritesbyClass(MediumAsteroid):
            medium.step()
            # Wrap screen for medium asteroids
            if medium.x > self.width + 45:
                medium.x = -45
            elif medium.x < -45:
                medium.x = self.width + 45
            if medium.y > self.height + 45:
                medium.y = -45
            elif medium.y < -45:
                medium.y = self.height + 45
                
        for small in self.getSpritesbyClass(SmallAsteroid):
            small.step()
            # Wrap screen for small asteroids
            if small.x > self.width + 22.5:
                small.x = -22.5
            elif small.x < -22.5:
                small.x = self.width + 22.5
            if small.y > self.height + 22.5:
                small.y = -22.5
            elif small.y < -22.5:
                small.y = self.height + 22.5
            
        for bullet in self.getSpritesbyClass(Bullet):
            bullet.step()
            
            if bullet.x > self.width + 50 or bullet.x < -50:
                bullet.destroy()
            elif bullet.y > self.height + 50 or bullet.y < -50:
                bullet.destroy()
            else:
                self.bighit = bullet.collidingWithSprites(BigAsteroid)
                self.mediumhit = bullet.collidingWithSprites(MediumAsteroid)
                self.smallhit = bullet.collidingWithSprites(SmallAsteroid)
                if self.bighit:
                    for big in self.bighit:
                        MediumAsteroid((big.x + math.sin(big.rotation)*90/4, big.y + math.cos(big.rotation)*90/4))
                        MediumAsteroid((big.x - math.sin(big.rotation)*90/4, big.y + math.cos(big.rotation)*90/4))
                        MediumAsteroid((big.x + math.sin(big.rotation)*90/4, big.y - math.cos(big.rotation)*90/4))
                        MediumAsteroid((big.x - math.sin(big.rotation)*90/4, big.y - math.cos(big.rotation)*90/4))
                        self.score += 10
                        print("Score: " + str(self.score))
                        big.destroy()
                    bullet.destroy()
                elif self.mediumhit:
                    for medium in self.mediumhit:
                        SmallAsteroid((medium.x + math.sin(medium.rotation)*90/8, medium.y + math.cos(medium.rotation)*90/8))
                        SmallAsteroid((medium.x - math.sin(medium.rotation)*90/8, medium.y + math.cos(medium.rotation)*90/8))
                        SmallAsteroid((medium.x + math.sin(medium.rotation)*90/8, medium.y - math.cos(medium.rotation)*90/8))
                        SmallAsteroid((medium.x - math.sin(medium.rotation)*90/8, medium.y - math.cos(medium.rotation)*90/8))
                        self.score += 20
                        print("Score: " + str(self.score))
                        medium.destroy()
                    bullet.destroy()
                elif self.smallhit:
                    for small in bullet.collidingWithSprites(SmallAsteroid):
                        self.score += 30
                        print("Score: " + str(self.score))
                        small.destroy()
                    bullet.destroy()
        
myapp = AsteroidsGame()
myapp.run()