# import colorgram
#
# colors=colorgram.extract('image.jpg',40)
#
# rgb_color=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
from turtle import Turtle, Screen
import random

def hirst_painting():
    for _ in range(10):
        t.pendown()
        t.dot(10, random.choice(color_list))
        t.penup()
        t.forward(50)
    for _ in range(30):
        t.penup()
        t.right(90)
        t.forward(50)
        t.right(90)

color_list=[(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

t=Turtle()
screen=Screen()
t.shape("arrow")
t.color("black")
t.speed("fastest")
screen.colormode(255)
t.penup()
t.goto(-150,100)
y_pos=100
for _ in range(10):
    t.penup()
    hirst_painting()
    t.penup()
    y_pos-=20
    t.goto(-150,y_pos)
    t.setheading(0)
    t.pendown()

screen.exitonclick()
