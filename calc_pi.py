import math
import sys
from random import uniform


class Point2D(object):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other_point) -> float:
        dx = self.x - other_point.x
        dy = self.y - other_point.y

        distance = math.sqrt(dx * dx + dy * dy)
        return distance


class PiCalculator(object):

    def __init__(self, num_points: int):
        self.radius = 10
        self.center = Point2D(0, 0)
        self.sum_random_points = num_points
        self.points_list = []
        pass

    def __get_one_random(self) -> float:
        # uniform(a, b) a~b 之间的一个均匀分布的随机数
        return uniform(-self.radius, self.radius)

    def put_random_points(self, sum_random_points):
        for _ in range(self.sum_random_points):
            one_x = self.__get_one_random()
            one_y = self.__get_one_random()

            one_point = Point2D(one_x, one_y)
            self.points_list.append(one_point)
            self.points_list.append(one_point)

    def sum_points_in_circle(self) -> int:
        sum = 0

        for one_point in self.points_list:
            distance_to_center = one_point.distance_to(self.center)
            if distance_to_center <= self.radius:
                sum += 1

        return sum

    def get_pi_value(self) -> float:
        """
        S_circle = pi * r**2
        S_square = (2r) * (2r) = 4 * r**2
        S_circle / S_square = sum_points_in_circle / sum_random_points

        ==> S_circle = (sum_points_in_circle / sum_random_points) * S_square
        ==> pi * r**2 = (sum_points_in_circle / sum_random_points) * S_square
        ==> pi = ((sum_points_in_circle / sum_random_points) * S_square) / r**2
               = ((sum_points_in_circle / sum_random_points) * 4 * r**2) / r**2
        """
        self.put_random_points(self.sum_random_points)
        sum_points_in_circle = self.sum_points_in_circle()

        r = self.radius

        pi = ((sum_points_in_circle / self.sum_random_points) * 4 * r**2) / r**2

        return pi


if __name__ == '__main__':
    for i in range(1, 7):
        n = 1 * 10 ** i
        caculator = PiCalculator(n)
        pi = caculator.get_pi_value()
        print(f'point number {n}, pi {pi}')
    pass
