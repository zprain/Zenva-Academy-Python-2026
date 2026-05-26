from turtle import *

speed(0)

move_distance = 50

bgcolor("#D2691E")

penup()
goto(200, 450)
pendown()

color("blue")

begin_fill()
goto(500, 450)
goto(500, -450)
goto(200, -450)
goto(200, 450)
end_fill()

penup()
goto(-200, 0)
shape("turtle")
color("green")


def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()


def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()


def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()


def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()


def check_goal():
    if xcor() > 200:
        hideturtle()
        color("white")
        write("YOU WIN!")
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")


onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")

listen()

done()
