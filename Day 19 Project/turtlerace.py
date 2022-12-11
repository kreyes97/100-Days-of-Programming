from turtle import Turtle, Screen
from random import randint


def create_turtles():
    turtle1 = Turtle()
    turtle2 = Turtle()
    turtle3 = Turtle()
    turtle4 = Turtle()
    turtle5 = Turtle()
    turtle6 = Turtle()
    colors = {
        turtle1: "red",
        turtle2: "orange",
        turtle3: "yellow",
        turtle4: "green",
        turtle5: "blue",
        turtle6: "violet",
    }
    turtles = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6]

    return turtles, colors


def create_finish():
    finish_line = Turtle()
    finish_line.penup()
    finish_line.goto(200, 200)
    finish_line.pendown()
    finish_line.right(90)
    finish_line.forward(400)
    finish_line.hideturtle()


def move_turtle(turtle):
    movement_range = [i for i in range(10, 50, 10)]
    turtle.forward(movement_range[randint(0, len(movement_range) - 1)])


def main():
    user_selection = input("Who will win the race? Enter a color: ")
    turtles = create_turtles()

    while True:
        if user_selection not in [value for key, value in turtles[1].items()]:
            print("Invalid input.")
            user_selection = input("Who will win the race? Enter a color: ")
        else:
            break

    position = -60
    screen = Screen()

    screen.setup(width=500, height=500, startx=-0, starty=0)

    for i in range(0, len(turtles[0])):
        turtles[0][i].shape("turtle")
        turtles[0][i].color(turtles[1][turtles[0][i]])
        turtles[0][i].penup()
        turtles[0][i].goto((-220, position))
        position += 30

    create_finish()

    status = True
    winners = []

    while status:
        for i in range(0, len(turtles[0])):
            move_turtle(turtles[0][i])
        for i in range(0, len(turtles[0])):
            if turtles[0][i].pos()[0] >= 195:
                winners.append(turtles[1][turtles[0][i]])

        if len(winners) > 0:
            break
        else:
            continue

    if user_selection in winners and len(winners) == 1:
        print(f"You win! The {winners[0]} turtle is the winner!")
    elif user_selection in winners and len(winners) != 1:
        print(f"Tie! The {', '.join(winners)} turtles are the winners!")
    elif user_selection not in winners and len(winners) != 1:
        print(f"You lose! The {', '.join(winners)} turtles are the winners!")
    else:
        print(f"You lose! The {winners[0]} turtle is the winner!")

    screen.exitonclick()


main()
