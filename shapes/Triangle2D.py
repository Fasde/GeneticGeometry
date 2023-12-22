from .Shape2D import Shape2D
from .Point2D import Point2D
import random
import math
from copy import deepcopy


class Triangle2D(Shape2D):

    def __init__(self, a: Point2D, b: Point2D, c: Point2D):
        self.points = [a, b, c]

    def angles(self):
        """
        Calculates the three angles inside the two-dimensional triangle using trigonometry.
        Results are given in degree values.

        :return: alpha, beta, gamma
        """
        a, b, c, a2, b2, c2 = self.side_lengths()
        pre_alpha = math.acos((b2 + c2 - a2) / (2 * b * c))
        pre_beta = math.acos((a2 + c2 - b2) / (2 * a * c))
        pre_gamma = math.acos((a2 + b2 - c2) / (2 * a * b))

        alpha = pre_alpha * 180 / math.pi
        beta = pre_beta * 180 / math.pi
        gamma = pre_gamma * 180 / math.pi

        return alpha, beta, gamma

    def differentiation_from_equilateral(self):
        """
        Calculates the amount by how much this triangle differs from an equilateral one.
        This is done by using the angles inside the triangle, calculating each difference from the ideal value of 60,
        and then adding all three differences to a single value.
        The ideal result for an actual equilateral triangle would therefore be 0.

        :return: difference of angles from 60° each
        """
        alpha, beta, gamma = self.angles()

        diff_a = abs(60-alpha)
        diff_b = abs(60-beta)
        diff_c = abs(60-gamma)

        return diff_a + diff_b + diff_c

    def mutate(self):
        """
        Returns a mutation of the current triangle by first deepcopying the object to a new one, then choosing one of
        the three points, and picking a random new point in its place.
        Note that this algorithm works stupidly, the mutation is completely random and does not take into accord
        whether the mutation its performing is beneficial or not. A less naive implemenation would nudge the mutation
        into a "fitter" position.

        :return: mutated triangle with one mutated point
        """
        chosen_one = random.randint(0, 2)
        copy = deepcopy(self)
        copy.points[chosen_one] = Point2D.random_init()
        return copy

    def side_lengths(self):
        """
        Calculates the lengths of the three sides as well as the un-squarerooted values of each
        :return: side-lengths as well as un-squarerooted versions
        """
        ab = (self.points[0].x - self.points[1].x) ** 2 + (self.points[0].y - self.points[1].y) ** 2
        ac = (self.points[0].x - self.points[2].x) ** 2 + (self.points[0].y - self.points[2].y) ** 2
        bc = (self.points[1].x - self.points[2].x) ** 2 + (self.points[1].y - self.points[2].y) ** 2
        return math.sqrt(ab), math.sqrt(ac), math.sqrt(bc), ab, ac, bc

    @classmethod
    def random_init(cls):
        a, b, c = Point2D.random_init(), Point2D.random_init(), Point2D.random_init()
        return cls(a, b, c)

    def __str__(self):
        alpha, beta, gamma = self.angles()
        return f"a: {self.points[0]}\nb: {self.points[1]}\nc: {self.points[2]}\nalpha: {alpha}, beta: {beta}, gamma: {gamma}\n"
