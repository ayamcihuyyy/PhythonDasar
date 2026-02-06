import turtle
from PIL import Image

def save_as_jpg(canvas, filename):
    # same as before
    ...

def drawRectangle(ttl, x, y, width, height):
    """ Draw a rectangle of dimensions width and height, with upper """
    ttl.up()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.down()
    for i in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.up()

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)
    ttl.penup()

def fillTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    # This assumes color is given as a Hex string value.
    ttl.fillcolor(color)
    ttl.begin_fill()
    drawTriangle(ttl, x1, y1, x2, y2, x3, y3)
    ttl.end_fill()

# set up the screen size (in pixels - 1000 x 1000)
# set the starting point of the turtle (0, 0)
turtle.setup(1500, 1000, 0, 0)

myBlue   = "#003882"
myYellow = "#FCD647"
myRed    = "#D12421"
myGreen  = "#007336"
myWhite  = "#FFFFFF"

Joe = turtle.Turtle()
Joe.screen.colormode(255)

drawRectangle(Joe, 0, 300)