import random

from shapes import Triangle2D
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np


class EvolvingEquilateralTriangle:

    def __init__(self, n: int = 1):
        """
        Inits the algorithm with n different random triangles, and calculates the initial fitness value of each,
        with the ideal being zero.
        :param n: Amount of triangles to be added to the algorithm
        """
        self.triangles = []
        self.fitness = []
        for i in range(n):
            t = Triangle2D.random_init()
            self.triangles.append(t)
            self.fitness.append(t.differentiation_from_equilateral())

    def evolve(self, n=100000, fitness_goal=1):
        """
        Iterates over all the triangles a maximum of n times, and each time the j-th triangle is mutated.
        If the mutation is closer to being equilateral than its "parent", it takes its place.
        If the j-th triangle already has a fitness below the fitness_goal, no mutation is performed so that the
        algorithm slowly converges and stops when all triangles fulfill the goal.
        :param n: Max amount of iterations
        :param fitness_goal: Value below which all fitness have to be
        """
        amount_total = len(self.triangles)
        finished = [0] * amount_total
        for i in range(n):
            if finished.count(1) == amount_total:
                self.final_report()
                break
            for j in range(amount_total):
                t = self.triangles[j]
                t_fitness = self.fitness[j]
                if t_fitness[j] < fitness_goal:
                    finished[j] = 1
                    continue
                t_mut = t.mutate()
                t_mut_fitness = t_mut.differentiation_from_equilateral()
                if t_mut_fitness < t_fitness:
                    self.triangles[j] = t_mut
                    self.fitness[j] = t_mut_fitness

    def final_report(self):
        """
        Prints a small summary of the final triangles, as well as plotting them via matplotlib and saving this plot to
        a file.
        """
        fig, ax = plt.subplots(dpi=1200)
        polygons = []
        for i in range(len(self.triangles)):
            t = self.triangles[i]
            print(f"Triangle:\n{t}with Fitness: {self.fitness[i]}\n")
            a, b, c = t.points
            points_to_draw = np.array([[a.x, a.y], [b.x, b.y], [c.x, c.y]])
            to_draw = Polygon(points_to_draw, color=[random.random(), random.random(), random.random()])
            polygons.append(to_draw)
        p = PatchCollection(polygons, alpha=0.25, match_original=True)
        ax.add_collection(p)
        ax.autoscale()
        plt.savefig("equilateral_triangles.svg")
        plt.show()
