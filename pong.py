# I am using the turtle module to build the pong game


import turtle

wn = turtle.Screen()  # wn is my window for the game
wn.title("Pong by @thapussimon")  # The title I have is the string provided
wn.bgcolor("black")  # The Background Color I have chosen is Black
wn.setup(width=800, height=600)  # Building the baground Height for the height
wn.tracer(0)

# Paddle A Creation

paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Not speed of the paddle, This is speed of the Animation
paddle_a.shape("square")  # SHape of the paddle set to Square
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # The default size is small for our paddle so we increase the size
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B  Creation

paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Not speed of the paddle, This is speed of the Animation
paddle_b.shape("square")  # SHape of the paddle set to Square
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # The default size is small for our paddle so we increase the size
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball Creation
ball = turtle.Turtle()
ball.speed(0)  # Not speed of the paddle, This is speed of the Animation
ball.shape("circle")  # Shape of the ball set to circle
ball.color("yellow")
ball.penup()
ball.goto(0, 0)




# Functions For Movement


def paddle_a_up():
    y=paddle_a.ycor()  # It returns The Y y coordinate
























# Main Loop for the game
while True:
    wn.update()
