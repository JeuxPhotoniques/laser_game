import pygame
from math import cos, sin, pi, radians
from pygame.math import Vector2

import formula


class Player:
    def __init__(self, x, y, color):
        self.rotate_right = pygame.K_m
        self.rotate_left = pygame.K_n
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT
        self.up = pygame.K_UP
        self.down = pygame.K_DOWN
        self.color = color
        self.lines = []

        self.x = x
        self.y = y

        self.size = 20
        self.theta = radians(-90)

        # self.c = (
        #     round(self.x + self.size * cos(0 + self.theta), 2), round(self.y + self.size * sin(0 + self.theta), 2))
        # self.a = (round(self.x + self.size * cos(2 * pi / 3 + self.theta), 2),
        #           round(self.y + self.size * sin(2 * pi / 3 + self.theta), 2))
        # self.b = (round(self.x + self.size * cos(4 * pi / 3 + self.theta), 2),
        #           round(self.y + self.size * sin(4 * pi / 3 + self.theta), 2))
        self.c = (1, 0)
        self.b = (1, 0)
        self.a = (1, 0)
        self.triangle()

    def get_borders(self):
        return [(self.a, self.b), (self.b, self.c), (self.c, self.a)]

    def triangle(self):
        self.c = (
            round(self.x + self.size * cos(0 + self.theta), 2), round(self.y + self.size * sin(0 + self.theta), 2))
        self.a = (round(self.x + self.size * cos(2 * pi / 3 + self.theta), 2),
                  round(self.y + self.size * sin(2 * pi / 3 + self.theta), 2))
        self.b = (round(self.x + self.size * cos(4 * pi / 3 + self.theta), 2),
                  round(self.y + self.size * sin(4 * pi / 3 + self.theta), 2))

    def get_new_direction(self, current_direction, end_line, start_line):
        v = Vector2(end_line) - Vector2(start_line)
        n = Vector2(-v.y, v.x)
        s = current_direction.reflect(n)
        return s

    def handle_keys(self, tick, obstacles):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 2 * tick / 30  # distance moved in 1 frame, try changing it to 5
        rot = 2 * pi / 500 * tick / 30
        move = Vector2(0, 0)
        if key[self.down]:  # down key
            move.y += 1  # move down
        elif key[self.up]:  # up key
            move.y -= 1  # move up
        if key[self.right]:  # right key
            move.x += 1  # move right
        elif key[self.left]:  # left key
            move.x -= 1  # move left
        if move.length() > 0:
            move = move.normalize() * dist
            self.x += move.x
            self.y += move.y

        if key[self.rotate_left]:  # left key
            self.theta -= rot
        elif key[self.rotate_right]:  # left key
            self.theta += rot

        self.triangle()

        for obstacle in obstacles:
            borders = obstacle.get_borders()
            for border in borders:
                for line in self.get_borders():
                    if formula.collideLineLine(*border, *line):
                        print("collision")
                        self.x -= move.x
                        self.y -= move.y

        for border in [((0, 0), (800, 0)), ((800, 0), (800, 600)), ((800, 600), (0, 600)), ((0, 600), (0, 0))]:
            for line in self.get_borders():
                if formula.collideLineLine(*border, *line):
                    print("collision")
                    self.x -= move.x
                    self.y -= move.y

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, (self.a, self.b, self.c))
