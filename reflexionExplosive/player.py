import pygame
from math import cos, sin, pi, radians
from pygame.math import Vector2

from reflexionExplosive import formula


class Player:
    def __init__(self, x, y, color, angle=-90, player2=False):
        if player2:
            self.up = pygame.K_w
            self.down = pygame.K_s
            self.left = pygame.K_a
            self.right = pygame.K_d
            self.rotate_left = pygame.K_q
            self.rotate_right = pygame.K_e
        else:
            self.rotate_right = pygame.K_m
            self.rotate_left = pygame.K_n
            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN

        self.color = color

        self.x = x
        self.y = y

        self.size = 20
        self.theta = radians(angle)

        self.c = None
        self.b = None
        self.a = None
        self.triangle()

    def get_borders(self):
        return [(self.a, self.b), (self.b, self.c), (self.c, self.a)]

    def triangle(self):
        self.c = (round(self.x + self.size * cos(0 + self.theta), 2),
                  round(self.y + self.size * sin(0 + self.theta), 2))
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
        key = pygame.key.get_pressed()

        dist = 2 * tick / 30
        rot = 2 * pi / 1000 * tick / 30

        direction = Vector2(0, 0)
        if key[self.down]:
            direction.y += 1
        elif key[self.up]:
            direction.y -= 1
        if key[self.right]:
            direction.x += 1
        elif key[self.left]:
            direction.x -= 1
        if direction.length() > 0:
            direction = direction.normalize() * dist

        if direction.x != 0:
            self.x += direction.x
            self.triangle()
            if self.check_collision(obstacles):
                self.x -= direction.x
                self.triangle()

        if direction.y != 0:
            self.y += direction.y
            self.triangle()
            if self.check_collision(obstacles):
                self.y -= direction.y
                self.triangle()

        if key[self.rotate_left]:
            self.theta -= rot
            self.triangle()
            if self.check_collision(obstacles):
                self.theta += rot
                self.triangle()
        elif key[self.rotate_right]:
            self.theta += rot
            self.triangle()
            if self.check_collision(obstacles):
                self.theta -= rot
                self.triangle()

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            borders = obstacle.get_borders()
            for border in borders:
                for line in self.get_borders():
                    if formula.collideLineLine(*border, *line):
                        return True
        for border in [((0, 0), (800, 0)), ((800, 0), (800, 600)), ((800, 600), (0, 600)), ((0, 600), (0, 0))]:
            for line in self.get_borders():
                if formula.collideLineLine(*border, *line):
                    return True
        return False

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, (self.a, self.b, self.c))
