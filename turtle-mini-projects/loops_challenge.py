import turtle

# PEOPLE=["Zac", "Alex"]

# for person in PEOPLE:
#     print("Hello " + person)

def move_and_turn(angle):
    turtle.forward(50)
    turtle.right(angle)

# for i in range(4):
#     move_and_turn(90)

num_moves_made=0

while num_moves_made < 4:
    move_and_turn(90)
    print(num_moves_made)
    num_moves_made+=1

turtle.done()