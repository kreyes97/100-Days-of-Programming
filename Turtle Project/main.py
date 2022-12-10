from turtle import Turtle, Screen
from random import randint


def color_generator():
    colors = [
        "yellow",
        "gold",
        "orange",
        "red",
        "maroon",
        "violet",
        "magenta",
        "purple",
        "navy",
        "blue",
        "skyblue",
        "cyan",
        "turquoise",
        "lightgreen",
        "green",
        "darkgreen",
        "chocolate",
        "brown",
        "black",
        "gray",
    ]

    return colors[randint(0, len(colors) - 1)]


def main():
    turtle = Turtle()
    screen = Screen()
    screen.setup(width=1000, height=1000, startx=-0, starty=0)
    turtle.shape("circle")
    turtle.shapesize(0.50, 0.50)
    turtle.penup()
    turtle.goto((-480, -480))

    for j in range(-480, 500, 20):
        for i in range(-480, 500, 20):
            colors = color_generator()
            turtle.color(colors)
            turtle.stamp()
            turtle.goto((i, j))

    screen.exitonclick()


main()
