from turtle import Turtle, Screen

global turtle
turtle = Turtle()


def forward():
    turtle.forward(50)


def left():
    turtle.left(10)


def right():
    turtle.right(10)


def main():
    screen = Screen()

    screen.listen()
    screen.onkeypress(key="space", fun=forward)
    screen.onkeypress(key="Left", fun=left)
    screen.onkeypress(key="Right", fun=right)
    screen.exitonclick()


main()
