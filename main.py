from turtle import Screen
from avatar import Avatar
from carManager import CarManager
from scoreboard import Scoreboard
from time import sleep
INITIAL_CAR_SPAWN_SPEED = 6
FINISH_LINE = 280

screen = Screen()

screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)

avatar = Avatar()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(avatar.move_up, "w")

game_is_on = True
car_spawn_speed = INITIAL_CAR_SPAWN_SPEED  # Smaller number = faster spawns
loop_iterations = car_spawn_speed
while game_is_on:
    sleep(0.1)
    screen.update()

    # Car Spawner
    if loop_iterations == car_spawn_speed:
        car_manager.create_car()
        loop_iterations = 0
    else:
        loop_iterations += 1

    car_manager.move_cars()

    # Detect avatar to car collision
    for car in car_manager.cars:
        if avatar.distance(car) < 15:
            game_is_on = False
            avatar.refresh()
            scoreboard.game_over()

    # Detect avatar to finish line collision
    if avatar.ycor() > FINISH_LINE:
        scoreboard.update()
        avatar.refresh()

        # Increase difficulty
        car_manager.increase_car_speeds()
        if scoreboard.score % 1 == 0 and car_spawn_speed >= 2:
            car_spawn_speed -= 1

screen.exitonclick()
