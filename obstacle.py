import pygame


class Obstacle:
    def __init__(self, points):
        self.points = points
        self.lines = []
        for i in range(len(points) - 1):
            self.lines.append((points[i], points[i + 1]))
        self.lines.append((points[-1], points[0]))
        self.color = (96, 96, 96)

    def get_borders(self):
        return self.lines

    def get_new_direction(self, current_direction, end_line, start_line):
        return None

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)
        # pygame.draw.rect(screen, self.color, self.rectangle)
