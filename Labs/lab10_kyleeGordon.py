# Kylee Gordon Lab-10 02/15/2022

# This program uses turtle graphics to draw a star pattern as shown in chapter 4 exercise 17

# set up turtle
import turtle

# output - draw star pattern
for x in range(0, 8):
    turtle.forward(200)
    turtle.right(135)

# close turtle
turtle.done()
