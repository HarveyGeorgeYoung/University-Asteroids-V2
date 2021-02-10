import pygame, math, random

#globalvariables
score = 0
lives = 3  #Score and lives used in reaction to colliding objects
current_achievement = ""
pygame.init()
swidth = 600
sheight = 400  #Screen size definitions, used throughout

#colourrange
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)  #Used for if we need to use colours with ease
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (170, 170, 170)
#loading all required images and transforming if needed
alienshipimg = pygame.image.load('Images/alienShip.png')
satalliteimg = pygame.image.load('Images/satellite.png')
asteroidsmall = pygame.image.load('Images/asteroidsmall.png')
asteroidmedium = pygame.image.load('Images/asteroidmedium.png')
asteroidlarge = pygame.image.load('Images/asteroidlarge.png')
ship = pygame.image.load('Images/ship.png')
ship = pygame.transform.scale(ship, (50, 50))
level1 = pygame.image.load('Images/bg.jpg')
level2 = pygame.image.load('Images/bg2.jfif')
level2 = pygame.transform.scale(level2, (600, 400))
level3 = pygame.image.load('Images/bg3.png')
go = pygame.image.load('Images/gameover.png')
laser = pygame.image.load('Images/laser.png')
laser = pygame.transform.scale(laser, (10, 10))  #Rotating and resizing
laser = pygame.transform.rotate(laser, 90)
dpoints = pygame.image.load('Images/dpoints.png')
fpoints = pygame.image.load('Images/50points.png')
oneup = pygame.image.load('Images/1up.png')
#loading text
smallfont = pygame.font.SysFont('Arial', 20)
quit = smallfont.render('Quit Game', 1, WHITE)
menu = smallfont.render('Main Menu', 1, WHITE)
l1 = smallfont.render('Level 1', 1, WHITE)
l2 = smallfont.render('Level 2', 1, WHITE)
l3 = smallfont.render('Level 3', 1, WHITE)
pygame.display.set_caption('Asteroids')
#setting display parameters
window = pygame.display.set_mode((swidth, sheight))
clock = pygame.time.Clock()
puChoice = random.randint(1, 3)
gameover = False

level2state = False
level3state = False


def update():

    if score <= 19:
        window.blit(level1, (0, 0))  #Drawing inital background
        window.blit(l1, (swidth - l1.get_width() - 260, 35))
    if level2state:
        window.blit(level2, (0, 0))  #second level background
        window.blit(l2, (swidth - l2.get_width() - 260, 35))
    if level3state:
        window.blit(level3, (0, 0))  #third level background
        window.blit(l3, (swidth - l3.get_width() - 260, 35))

    font = pygame.font.SysFont('arial', 20)
    for e in alienships:
        e.draw(window)  #Drawing/updating satallite
    for s in satallites:
        s.draw(window)  #Drawing/updating alienship
    for a in asteroids:
        a.draw(window)  #Drawing/updating asteroids
    for b in playerProjectiles:
        b.drawProjectile(window)
    ship.physicsComponent()
    ship.graphicsComponent()

    if score == 11 or score == 21 or score == 35 or score == 45 or score == 65 or score == 95:
        if puChoice == 1: doubleSpawner.prototype_.clone(window)
        elif puChoice == 2: PointsSpawner.prototype_.clone(window)
        elif puChoice == 3: lifeSpawner.prototype_.clone(window)
    displayLives = font.render(
        "Lives: " + str(lives), 1,
        RED)  #Lives display - stored here so that it can update
    displayScore = font.render(
        "Score: " + str(score), 1,
        RED)  #Score display - stored here so that it can update
    window.blit(displayScore,
                (swidth - displayScore.get_width() - 50, 35))  #Top right
    window.blit(displayLives, (50, 35))  #Top left

    if (current_achievement):  #display achievment if one is earned
        font = pygame.font.SysFont('arial', 15)
        displayAchievement = font.render(
            "Achievement Unlocked - " + str(current_achievement), 0, WHITE)
        window.blit(displayAchievement, (60, 350))
    if gameover:
        while True:
            if score <= 19:
                window.blit(level1,
                            (0, 0))  #Drawing background of the level reached
            if level2state:
                window.blit(level2, (0, 0))
            if level3state:
                window.blit(level3, (0, 0))

            window.blit(go, (50, 110))  #game over display
            window.blit(displayScore,
                        (swidth - displayScore.get_width() - 250, 325))
            #same as the main menu
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if swidth / 2 <= mouse[
                            0] <= swidth / 2 + 140 and sheight / 2 <= mouse[
                                1] <= sheight / 2 + 40:
                        pygame.quit()
                    if swidth / 2 <= mouse[
                            0] <= swidth / 2 + 140 and sheight / 3 <= mouse[
                                1] <= sheight / 3 + 40:
                        import main
                        main

            if swidth / 2 <= mouse[
                    0] <= swidth / 2 + 140 and sheight / 3 <= mouse[
                        1] <= sheight / 3 + 40:
                pygame.draw.rect(window, GRAY,
                                 [swidth / 2.5, sheight / 3, 140, 40])

            else:
                pygame.draw.rect(window, BLACK,
                                 [swidth / 2.5, sheight / 3, 140, 40])

            if swidth / 2 <= mouse[
                    0] <= swidth / 2 + 140 and sheight / 2 <= mouse[
                        1] <= sheight / 2 + 40:
                pygame.draw.rect(window, GRAY,
                                 [swidth / 2.5, sheight / 2, 140, 40])

            else:
                pygame.draw.rect(window, BLACK,[swidth / 2.5, sheight / 2, 140, 40])
            window.blit(quit, (swidth / 2.5 + 20, sheight / 2 + 10))
            window.blit(menu, (swidth / 2.5 + 20, sheight / 3 + 10))
            pygame.display.update()

    pygame.display.update(
    )  #Updating the window - must be after every other object has been drawn/updated


