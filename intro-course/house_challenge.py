# Instructions:

# Using filled shapes, draw a simple house. Your house should have at least:

# A square or rectangle for the main building.
# A triangle for the roof.
# At least one window or door, using any shape.
# Feel free to add additional details like a chimney, pathway, or surrounding trees using shapes and colors.

# Tips:

# Use begin_fill() and end_fill() to fill in each shape.
# Change colors between shapes to make your house more vibrant.
# Use penup() and pendown() to move between different parts of your drawing without drawing lines.

from turtle import*


# house
begin_fill()
color("blue")

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

end_fill()

# door
penup()
forward(40)
pendown()

begin_fill()
color("brown")

left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(180)

end_fill()

# roof
penup()
forward(100)
pendown()

begin_fill()
color("brown")

right(90)
forward(30)
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(70)
left(90)
end_fill()

# chimney
penup()
forward(50)
pendown()

begin_fill()
color("#800020")

forward(30)
right(90)
forward(20)
right(90)
forward(60)
end_fill()


done()

# roof
# chimney
