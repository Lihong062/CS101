'''
DrawRandom.py
@author: Lihong Wang
'''

import turtle, BoundingBox, random, TurtleShapes

def drawEverywhere(turt, func):
    '''
    This Function calls turt to draw func n times, where user gives n
    size and location of drawings are randomized
    '''
    number = int(input('How many shapes to draw? '))
    for i in range(number):
        size = int(random.random()*35 + 15)
        randx = random.random()*400 - 200
        randy = random.random()*400 - 200
        turt.penup()
        turt.setx(randx)
        turt.sety(randy)
        turt.pendown()
        func(turt, size)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    ## CALL FUNCTIONS HERE
    turtle = turtle.Turtle()
    turtle.speed(0)

    shape = input('Input 1 to draw squares, 2 to draw the rainbow benzene: ')
    if shape == '2' or shape == 'drawOneRainbowBenzene':
        drawEverywhere(turtle, TurtleShapes.drawOneRainbowBenzene)
    elif shape == '1' or shape == 'drawOneShape':
        drawEverywhere(turtle, TurtleShapes.drawOneShape)


    win.exitonclick()
    