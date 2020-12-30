import pygame
from pygame.math import Vector2


class Obstacle:
    def __init__(self, points, reflect=False):
        self.points = points
        self.lines = []
        for i in range(len(points) - 1):
            self.lines.append((points[i], points[i + 1]))
        self.lines.append((points[-1], points[0]))
        if reflect:
            self.color = (200, 200, 200)
        else:
            self.color = (96, 96, 96)
        self.reflect = reflect

    def get_borders(self):
        return self.lines

    def get_new_direction(self, current_direction, end_line, start_line):
        if self.reflect:
            v = Vector2(end_line) - Vector2(start_line)
            n = Vector2(-v.y, v.x)
            s = current_direction.reflect(n)
            return s
        else:
            return None

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)
