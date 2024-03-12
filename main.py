import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(fun=player.go_up, key="Up")

can_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    can_manager.create_car()
    can_manager.move_cars()