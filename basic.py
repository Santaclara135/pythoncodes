import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Set speed to fastest
pen.hideturtle()

# Function to draw a rectangle
def draw_rectangle(turtle, width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

# Function to draw a triangle
def draw_triangle(turtle, side):
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)

# Draw the base of the house
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.fillcolor("lightgray")
pen.begin_fill()
draw_rectangle(pen, 200, 150)
pen.end_fill()

# Draw the roof
pen.penup()
pen.goto(-110, 50)
pen.pendown()
pen.fillcolor("brown")
pen.begin_fill()
draw_triangle(pen, 220)
pen.end_fill()

# Draw the door
pen.penup()
pen.goto(-40, -100)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
draw_rectangle(pen, 40, 70)
pen.end_fill()

# Draw windows
pen.penup()
pen.goto(-80, 0)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
draw_rectangle(pen, 30, 30)
pen.end_fill()

pen.penup()
pen.goto(20, 0)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
draw_rectangle(pen, 30, 30)
pen.end_fill()

# Keep the window open until it is closed manually
turtle.done()