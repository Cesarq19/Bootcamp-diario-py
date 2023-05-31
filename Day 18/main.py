import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


#directions = [0, 90, 180, 270]
tim.speed("fastest")


for i in range(200):
    tim.color(random_color())
    tim.circle(200)
    #tim.forward(30)
    tim.setheading((i/200)*360)


screen = t.Screen()
screen.exitonclick()
