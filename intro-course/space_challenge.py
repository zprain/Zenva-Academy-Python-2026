from turtle import*

# space
bgcolor("black")

# orange
begin_fill()
color("orange")
circle(60)
end_fill()

# ring
penup()
left(90)
forward(30)
right(90)
pendown()

begin_fill()
color("blue")

backward(53)
# left(30)
# forward(5)
# left(30)
# forward(5)
# left(90)
# forward(150)
right(90)
circle(70,240)

# left(30)
# forward(5)
# left(30)
# forward(5)
# left(90)
# forward(150)


penup()
forward(150)
pendown()

# gray
begin_fill()
color("gray")
circle(20)
end_fill()

penup()
forward(80)
pendown()

# red
begin_fill()
color("red")
circle(40)
end_fill()

penup()
forward(90)
pendown()

# green
begin_fill()
color("green")
circle(30)
end_fill()

penup()
backward(490)
left(90)
forward(200)
pendown()


#star 
begin_fill()
color("yellow")
# star constant
STAR_POINT_ANGLE=95
STAR_POINT_SIDE_LENGTH=50
STAR_POINT_INTERSECTION_ANGLE=165

# point1
right(135)
forward(STAR_POINT_SIDE_LENGTH)
left(STAR_POINT_INTERSECTION_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)
# point2
right(STAR_POINT_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)
left(STAR_POINT_INTERSECTION_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)

# point3
right(STAR_POINT_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)
left(STAR_POINT_INTERSECTION_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)

# point4
right(STAR_POINT_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)
left(STAR_POINT_INTERSECTION_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)

# point5
right(STAR_POINT_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)
left(STAR_POINT_INTERSECTION_ANGLE)
forward(STAR_POINT_SIDE_LENGTH)

end_fill()

done()