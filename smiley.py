import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0) 

def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


draw_circle(0, 0, 100, "yellow")


draw_circle(-35, 35, 15, "black")
draw_circle(35, 35, 15, "black")

pen.penup()
pen.goto(-50, -20)
pen.pendown()
pen.width(5)
pen.setheading(-60)
pen.circle(80, 120)

turtle.done()