import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(fun=Player.go_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
