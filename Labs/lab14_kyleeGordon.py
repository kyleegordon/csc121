# Kylee Gordon Lab-14 03/25/2022

# This program uses Turtle Graphics to draw a snowman

# Set up turtle
import turtle
turtle.hideturtle()
turtle.width(1)
turtle.speed(0)


def main():
    drawBase(0, -200, 100)
    drawMidSection(0, 0, 75)
    drawHead(0, 150, 50)


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

    drawArms(x, y, radius)

    drawButtons(x, y, radius)


def drawArms(mid_x, mid_y, mid_radius):
    # Left Arm
    turtle.penup()
    turtle.goto((mid_x - mid_radius), (mid_y + mid_radius))
    turtle.pendown()
    turtle.setheading(150)
    turtle.forward(mid_radius * 0.67)
    turtle.right(45)
    turtle.forward(mid_radius * 0.67)
    turtle.right(45)
    turtle.forward(mid_radius / 5)
    turtle.back(mid_radius / 5)
    turtle.left(90)
    turtle.forward(mid_radius / 5)

    # Right Arm
    turtle.penup()
    turtle.goto((mid_x + mid_radius), (mid_y + mid_radius))
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(mid_radius)
    turtle.right(45)
    turtle.forward(mid_radius / 5)
    turtle.back(mid_radius / 5)
    turtle.left(90)
    turtle.forward(mid_radius / 5)


def drawHead(x, y, radius):
    # Head
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(radius)

    # Eyes
    drawFilledCircle((x - (radius / 3)), (y + radius), (radius / 10), 'blue')
    drawFilledCircle((x + (radius / 3)), (y + radius), (radius / 10), 'blue')

    # Mouth
    turtle.penup()
    turtle.goto((x - (radius / 2)), 180)
    turtle.pendown()
    turtle.forward(radius)

    drawHat(x, y, radius)

    drawScarf(x, y, radius)


def drawHat(head_x, head_y, head_radius):
    # Hat Brim
    turtle.penup()
    turtle.goto((head_x - (1.5 * head_radius)), (head_y + (1.5 * head_radius)))
    turtle.pendown()
    drawFilledRectangle(head_radius * 3, head_radius / 2, 'black')

    # Hat Top
    turtle.penup()
    turtle.goto((head_x + (0.75 * head_radius)), (head_y + (2 * head_radius)))
    turtle.pendown()
    turtle.setheading(0)
    turtle.left(90)
    drawFilledRectangle((head_radius * 1.5), (head_radius * 1.5), 'black')


def drawScarf(head_x, head_y, head_radius):
    turtle.penup()
    turtle.goto(head_x - head_radius, (head_y - (head_radius / 5)))
    turtle.pendown()
    turtle.pencolor('red')
    turtle.setheading(0)

    drawFilledRectangle((head_radius * 2), (head_radius / 3), 'red')
    turtle.right(45)
    drawFilledRectangle(head_radius, (head_radius / 3), 'red')
    turtle.left(135)
    drawFilledRectangle(head_radius, (head_radius / 3), 'red')

    turtle.pencolor('black')


def drawButtons(mid_x, mid_y, mid_radius):
    # Top Button
    drawFilledCircle(mid_x, (mid_y + (mid_radius * 1.5)), (mid_radius / 15), 'purple')

    # Middle Button
    drawFilledCircle(mid_x, (mid_y + mid_radius), (mid_radius / 15), 'purple')

    # Bottom Button
    drawFilledCircle(mid_x, (mid_y + (mid_radius * 0.5)), (mid_radius / 15), 'purple')


def drawFilledCircle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def drawFilledRectangle(length, width, color):
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.end_fill()


main()

# close turtle
turtle.done()
