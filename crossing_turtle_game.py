from turtle import Screen
from players import Player
from cars import CarManager
from scoreboard import Score
import time

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Score()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.move_car()

    if player.level_up():
        player.go_to_start()
        cars.speed_up()
        score.points()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()


screen.exitonclick()