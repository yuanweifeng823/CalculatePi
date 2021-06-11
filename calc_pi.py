import sys
import math
import random


class Point2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def distance_between(p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y

        distance = math.sqrt(dx * dx + dy * dy)
        return distance

class PiCalculator(object):

    def __init__(self, num_points):
        self.radius = 1
        self.center = Point(0, 0)
        self.sum_random_points = num_points
        self.points_list = []
        pass

    def __get_one_random(self):
        return random() * self.radius * 2 - self.radius

    def put_random_points(self, sum_random_points):
        one_x = self.__get_one_random()
        one_y = self.__get_one_random()

        one_point = Point(x, y)
        self.points_list.append(one_point)

        pass

    def sum_points_in_circle(self):
        pass

    def get_pi_value(self):
        """
        / pi * r * r = S_circle
        | (r+r) * (r+r) = S_square
        \ S_circle / S_squre = sum_points_in_circle / sum_random_points

        ==> 

        S_circle = sum_points_in_circle / sum_random_points * S_squre
        pi * r * r = sum_points_in_circle / sum_random_points * S_squre
        pi = (sum_points_in_circle / sum_random_points * S_squre) / (r * r)
        pi = (sum_points_in_circle / sum_random_points * (r+r) * (r+r)) / (r * r)
        """
        put_random_points(self.sum_random_points)
        sum_points_in_circle = sum_points_in_circle()

        r = self.radius

        pi = (sum_points_in_circle / sum_random_points * (r + r) * (r+r)) / (r * r)

        return pi

if __name__ == '__main__':
    pass