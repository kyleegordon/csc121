# Kylee Gordon Lab-03 01/23/2022

# This program uses turtle graphics to draw two shapes from
# exercise 15 in chapter 2 of the textbook:
# Starting Out With Python 5th edition by Tony Gaddis

# set up turtle
import turtle
turtle.showturtle()
turtle.width(3)

# reposition the turtle pen for drawing
turtle.penup()
turtle.goto(-500, 250)

# draw two blue squares that are positioned at a 45 degree angle and touching corners in the middle
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.setheading(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

# reposition the turtle for the second shape
turtle.penup()
turtle.goto(500, -250)
turtle.pendown()

# draw olympic rings
turtle.circle(50)
turtle.penup()
turtle.goto(380, -250)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.goto(440, -200)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.goto(315, -200)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.goto(565, -200)
turtle.pendown()
turtle.circle(50)

# close turtle
turtle.done()
