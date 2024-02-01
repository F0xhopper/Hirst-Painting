from turtle import Turtle,Screen,colormode
import random
import colorgram
mr_turtle = Turtle()
colormode(255)
# rgb_colors = []
# colors = colorgram.extract('hirsts-painting.jpg',30)
# print(colors)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49),  (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

mr_turtle.setheading(225)
mr_turtle.forward(300)
mr_turtle.setheading(0)
number_of_dots = 100


for dot_count in range(1,number_of_dots +1):
    mr_turtle.dot(20)
    


screen = Screen()
screen.exitonclick()