class KeyCheck:         #ship key check
    def keyPress(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            ship.x -= 5  #constant x direction when key is pressed

        if keys[pygame.K_d]:
            ship.x += 5  #constant x direction when key is pressed

        if keys[pygame.K_w]:
            #self.xvel = self.direction[0] * 10
            #self.yvel = -self.direction[1] * 10
            #self.x += self.xvel                uncomment this to activate
            #self.y -= self.yvel                directional forward
            
            ship.y -= 5  #constant y direction when key is pressed

        if keys[pygame.K_s]:
            ship.y += 5  #constant y direction when key is pressed

        if keys[pygame.
                K_LEFT]:  #changes the ships direction by 5 degrees to the left
            ship.angle += 5
            ship.direction[0] = math.sin(-math.radians(ship.angle))
            ship.direction[1] = -math.cos(math.radians(ship.angle))

        if keys[pygame.
                K_RIGHT]:  #changes the ships direction by 5 degrees to the right
            ship.angle -= 5
            ship.direction[0] = math.sin(-math.radians(ship.angle))
            ship.direction[1] = -math.cos(math.radians(ship.angle))


class boundaryCheck: #ship infinte screen
    def InfinteScreen(self):
        if ship.x > swidth + 50:  #This code makes the screen infinte
            ship.x = 0
        if ship.x < 0 - 50:  #Once the size of the ship(50) goes out of bounds at
            ship.x = swidth
        if ship.y < -50:  #either x value or y value it spawns it in again
            ship.y = sheight
        if ship.y > sheight + 50:  #at the opposite size.
            ship.y = 0


class DrawShip: #draw ship update
    def updateShip(self, surface):
        orig_rect = ship.image.get_rect()
        rotateimage = pygame.transform.rotate(ship.image, ship.angle)
        rot_rect = orig_rect.copy()
        ship.center = rotateimage.get_rect().center
        rot_rect.center = rotateimage.get_rect().center
        rotateimage = rotateimage.subsurface(rot_rect).copy()

        surface.blit(rotateimage, (ship.x, ship.y))

class Ship(object):
    def __init__(self):
        self.image = ship
        self.firex = 0
        self.firey = 0
        self.x = 100
        self.y = 100
        self.width = self.image.get_width()  #defining variables for the ship object
        self.height = self.image.get_height()
        self.direction = [0, 0]
        self.angle = 0
        self.direction[0] = math.sin(-math.radians(self.angle))
        self.direction[1] = -math.cos(math.radians(self.angle))
        self.keyCheck = KeyCheck()
        self.infinteScreen = boundaryCheck()
        self.drawShip = DrawShip()

    def physicsComponent(self):
        self.keyCheck.keyPress()
        self.infinteScreen.InfinteScreen()

    def graphicsComponent(self):
        self.drawShip.updateShip(window)


class projectile(object):
    def __init__(self):
        self.point = (ship.x + 25), (
            ship.y + 25
        )  #Setting where it comes from(middle of the ship as we do not have a head point of the ship assinged)
        self.x, self.y = self.point
        self.width = 7  #Size of the projectile
        self.height = 7
        self.direction = ship.direction
        self.direction[0] = math.sin(-math.radians(ship.angle))  #Different angle caluclations to the ship instead we do not minus the cos and that flips it from being upside down
        self.direction[1] = math.cos(math.radians(ship.angle))
        self.xvel = self.direction[
            0] * 10  #Sets the velocity for each direction based on the angle of the ship
        self.yvel = self.direction[1] * 10

    def updateProjectile(self):
        self.x += self.xvel  #When moving this is what keeps it moving that direction in the velocity.
        self.y -= self.yvel

    def drawProjectile(self, window):
        pygame.draw.rect(window, RED,
                         [self.x, self.y, self.width, self.height])
        #drawing the RED(defined in the colour range at the top) projectile with the given parameters calculated prior

    def checkBoundaries(self):
        if self.x < -20 or self.x > swidth or self.y > sheight or self.y < -20:
            return True  #Removes projectile once 20 pixels outside of the screen or screen height/width


#Asteroid Class
class Asteroid(object):
    def __init__(self, size):

        self.size = size  #This is defined by the random choice when init below
        if self.size == 1:
            self.image = asteroidsmall
        elif self.size == 2:
            self.image = asteroidmedium
        elif self.size == 3:
            self.image = asteroidlarge  ## Different sizes of asteroids defined earlier

        self.width = 50 * size  #each image size is 50,100,150 so it would be 3,2,1 * 50 which equals the size of the img
        self.height = 50 * size
        self.ranPoint = random.choice([(random.randrange(0, swidth - self.width),random.choice([-1 * self.height - 5, sheight + 5])),(random.choice([-1 * self.width - 5, swidth + 5]),random.randrange(0, sheight - self.height))])  #Only spawning just outside the required window size on each side. nowhere else
        self.x, self.y = self.ranPoint
        if self.x < swidth // 2:  #if spawned on left side of window
            self.xdir = 1  #go right
        else:  #if spawned on right
            self.xdir = -1  #go left
        if self.y < sheight // 2:  #if spawned on bottom of window
            self.ydir = 1  #go up
        else:  #if spawned on top of window
            self.ydir = -1  #go down
        self.xvel = self.xdir * random.randrange(1, 2)
        self.yvel = self.ydir * random.randrange(
            1, 2)  #random speed of each direction

    def draw(self, window):
        window.blit(
            self.image,
            (self.x, self.y
             ))  #defining draw statment and where the locaiton of it spawns

#AlienShip Class
class AlienShip(object):
    def __init__(self):

        self.image = alienshipimg

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.ranPoint = random.choice([(random.randrange(0, swidth - self.width),random.choice([-1 * self.height - 5, sheight + 5])),(random.choice([-1 * self.width - 5, swidth + 5]),random.randrange(0, sheight - self.height))])  #Only spawning just outside the required window size on each side. nowhere else
        self.x, self.y = self.ranPoint
        if self.x < swidth // 2:  #if spawned on left side of window
            self.xdir = 1  #go right
        else:  #if spawned on right
            self.xdir = -1  #go left
        if self.y < sheight // 2:  #if spawned on bottom of window
            self.ydir = 1  #go up
        else:  #if spawned on top of window
            self.ydir = -1  #go down
        self.xvel = self.xdir * random.randrange(1, 2)
        self.yvel = self.ydir * random.randrange(
            1, 2)  #random speed of each direction

    def draw(self, window):
        window.blit(
            self.image,
            (self.x, self.y
             ))  #defining draw statment and where the locaiton of it spawns

#Satallite Class
class Satallite(object):
    def __init__(self):

        self.image = satalliteimg

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.ranPoint = random.choice([(random.randrange(0, swidth - self.width),random.choice([-1 * self.height - 5, sheight + 5])),(random.choice([-1 * self.width - 5, swidth + 5]),random.randrange(0, sheight - self.height))])  #Only spawning just outside the required window size on each side. nowhere else
        self.x, self.y = self.ranPoint
        if self.x < swidth // 2:  #if spawned on left side of window
            self.xdir = 1  #go right
        else:  #if spawned on right
            self.xdir = -1  #go left
        if self.y < sheight // 2:  #if spawned on bottom of window
            self.ydir = 1  #go up
        else:  #if spawned on top of window
            self.ydir = -1  #go down
        self.xvel = self.xdir * random.randrange(1, 2)
        self.yvel = self.ydir * random.randrange(
            1, 2)  #random speed of each direction

    def draw(self, window):
        window.blit(
            self.image,
            (self.x, self.y
             ))  #defining draw statment and where the locaiton of it spawns

#prototype
class powerUp:
    def __init__(self):
        self.x = 0
        self.y = 0
        pass

    def clone(self):
        pass


class doublePoints(powerUp):
    def __init__(self):
        self.x = random.randint(0, 550)
        self.y = random.randint(0, 350)
        self.image = dpoints
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def clone(self, surface):
        surface.blit(self.image, (self.x, self.y))


class fiftyPoints(powerUp):
    def __init__(self):
        self.x = random.randint(0, 550)
        self.y = random.randint(0, 350)
        self.image = fpoints
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def clone(self, surface):
        surface.blit(self.image, (self.x, self.y))


class addLife(powerUp):
    def __init__(self):
        self.x = random.randint(0, 550)
        self.y = random.randint(0, 350)
        self.image = oneup
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def clone(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Spawner:
    def __init__(self, prototype):
        self.x = 0
        self.y = 0
        self.prototype_ = prototype

    def spawnPowerUp(self):
        return self.prototype_.clone()


#Achievement classes
class Observer():
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observables = {}

    def observe(self, event, func_name):
        self._observables[event] = func_name

class Event():
    def __init__(self, event, data, data2):
        #creates an instance of the event and data
        self.event = event
        self.data = data
        self.data2 = data2
        self.watch()#calls watch func

    def watch(self):
      #checks to see if event in being observed already and then calls the related function
        for observer in Observer._observers:
            if self.event in observer._observables:
                observer._observables[self.event](self.data, self.data2)


class Achievements(Observer):
    def __init__(self):
        Observer.__init__(self)

    def points(self, points, lives):
        message = ""
        rank = ""
        global current_achievement
        add_achievement = 0
        if (lives == 3):
            rank = "Hero: "
        elif (lives == 2):
            rank = "Master: "
        else:
            rank = "Novice: "
        if (int(points) >= 20 and int(points) < 40):
            message = "Reach 20 points"
        elif (int(points) >= 40 and int(points) < 60):
            message = "Reach 40 points"
        elif (int(points) >= 60 and int(points) < 80):
            message = "Reach 60 points"
        elif (int(points) >= 80):
            message = "Reach 80 points"
        if (message):
            for i in achievements_unlocked:
                if i == message:
                    add_achievement += 1
            if add_achievement == 0:
                print(message)
                achievements_unlocked.append(message)
                current_achievement = rank + message
                return current_achievement

    def lives(self, points, lives):
        message = ""#achivement message
        global current_achievement
        add_achievement = 0
        if (int(points) < 50):
            if (int(lives) == 2):
                message = "Messed up: Lose a life"
            elif (int(lives) == 1):
                message = "Last Chance: One life left"
        else:
            if (int(lives) == 2):
                message = "Training pays off"
            elif (int(lives) == 1):
                message = "My last stance"
        if (message):
          #checks to see if achievement is in the achievement array and if not then message is displayed to screen 
            for i in achievements_unlocked:
                if i == message:
                    add_achievement += 1
            if add_achievement == 0:
                achievements_unlocked.append(message)
                current_achievement = message
                return current_achievement


# Create initial object instances
achievements_unlocked = []
achievement = Achievements()
achievement.observe('points', achievement.points)
achievement.observe('lives', achievement.lives)

satallites = []
alienships = []
doubleSpawner = Spawner(doublePoints())
PointsSpawner = Spawner(fiftyPoints())
lifeSpawner = Spawner(addLife())
ship = Ship()
playerProjectiles = []  #definding the projectile list to add when space is pressed
asteroids = []  #defining the list
count = 0  #used for asteroid spawning times
running = True
while running:
    clock.tick(60)  #Ignore this, doesn't affect the program right now
    count += 1
    if not gameover:
        for b in playerProjectiles:
            b.updateProjectile()
            if b.checkBoundaries():
                playerProjectiles.pop(playerProjectiles.index(b))  #Check if bullet has gone out of the screen and destroy

        if count % 50 == 0:
            ran = random.choice([1, 1, 1, 2, 2, 3])  #Chances of each asteroid small:medium:large = 3:2:1
            asteroids.append(Asteroid(ran))  #change the size value of asteroid given the value just recieved
        if count % 800 == 0:
            satallites.append(Satallite())
        if count % 1500 == 0:
            alienships.append(AlienShip())
        for a in asteroids:
            a.x += a.xvel  #THIS IS WHAT MAKES THE ASTEROIDS MOVE
            a.y += a.yvel  #spawned

            # bullet collision
            for b in playerProjectiles:
                if (b.x >= a.x and b.x <= a.x + a.width) or b.x + b.width >= a.x and b.x + b.width <= a.x + a.width:  #Seeing if the two objects from the list cross over each others center point + width of themselves
                    if (b.y >= a.y and b.y <= a.y + a.height) or b.y + b.height >= a.y and b.y + b.height <= a.y + a.height:
                        if a.size == 3:
                            newAsteroid = Asteroid(2)  #Creates two new asteroids
                            newAsteroid1 = Asteroid(2)
                            newAsteroid.x = a.x  #Assigns them the x values of the asteroid that was shot
                            newAsteroid1.x = a.x
                            newAsteroid.y = a.y  #Assigns them the y values of the asteroid that was shot
                            newAsteroid1.y = a.y
                            asteroids.append(newAsteroid)  #Creates two new asteroids given the variables above
                            asteroids.append(newAsteroid1)
                            score += 1  #Score plus 1 for shooting big asteroid
                            Event('points', score, lives)
                        if a.size == 2:
                            newAsteroid = Asteroid(1)
                            newAsteroid1 = Asteroid(1)  #Creates two new asteroids
                            newAsteroid.x = a.x
                            newAsteroid1.x = a.x  #Assigns them the x values of the asteroid that was shot
                            newAsteroid.y = a.y
                            newAsteroid1.y = a.y  #Assigns them the y values of the asteroid that was shot
                            asteroids.append(newAsteroid)
                            asteroids.append(newAsteroid1)  #Creates two new asteroids given the variables above
                            score += 2  #Score plus 2 for shooting medium asteroid
                            Event('points', score, lives)
                        if a.size == 1:
                            score += 3  #Score plus 3 for shooting little asteroid
                            Event('points', score, lives)
                        asteroids.pop(asteroids.index(a))  #pops the original asteorid that was hit
                        playerProjectiles.pop(playerProjectiles.index(b))  #destroys the bullet taht destroyed the asteroid
                        print(score)  #Prints score in the console for testing

            if (a.x >= ship.x - ship.width // 2 and a.x <= ship.x + ship.width // 2) or (a.x + a.width <= ship.x + ship.width // 2 and a.x + a.width >= ship.x - ship.width // 2):  #Seeing if the two objects from the list cross over each others center point + width of themselves
                if (a.y >= ship.y - ship.height // 2 and a.y <= ship.y + ship.height // 2) or (a.y + a.height >= ship.y - ship.height // 2 and a.y + a.height <= ship.y + ship.height // 2):
                    lives -= 1  #Removes one life and then
                    Event('lives', score, lives)
                    asteroids.pop(asteroids.index(a))  #pops the asteroid that hit the ship
                    print(lives)  #prints lives in the console to test
            

        for s in satallites:
            s.x += s.xvel
            s.y += s.yvel
            if s.x < -100 - s.width or s.x > swidth + 100 or s.y > sheight + 100 or s.y < -100 - s.height:
                satallites.pop(satallites.index(s))
                break
            for b in playerProjectiles:
                if (b.x >= s.x and b.x <= s.x + s.width) or b.x + b.width >= s.x and b.x + b.width <= s.x + s.width:
                    if (b.y >= s.y and b.y <= s.y + s.height) or b.y + b.height >= s.y and b.y + b.height <= s.y + s.height:
                        score += 5 #Score minus 5 for shooting alien ship
                        Event('points', score, lives)
                        satallites.pop(satallites.index(s))
                        playerProjectiles.pop(playerProjectiles.index(b))
                        break
            
            

        for p in alienships:
            p.x += p.xvel
            p.y += p.yvel
            if p.x < -100 - p.width or p.x > swidth + 100 or p.y > sheight + 100 or p.y < -100 - p.height:
                alienships.pop(alienships.index(p))
                break
            for b in playerProjectiles:
                if (b.x >= p.x and b.x <= p.x + p.width) or b.x + b.width >= p.x and b.x + b.width <= p.x + p.width:
                    if (b.y >= p.y and b.y <= p.y + p.height) or b.y + b.height >= p.y and b.y + b.height <= p.y + p.height:
                        score += 5 #Score plus 5 for shooting alien ship
                        Event('points', score, lives)
                        alienships.pop(alienships.index(p))
                        playerProjectiles.pop(playerProjectiles.index(b))
                        break   

            if (p.x >= ship.x - ship.width // 2 and p.x <= ship.x + ship.width // 2) or (p.x + p.width <= ship.x + ship.width // 2 and p.x + p.width >= ship.x - ship.width // 2):  #Seeing if the two objects from the list cross over each others center point + width of themselves
                if (s.y >= ship.y - ship.height // 2 and s.y <= ship.y + ship.height // 2) or (s.y + s.height >= ship.y - ship.height // 2 and s.y + s.height <= ship.y + ship.height // 2):
                    lives -= 2  #Removes two life and then
                    Event('lives', score, lives)
                    alienships.pop(alienships.index(p))  #pops the asteroid that hit the ship
                    print(lives)  #prints lives in the console to test   
        
        #for b in playerProjectiles:
                #if (b.x >= doubleSpawner.x and b.x <= doubleSpawner.x + doubleSpawner.width) or b.x + b.width >= doubleSpawner.x and b.x + b.width <= doubleSpawner.x + doubleSpawner.width:
                    #if (b.y >= doubleSpawner.y and b.y <= doubleSpawner.y + doubleSpawner.height) or b.y + b.height >= doubleSpawner.y and b.y + b.height <= doubleSpawner.y + doubleSpawner.height:
                        #Event('points', score, lives)
                        #score += score
                        #break      
                #if (b.x >= fiftyPoints.x and b.x <= fiftyPoints.x + fiftyPoints.width) or b.x + b.width >= fiftyPoints.x and b.x + b.width <= fiftyPoints.x + fiftyPoints.width:
                    #if (b.y >= fiftyPoints.y and b.y <= fiftyPoints.y + fiftyPoints.height) or b.y + b.height >= fiftyPoints.y and b.y + b.height <= fiftyPoints.y + fiftyPoints.height:
                        #score += 50
                        #Event('points', score, lives)
                        #break     
                #if (b.x >= addLife.x and b.x <= addLife.x + addLife.width) or b.x + b.width >= addLifep.x and b.x + b.width <= addLife.x + addLife.width:
                    #if (b.y >= addLife.y and b.y <= addLife.y + addLife.height) or b.y + b.height >= addLife.y and b.y + b.height <= addLife.y + addLife.height:
                        #lives += 1  
                        #Event('lives', score, lives)
                        #break     

        
        if lives <= 0:
                gameover = True
        if score >= 20:
            level2state = True
        if score >= 40:
            level3state = True

            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gameover:
                        playerProjectiles.append(projectile())

    update()  #while game is running update is always running

pygame.quit()
