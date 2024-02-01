from turtle import Turtle, Screen

mike = Turtle()
screen = Screen()


def move_forward():
    mike.forward(10)


def move_backward():
    mike.backward(10)


def turn_right():
    mike.right(10)


def turn_left():
    mike.left(10)


def clear_screen():
    mike.clear()
    mike.penup()
    mike.home()
    mike.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_screen, "c")

screen.exitonclick()
