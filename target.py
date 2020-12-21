import pygame
from pygame.math import Vector2

class Target:
    def __init__(self, position):
        self.position = Vector2(position) - Vector2(10,10)
        self.rectangle = pygame.Rect(*self.position, 20, 20)
        self.color_hit = (0, 205, 255)
        self.color_missed = (0, 102, 102)
        self.is_shot = False

    def get_borders(self):
        return [(self.rectangle.topleft, self.rectangle.bottomleft),
                (self.rectangle.bottomleft, self.rectangle.bottomright),
                (self.rectangle.bottomright, self.rectangle.topright),
                (self.rectangle.topright, self.rectangle.topleft)]

    def get_new_direction(self, current_direction, end_line, start_line):
        self.is_shot = True
        return current_direction

    def update(self, obstacle):
        self.is_shot = False
        return None

    def draw(self, screen):
        if self.is_shot:
            pygame.draw.rect(screen, self.color_hit, self.rectangle)
            # self.color = ((self.color[0] - self.shot) % 250, (self.color[1] + self.shot) % 250, 50)
        else:
            # self.color = (250, 250, 250)
            pygame.draw.rect(screen, self.color_missed, self.rectangle)
