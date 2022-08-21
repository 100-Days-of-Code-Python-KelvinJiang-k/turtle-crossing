from car import Car
CAR_SPEED_INCREASE = 2


class CarManager:

    def __init__(self):
        self.cars = []

    def create_car(self):
        car = Car()
        self.cars.append(car)

    def increase_car_speeds(self):
        for i, car in enumerate(self.cars):
            self.cars[i].car_speed += CAR_SPEED_INCREASE

    def move_cars(self):
        for i, car in enumerate(self.cars):
            car.move_left()
            if car.xcor() < -340:
                del self.cars[i]
