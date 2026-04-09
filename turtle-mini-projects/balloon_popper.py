import turtle
import random
import time

DIAMETER=40
pop_diameter=100
PENCIL_1=turtle.Turtle()
PENCIL_2=turtle.Turtle()
ACTIVE_PENCIL=PENCIL_2

def draw_balloon():
    global ACTIVE_PENCIL
    last_active_pencil=ACTIVE_PENCIL
    if ACTIVE_PENCIL==PENCIL_1:
        ACTIVE_PENCIL=PENCIL_2
    else:
        ACTIVE_PENCIL=PENCIL_1
    print (DIAMETER)
    PENCIL_1.color("red")
    PENCIL_2.color("red")
    ACTIVE_PENCIL.dot(DIAMETER)
    last_active_pencil.clear()

def set_diameter(new_diameter: int):
    global DIAMETER
    DIAMETER+=new_diameter

def inflate_balloon():
    set_diameter(new_diameter=10)
    draw_balloon()

    if DIAMETER >= pop_diameter:
        PENCIL_1.clear()
        PENCIL_2.clear()
        turtle.write("POP!")
        time.sleep(2)
        turtle.clear()

def deflate_balloon():
    set_diameter(new_diameter=-10)
    draw_balloon()

draw_balloon()

turtle.onkey(inflate_balloon, "Up")
turtle.onkey(deflate_balloon, "Down")
turtle.listen()

turtle.done()