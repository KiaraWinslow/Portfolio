from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
t.penup()
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
sides = 4
pencolor("pink")
pendown()
fillcolor("pink")
begin_fill()
while sides > 0:
    forward(100)
    right(90)
    sides = sides-1
penup()
end_fill()

forward (200)

sides = 3
pencolor("purple")
pendown()
fillcolor("purple")
begin_fill()
while sides > 0:
    forward(200)
    right(120)
    sides = sides-1
penup()
end_fill()

forward(-300)
pencolor("green")
pendown()
begin_fill()
fillcolor("green")
circle(100,360,360)
penup()
end_fill()


# Close window on click.
exitonclick()
