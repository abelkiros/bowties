"""
 file: bowties.py
 language: python3
 author: amk7296@g.rit.edu abel m kiros
 description: This program uses turtle graphics to recursivly draw of bowties.
"""
import turtle as t

t.setup(600,600)

def draw_one_bowtie(depth,size):
    """ draw_one_bowtie_2 draws the bowtie shape and bowties 1/3 its sizes.
            depth ( int ): The current depth of recursion
            size ( int ): The size of the current depth
            Pre-conditions:
              depth >= 0, size > 0,
              turtle is facing east turtle pen is up
            Post-conditions:
              Depths of the bowties were drawn for the current depth
              turtle is facing east and turtle pen is up.
    """
    t.pencolor('blue')
    t.pendown()
    t.left(30)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.forward(size*2)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.right(120)
    t.up()
    t.forward(size*1/4)
    t.left(90)
    t.down()
    t.fillcolor('red')
    t.begin_fill()
    t.circle(size*1/4)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(size * 1 / 4)
    t.right(90)

def draw_one_bowtie_2(depth,size):
    """ draw_one_bowtie_2 draws the bowtie shape and bowties 1/3 its sizes.
          depth ( int ): The current depth of recursion
          size ( int ): The size of the current depth
          Pre-conditions:
              depth >= 0, size > 0,
              turtle is facing east turtle pen is up
          Post-conditions:
              Depths of the bowties were drawn for the current depth
              turtle is facing east and turtle pen is up.
    """
    draw_one_bowtie(depth,size)
    t.left(30)
    t.up()
    t.forward(size * 2)
    t.down()
    draw_one_bowtie(depth,size / 3)
    t.up()
    t.forward(-size * 2)
    t.right(60)
    t.forward(-size * 2)
    t.down()
    draw_one_bowtie(depth, size / 3)
    t.up()
    t.forward(size * 4)
    t.down()
    draw_one_bowtie(depth, size / 3)
    t.up()
    t.forward(-size * 2)
    t.right(120)
    t.up()
    t.forward(size * 2)
    t.down()
    draw_one_bowtie(depth,size / 3)
    t.up()
    t.forward(-size * 2)
    t.left(150)


def draw_bowties(depth, size):
    """ draw_bowties recursively draws the bowtie shape.
        depth ( int ): The current depth of recursion
        size ( int ): The size of the current depth
        Pre-conditions:
            depth >= 0, size > 0,
            turtle is facing east turtle pen is down
        Post-conditions:
            Depths of the bowties were drawn for the current depth
            turtle is facing east and turtle pen is up.
    """
    if depth == 0:
        pass

    elif depth == 1:
        draw_one_bowtie(depth-1, size)

    elif depth == 2:
       draw_one_bowtie_2(depth-1, size)

    else:
        draw_one_bowtie(depth-1, size)
        t.left(30)
        t.up()
        t.forward(size*2)
        draw_bowties(depth - 1, size / 3)
        t.back(size * 2)
        t.right(60)
        t.forward(size*2)
        draw_bowties(depth-1,size/3)
        t.back(size * 2)
        t.right(120)
        t.forward(size * 2)
        draw_bowties(depth - 1, size / 3)
        t.back(size * 2)
        t.right(60)
        t.forward(size*2)
        draw_bowties(depth - 1, size / 3)
        t.back(size*2)
        t.right(150)

def main(depth, size):
    """ The main function runs the recursive function and takes in user input
           depth ( int ): The current depth of recursion
           size ( int ): The size of the current depth
           Pre-conditions: Takes user input
           Post-conditions: runs function using inputted values
    """
depth = int(input("Enter an integer for the depth: "))

t.speed(0)
draw_bowties(depth, 100)
t.done()

main(depth, 100)


