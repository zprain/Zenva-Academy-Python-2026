# square_artwork_challenge

import turtle

# prepare program (define common values and additional helper functions).

RED_HEX_CODE="#FF0000"

def draw_square(square_size: int = 100, square_color: str = RED_HEX_CODE):
    """
    Draws a filled square using the turtle graphics library.

    The function initializes a fill, moves the turtle in a clockwise direction 
    to create a square based on the provided size, and then applies the 
    specified color. Once the drawing is complete, it invokes turtle.done() 
    to pause the graphics window.

    Args:
        square_size (int): The length of each side of the square in pixels. 
            Defaults to 100.
        square_color (str): A string representing a color name (e.g., 'blue') 
            or a hex code (e.g., '#FF0000'). Defaults to RED_HEX_CODE.

    Note:
        This function calls `turtle.done()`, which may cause the program 
        to hang or prevent further code from executing until the graphics 
        window is manually closed.
    """
    # ... your code logic ...
    # logic to draw a square
    turtle.begin_fill()
    turtle.color(square_color)

    turtle.forward(square_size)
    turtle.right(90)
    turtle.forward(square_size)
    turtle.right(90)
    turtle.forward(square_size)
    turtle.right(90)
    turtle.forward(square_size)
    

    turtle.end_fill()

# program execution
print("draw_square_function_defined")
draw_square(square_size=200, square_color="blue")
draw_square()

turtle.done()