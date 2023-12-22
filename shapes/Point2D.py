from .Shape2D import Shape2D
import random
import math


class Point2D(Shape2D):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other_point) -> float:
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def distance_from_start(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @classmethod
    def random_init(cls):
        return cls(random.random() * 100, random.random() * 100)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
