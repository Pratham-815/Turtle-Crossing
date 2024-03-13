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

car_manager = CarManager()

Scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()


screen.exitonclick()