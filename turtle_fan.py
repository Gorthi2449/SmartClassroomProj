import turtle

#mlt.color("green")
#square()
#exitonclick()
def res1():

    def moving_object(move):
        # to fill the color in ball
        move.begin_fill()
        move.color('black')
        move.left(30)
        move.forward(30)
        move.right(30)
        move.forward(200)
        move.right(90)
        move.forward(30)
        move.right(90)
        move.forward(200)
        move.right(30)
        move.forward(30)
        move.end_fill()
        move.begin_fill()
        move.color('black')
        move.forward(30)
        move.right(30)
        move.forward(200)
        move.right(90)
        move.forward(30)
        move.right(90)
        move.forward(200)
        move.right(30)
        move.forward(30)
        move.end_fill()
        move.begin_fill()
        move.color('black')
        move.forward(30)
        move.right(30)
        move.forward(200)
        move.right(90)
        move.forward(30)
        move.right(90)
        move.forward(200)
        move.right(30)
        move.forward(30)
        move.end_fill()
    # create a screen object
    screen = turtle.Screen()

    # set screen size
    screen.setup(600, 600)

    # screen background color
    screen.bgcolor('green')

    # screen updaion
    screen.tracer(0)

    # create a turtle object object
    move = turtle.Turtle()

    # set a turtle object color
    move.color('orange')

    # set turtle object speed
    move.speed(0)

    # set turtle object width
    move.width(2)

    # hide turtle object
    move.hideturtle()

    # turtle object in air
    move.penup()

    # set initial position
    move.goto(0, 0)

    # move turtle object to surface
    move.pendown()

    # infinite loop
    while True:
        # clear turtle work
        move.clear()

        # call function to draw ball
        moving_object(move)

        # update screen
        screen.update()

        # forward motion by turtle object
        move.left(3)







