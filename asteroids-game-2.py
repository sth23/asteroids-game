from ggame import App, RectangleAsset, PolygonAsset, CircleAsset, LineAsset, ImageAsset, Frame, Sprite, LineStyle, Color
import math
import random

# Colors & lines
black = Color(0x000000, 1.0)
noline = LineStyle(0, black)
blackline = LineStyle(1, black)

class Asteroid(Sprite):
    def __init__(self, position, size):
        self.size = size
        self.xcoordinates = [30, 60, 90, 90, 60, 30, 0, 0]
        self.ycoordinates = [0, 0, 30, 60, 90, 90, 60, 30]
        self.range = 12
        self.radius = 45
        self.points = [None] * 8
        self.speed = 1
        if size == "big":
            self.xcoordinates = [x + random.randint(-self.range, self.range) for x in self.xcoordinates]
            self.ycoordinates = [y + random.randint(-self.range, self.range) for y in self.ycoordinates]
        elif size == "medium":
            self.speed = 2
            self.range = int(self.range / 2)
            self.radius = self.radius / 2
            self.xcoordinates = [x / 2 + random.randint(-self.range, self.range) for x in self.xcoordinates]
            self.ycoordinates = [y / 2 + random.randint(-self.range, self.range) for y in self.ycoordinates]
        else:
            self.speed = 3
            self.range = int(self.range / 2)
            self.radius = self.radius / 4
            self.xcoordinates = [x / 4 + random.randint(-self.range, self.range) for x in self.xcoordinates]
            self.ycoordinates = [y / 4 + random.randint(-self.range, self.range) for y in self.ycoordinates]
            
        for z in range(0,8):
            self.points[z] = (self.xcoordinates[z], self.ycoordinates[z])

        self.poly = PolygonAsset(self.points, noline, black)
        
        super().__init__(self.poly, position, CircleAsset(self.radius))
        

        self.rotation = random.random() * 2 * math.pi
        self.vx = self.speed * math.sin(self.rotation)
        self.vy = self.speed * math.cos(self.rotation)
        self.vr = 0.02 * random.random()
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
        
class ExtraLife(Sprite):
    ship = PolygonAsset([(0,10), (5,0), (10,10), (5,5)], noline, black)
    
    def __init__(self, position):
        super().__init__(ExtraLife.ship, position)

class Ship(Sprite):
    ship = PolygonAsset([(0,30), (15,0), (30,30), (15,15)], noline, black)
    
    def __init__(self, position, width, height):
        super().__init__(Ship.ship, position, CircleAsset(15))
        self.gamewidth = width
        self.gameheight = height
        self.speedlimit = 7.5
        self.rotatespeed = 0.1
        self.maxspin = 1
        self.thrust = 0.25
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.deltavx = 0
        self.deltavy = 0
        self.speed = 0
        self.fxcenter = self.fycenter = 0.5
        self.extralives = 3
        
        AsteroidsGame.listenKeyEvent("keydown", "space", self.shoot)

        AsteroidsGame.listenKeyEvent("keydown", "right arrow", self.rotateRightOn)
        AsteroidsGame.listenKeyEvent("keyup", "right arrow", self.rotateRightOff)
        AsteroidsGame.listenKeyEvent("keydown", "left arrow", self.rotateLeftOn)
        AsteroidsGame.listenKeyEvent("keyup", "left arrow", self.rotateLeftOff)
        AsteroidsGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)

    def shoot(self, event):
        if self.extralives >= 0:
            Bullet((self.x - 15 * math.sin(self.rotation), self.y - 15 * math.cos(self.rotation)), self.rotation)

    def rotateRightOn(self, event):
        if self.extralives >= 0:
            self.vr = -self.rotatespeed
        
    def rotateRightOff(self, event):
        if self.extralives >= 0:
            self.vr = 0
        
    def rotateLeftOn(self, event):
        if self.extralives >= 0:
            self.vr = self.rotatespeed
        
    def rotateLeftOff(self, event):
        if self.extralives >= 0:
            self.vr = 0
        
    def thrustOn(self, event):
        if self.extralives >= 0:
            self.deltavx = -self.thrust * math.sin(self.rotation)
            self.deltavy = -self.thrust * math.cos(self.rotation)
        
            # Check speed limit
            if ((self.vx + self.deltavx)**2 + (self.vy + self.deltavy)**2)**0.5 < self.speedlimit:
                self.vx += self.deltavx
                self.vy += self.deltavy
        
    def step(self):
        if self.extralives >= 0:
            self.x += self.vx
            self.y += self.vy
            self.rotation += self.vr
            
