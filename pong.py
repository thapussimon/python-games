# I am using the turtle module to build the pong game


import turtle

wn = turtle.Screen()  # wn is my window for the game
wn.title("Pong by @thapussimon")  # The title I have is the string provided
wn.bgcolor("black")  # The Background Color I have chosen is Black
wn.setup(width=800, height=600)  # Building the baground Height for the height
wn.tracer(0)

# Main Loop for the game
while True:
    wn.update()
