'''
DrawRow.py

@author: Lihong Wang
'''

import turtle, BoundingBox, TurtleShapes

def drawRowsOfRows(turt, func):
    '''
    This Function Draws 10 rows of func with the base being larger than the top
    '''
    turt.penup()
    turt.setx(-200)
    turt.sety(-200)
    turt.pendown()
    for row in range(10):
        turt.penup()
        turt.sety(-200 + row * 40)
        turt.pendown()
        for column in range(10):
            turt.penup()
            turt.setx(-200+ column * 40)
            turt.sety(-200 + row * 40)
            turt.pendown()
            func(turt, 25 - 2*row)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    ## CALL FUNCTIONS HERE
    func = TurtleShapes.drawOneRainbowBenzene
    turtle = turtle.Turtle()
    turtle.speed(0)

    drawRowsOfRows(turtle, func)
    
    win.exitonclick()
    