class shipPiece(Sprite):
    tri = PolygonAsset([(7.5,0), (15,0), (0,15)], noline, black)
    
    def __init__(self, position, vx, vy):
        super().__init__(shipPiece.tri, position)
        self.vx = vx * random.random()
        self.vy = vy * random.random()
        self.vr = random.random() * 0.25
        self.rotation = 2 * math.pi * random.random()
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
class AsteroidsGame(App):
    def __init__(self):
        super().__init__()
        self.player1 = Ship((self.width / 2, self.height / 2), self.width, self.height)
        self.showExtraLives()
        
        self.hit = []
        
        self.count = 0
        self.randx = 0
        self.randy = 0
        self.random = 0
        self.score = 0
        print("Score: " + str(self.score))
        
    def showExtraLives(self):
        for x in self.getSpritesbyClass(ExtraLife):
            x.destroy()
        for x in range(0,self.player1.extralives):
            ExtraLife((10 + x * 15, self.height - 20))
            
    def destroyShip(self):

        
    def resetScreen(self):
        [asteroid.destroy() for asteroid in self.getSpritesbyClass(Asteroid)]

        self.player1.x = self.width / 2
        self.player1.y = self.height / 2
        self.player1.vx = 0
        self.player1.vy = 0
        self.player1.rotation = 0
        self.player1.extralives -= 1
        self.showExtraLives()
        self.count = 0
        if self.player1.extralives < 0:
            print("Game Over")
        
    def step(self):
        # Randomly create big asteroids that drift onto screen
        if self.count % 1000 == 0:
            self.random = random.randint(0,3)
            if self.random == 0:
                Asteroid((random.randint(0, self.width), -45), "big")
            elif self.random == 1:
                Asteroid((self.width + 45, random.randint(0, self.height)), "big")
            elif self.random == 2:
                Asteroid((random.randint(0, self.width), self.height + 45), "big")
            else:
                Asteroid((-45, random.randint(0, self.height)), "big")
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
                
            if ship.collidingWithSprites(Asteroid):
                if self.player1.extralives >= 0:
                    self.resetScreen()
                else:
                    self.player1.destroy()
        
        for asteroid in self.getSpritesbyClass(Asteroid):
            asteroid.step()
            # Wrap screen for big asteroids
            if asteroid.x > self.width + asteroid.radius:
                asteroid.x = -asteroid.radius
            elif asteroid.x < -asteroid.radius:
                asteroid.x = self.width + asteroid.radius
            if asteroid.y > self.height + asteroid.radius:
                asteroid.y = -asteroid.radius
            elif asteroid.y < -asteroid.radius:
                asteroid.y = self.height + asteroid.radius
            
        for bullet in self.getSpritesbyClass(Bullet):
            bullet.step()
            
            if bullet.x > self.width + 50 or bullet.x < -50:
                bullet.destroy()
            elif bullet.y > self.height + 50 or bullet.y < -50:
                bullet.destroy()
            else:
                self.hit = bullet.collidingWithSprites(Asteroid)
                if self.hit:
                    for asteroid in self.hit:
                        if asteroid.size == "big":
                            Asteroid((asteroid.x + math.sin(asteroid.rotation) * asteroid.radius / 2, asteroid.y + math.cos(asteroid.rotation) * asteroid.radius / 2), "medium")
                            Asteroid((asteroid.x - math.sin(asteroid.rotation) * asteroid.radius / 2, asteroid.y + math.cos(asteroid.rotation) * asteroid.radius / 2), "medium")
                            Asteroid((asteroid.x + math.sin(asteroid.rotation) * asteroid.radius / 2, asteroid.y - math.cos(asteroid.rotation) * asteroid.radius / 2), "medium")
                            Asteroid((asteroid.x - math.sin(asteroid.rotation) * asteroid.radius / 2, asteroid.y - math.cos(asteroid.rotation) * asteroid.radius / 2), "medium")
                            self.score += 10
                            asteroid.destroy()
                        elif asteroid.size == "medium":
                            Asteroid((asteroid.x + math.sin(asteroid.rotation) * asteroid.radius / 2, asteroid.y + math.cos(asteroid.rotation) * asteroid.radius / 2), "small")
                            Asteroid((asteroid.x - math.sin(asteroid.rotation) * asteroid.radius / 2, asteroid.y + math.cos(asteroid.rotation) * asteroid.radius / 2), "small")
                            Asteroid((asteroid.x + math.sin(asteroid.rotation) * asteroid.radius / 2, asteroid.y - math.cos(asteroid.rotation) * asteroid.radius / 2), "small")
                            Asteroid((asteroid.x - math.sin(asteroid.rotation) * asteroid.radius / 2, asteroid.y - math.cos(asteroid.rotation) * asteroid.radius / 2), "small")
                            self.score += 20
                            asteroid.destroy()
                        elif asteroid.size == "small":
                            self.score += 30
                            asteroid.destroy()
                    bullet.destroy()
        
myapp = AsteroidsGame()
myapp.run()
