'''
TurtleShapes.py
@author: Lihong Wang
'''

import turtle, BoundingBox

def drawOneShape(turt, size):
    '''
    This Function Draws a Colorful Square
    '''
    colors = ['blue', 'red', 'green', 'orange']
    for i in range(4):
        turt.color(colors[i])
        turt.forward(size)
        turt.right(90)

def drawOneRainbowBenzene(turt, size):
    '''
    This Function Draws a Colorful Benzene
    '''
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    for x in range(size):
        turt.pencolor(colors[x % 6])
        turt.forward(x)
        turt.left(58)
    turt.setheading(0)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    ## CALL FUNCTIONS HERE
    turtle = turtle.Turtle()
    turtle.speed(0)
    # Sets up the turtle

    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    # Moves the turtle

    drawOneShape(turtle, 50)

    turtle.right(180)
    turtle.penup()
    turtle.forward(250)
    turtle.pendown()
    turtle.right(180)
    # Moves the turtle

    drawOneRainbowBenzene(turtle, 100)
    # This thing technically has 2 shapes (hexagon and triangles inside the hexagon)

    win.exitonclick()
