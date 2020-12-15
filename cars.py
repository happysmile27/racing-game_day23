from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            turtle = Turtle()
            turtle.shape("square")
            turtle.shapesize(1, 2)
            turtle.penup()
            turtle.color(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            turtle.goto(300, random_y)
            self.all_cars.append(turtle)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

