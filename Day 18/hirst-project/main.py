# import colorgram
#
#
# def obtain_colors(number_of_colors):
#     colors = colorgram.extract('imageBackground.jpg', number_of_colors)
#     response = list()
#
#     for i in range(number_of_colors - 1):
#         rgb = colors[i].rgb
#
#         r = rgb.r
#         g = rgb.g
#         b = rgb.b
#         response.append((r, g, b))
#
#     return response
#
#
# print(obtain_colors(30))
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


color_list = [(206, 159, 112), (138, 173, 192), (223, 206, 119), (43, 106, 138), (139, 183, 149), (15, 52, 75),
              (218, 88, 65), (36, 126, 105), (124, 81, 95), (193, 133, 145), (71, 164, 120), (145, 81, 71),
              (12, 58, 49), (55, 153, 180), (51, 34, 43), (126, 37, 50), (205, 85, 102), (175, 206, 171),
              (6, 109, 87), (229, 168, 182), (147, 204, 230), (157, 153, 67), (33, 64, 101), (16, 84, 100),
              (47, 30, 27)]


coord_x = 0
coord_y = 0

for row in range(10):
    for column in range(10):
        tim.setx(coord_x)
        tim.sety(coord_y)
        tim.dot(20, random.choice(color_list))
        coord_x += 50
    coord_x = 0
    coord_y += 50

screen = t.Screen()
screen.exitonclick()
