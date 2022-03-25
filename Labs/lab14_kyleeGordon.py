# Kylee Gordon Lab-14 03/24/2022

# This program uses Turtle Graphics to draw a snowman

# set up turtle
import turtle
turtle.hideturtle()
turtle.width(1)
turtle.speed(0)


def main():
    drawBase(0, -200, 100)
    drawMidSection(0, 0, 75)
    drawHead(0, 150, 50)
    drawArms()
    drawButtons()
    drawScarf()


def drawBase(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)


def drawMidSection(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)


def drawArms():
    # Left Arm
    turtle.penup()
    turtle.goto(-75, 75)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(50)


def drawHead(x, y, radius):
    # Head
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)

    # Eyes
    turtle.penup()
    turtle.goto((x - (radius / 3)), (y + radius))
    turtle.pendown()
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.penup()
    turtle.goto((x + (radius / 3)), (y + radius))
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    # Mouth
    turtle.penup()
    turtle.goto((x - (radius / 2)), 180)
    turtle.pendown()
    turtle.forward(radius)

    # Hat
    drawHat(x, y, radius)



def drawHat(head_x, head_y, head_radius):
    # drawHead(0, 150, 50)
    # Hat Brim
    turtle.penup()
    turtle.goto((head_x - (1.5 * head_radius)), (head_y + (1.5 * head_radius)))
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.goto((head_x + (1.5 * head_radius)), (head_y + (1.5 * head_radius)))
    turtle.goto((head_x + (1.5 * head_radius)), (head_y + (2 * head_radius)))
    turtle.goto((head_x - (1.5 * head_radius)), (head_y + (2 * head_radius)))
    turtle.goto((head_x - (1.5 * head_radius)), (head_y + (1.5 * head_radius)))
    turtle.end_fill()

    # Hat Top
    turtle.penup()
    turtle.goto((head_x + (0.75 * head_radius)), (head_y + (2 * head_radius)))
    turtle.pendown()
    turtle.left(90)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(head_radius * 1.5)
        turtle.left(90)
    turtle.end_fill()


def drawScarf():
    pass


def drawButtons():
    pass


main()

# close turtle
turtle.done()
