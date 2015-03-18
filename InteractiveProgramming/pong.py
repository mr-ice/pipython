# SimpleGUI PONG!
import simplegui

class Sprite:
    """A sprite is a video element, so it needs some things
    like position, size, color (basic in pong), and if it
    moves, a velocity"""
    def __init__(self):
        self._x_pos = 0
        self._y_pos = 0
        self._x_dim = 0
        self._y_dim = 0
        self._x_vel = 0
        self._y_vel = 0
        self._shape = 'point'
        self._color = "Red"
    
    def position(self,x,y):
        if x:
            self._x_pos = x
        if y:
            self._y_pos = y
        return [self._x_pos, self._y_pos]
    
    def size(self,h=None,w=None):
        self.width(w)
        self.height(h)
        return [self.width(),self.height()]

    def color(self,c=None):
        if c:
            self._color = c
        return self._color
    
    def height(self,y=None):
        if y:
            self._y_dim = y
        return self._y_dim
    
    def width(self,x=None):
        if x:
            self._x_dim = x
        return self._x_dim

    def move(self):
        self._x_pos = self._x_pos + self._x_vel
        self._y_pos = self._y_pos + self._y_vel

    def top(self):
        return [self._x_pos + self._x_dim,
                self._y_pos + self._y_dim]

    def bounce(self,x,y):
        """Bouncing off a plane will reverse one of the
        velocities"""
        if x: 
            """The plane is a horizontal plane"""
            self._y_vel *= -1
            
        if y:
            """The plane is a vertical plane"""
            self._x_vel *= -1

    def accelerate(self, magnitude, direction):
        """Accelerate the sprite by adding a force and direction
        to the current velocity.
        
        magnitude = pixels per second
        direction = degrees where 0 = north
        
        due to simplegui's mirrored directions, we have to subtract
        the direction in degreees from 180 first
        """
        from math import sin,cos,radians
        self._x_vel += cos(radians(180-direction)) * magnitude
        self._y_vel += sin(radians(180-direction)) * magnitude
        
class Rectangle(Sprite):
    def __init__(self):
        self._shape = 'rectangle'
        
    def draw(self,canvas):
        return canvas.draw_polygon(
            [[self._x_pos, self._y_pos],
             [self._x_pos, self._y_pos + self._y_dim],
             [self._x_pos + self._x_dim, self._y_pos + self._y_dim],
             [self._x_pos + self._x_dim, self._y_pos]],
            self._line_width,
            self._color)
    
    def dim(self):
        """dimensions of the rectangle is two points.  Here we return 
        x0, y0, x1, y1 so that the intersect function can compare them."""
        return [self._x_pos, 
                self._y_pos,
                self._x_pos + self._x_dim,
                self._y_pos + self._y_dim]
    
    def intersect(self,sprite):
        """Determine if we intersect another rectangular sprite"""
        me = self.dim()
        it = sprite.dim()
        
        if (me[0] <= it[2] and me[2] >= it[0] and
            me[3] <= it[1] and me[1] >= it[3]):
            return False
        else:
            return True
        
class Polygon(Sprite):
    def __init__(self):
        self._shape = 'polygon'
    
    def draw(self,canvas):
        """polygons have five or more points"""
        points = self._points * self.position()
        canvas.draw_polygon(
            [points],
            self._line_width,
            self._color)
      
class Circle(Sprite):
    def __init__(self):
        self._shape = 'circle'
        self._radius = 1

    def draw(self,canvas):
        """circles are defined by one point and a radius"""
        canvas.draw_circle([self._x_pos, self._y_pos], self._radius, self._line_width, self._color)

class One(Rectangle):
    def __init__(self):
        self._color = 'white'
        self.size(40,10)

class Two(Rectangle):
    def __init__(self):
        
def tick():
    """Handler to handle the time tick"""
    for polygon in moving:
        polygon.move()

        [px,py] = polygon.position()
        if px < 0:
            polygon.
    
def draw(canvas):
	"""Handler to draw on canvas"""
    global polygons	
    for polygon in polygons:
        polygon.draw(canvas)

      
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 600)
frame.add_button("Start", click)
frame.add_button("Reset", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
