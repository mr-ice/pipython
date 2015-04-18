# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600

angular_acceleration = 0.06
friction = 0.06

class Game:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.time = 0.5

class Image:
    def __init__(self, url, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
        self.image = simplegui.load_image(url)

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris = Image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png",[320, 240], [640, 480])

# nebula images - nebula_brown.png, nebula_blue.png
nebula = Image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png",[400, 300], [800, 600])

# splash image
splash = Image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png",[200, 150], [400, 300])

# ship image
ship = Image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png",[45, 45], [90, 90], 35)

# missile image - shot1.png, shot2.png, shot3.png
missile = Image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png",[5,5], [10, 10], 3, 50)

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid = Image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png",[45, 45], [90, 90], 40)

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion = Image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png",[64, 64], [128, 128], 17, 24, True)

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack.set_volume(.5)
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_thrust_sound.set_volume(.5)
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
explosion_sound.set_volume(.5)

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = image.get_center()
        self.image_size = image.get_size()
        self.radius = image.get_radius()
        
    def draw(self,canvas):
        canvas.draw_image(self.image.image,
                          self.image.get_center(),
                          self.image.get_size(),
                          self.pos, self.image.get_size(), self.angle)
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        print self.pos, self.vel, self.thrust, self.angle, angle_to_vector(self.angle)
        self.angle += self.angle_vel
        if self.thrust:
            direction = angle_to_vector(self.angle)
            for x in range(2):
                direction[x] *= angular_acceleration 
                self.vel[x] += direction[x]
        else:
            for x in range(2):
                self.vel[x] = self.vel[x] * (  1 - friction )
                if self.vel[x] < 0.0000001: self.vel[x] = 0
                    
        for x in range(2):
            self.pos[x] += self.vel[x]
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image.image,
                          self.image.get_center(),
                          self.image.get_size(),
                          self.pos, self.image.get_size())
    
    def update(self):
        pass        
           
def draw(canvas):
    global game
    
    # animate background
    game.time += 1
    wtime = (game.time / 4) % WIDTH
    center = debris.get_center()
    size = debris.get_size()
    canvas.draw_image(nebula.image, nebula.get_center(), nebula.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris.image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris.image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    pass

def key_down(key):
    global my_ship, angular_acceleration
    if key==simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -angular_acceleration
    if key==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = angular_acceleration
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
        
def key_up(key):
    global my_ship, angular_acceleration
    if key==simplegui.KEY_MAP["left"]:
        if my_ship.angle_vel == -angular_acceleration:
            my_ship.angle_vel = 0
    if key==simplegui.KEY_MAP["right"]:
        if my_ship.angle_vel == angular_acceleration:
            my_ship.angle_vel = 0
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrust = False
        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize game
game = Game()

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 10, ship)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

# If, for some reason, you must use Firefox or another browser (or had issues playing sounds in Chrome), please give your peers full credit on the two sound-related rubric items.
# 1 pt - The program draws the ship as an image.
# 1 pt - The ship flies in a straight line when not under thrust.
# 1 pt - The ship rotates at a constant angular velocity in a counter clockwise direction when the left arrow key is held down.
# 1 pt - The ship rotates at a constant angular velocity in the clockwise direction when the right arrow key is held down.
# 1 pt - The ship's orientation is independent of its velocity.
# 1 pt - The program draws the ship with thrusters on when the up arrow is held down.
# 1 pt - The program plays the thrust sound only when the up arrow key is held down.
# 1 pt - The ship accelerates in its forward direction when the thrust key is held down.
# 1 pt - The ship's position wraps to the other side of the screen when it crosses the edge of the screen.
# 1 pt - The ship's velocity slows to zero while the thrust is not being applied.
# 1 pt - The program draws a rock as an image.
# 1 pt - The rock travels in a straight line at a constant velocity.
# 1 pt - The rock is respawned once every second by a timer.
# 1 pt - The rock has a random spawn position, spin direction and velocity.
# 1 pt - The program spawns a missile when the space bar is pressed.
# 1 pt - The missile spawns at the tip of the ship's cannon.
# 1 pt - The missile's velocity is the sum of the ship's velocity and a multiple of its forward vector.
# 1 pt - The program plays the missile firing sound when the missile is spawned.
# 1 pt - The program draws appropriate text for lives on the upper left portion of the canvas.
# 1 pt - The program draws appropriate text for score on the upper right portion of the canvas.
