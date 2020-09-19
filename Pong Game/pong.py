import turtle

wn = turtle.Screen()
wn.title("Pong by thapussimon")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Speed OF the ANimation Not The speed Of the Paddle
paddle_a.shape("square")
paddle_a.color("white")

paddle_a.penup()  # Turtles By Definition Draws a line, In Here We do not need to draw a line
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_len=1, stretch_wid=5)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Speed OF the ANimation Not The speed Of the Paddle
paddle_b.shape("square")
paddle_b.color("white")

paddle_b.penup()  # Turtles By Definition Draws a line, In Here We do not need to draw a line
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_len=1, stretch_wid=5)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)

# Every Time The Ball Moves It Moves By 0.3 Pixels
ball.dx = 0.2
ball.dy = 0.2

# Score

score_a = 0
score_b = 0
# Score Board Development

pen = turtle.Turtle()
pen.speed(0)  # Animation Speed
pen.color("white")
pen.penup()  # Do not want to draw lines after the turtle moves
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


# Functions for Paddel Movements


# Paddle A Movement

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Paddle B Movement
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border CHecking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # Paddle And Ball COllisions Just Play Around with The Coordinates Till You Get it Right

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < - 340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
