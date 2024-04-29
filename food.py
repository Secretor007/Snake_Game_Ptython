from turtle import Turtle
import random

COLOR_LIST = [(84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251),
              (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0),
              (254, 147, 146), (253, 71, 70), (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216),
              (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rgb = random.choice(COLOR_LIST)
        color_hex = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
        self.color(color_hex)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.penup()
        self.goto(random_x, random_y)
