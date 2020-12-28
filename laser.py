import pygame
from pygame.math import Vector2
from copy import copy
import formula


class Laser:
    def __init__(self, position, direction, color=(51, 165, 193)):
        self.position = Vector2(position)
        self.direction = Vector2(direction).normalize()
        self.color = color
        self.length = 1000
        self.lines = [position, position]

    def update(self, obstacles):
        self.lines = [self.position]
        current_direction = self.direction
        for _ in range(30):
            # TODO::new line detection
            line = [self.lines[-1] + current_direction * 2, self.lines[-1] + current_direction * self.length]
            collision_list = []
            for obstacle in obstacles:
                borders = obstacle.get_borders()
                for border in borders:
                    if formula.collideLineLine(*border, *line):
                        point = Vector2(formula.line_intersection(border, line))
                        col = (obstacle, border, point)
                        collision_list.append(col)
            if len(collision_list) == 0:
                self.lines.append(line[-1])
                return None
            obstacle_result, border_result, point_result = min(collision_list,
                                                               key=lambda k: formula.distance(line[0], k[2]))
            self.lines.append(point_result)
            current_direction = obstacle_result.get_new_direction(current_direction, *border_result)
            if current_direction is None:
                return None

    # ancienne version qui marche
    def update_work(self, obstacles):
        self.lines = [self.position]
        current_direction = self.direction
        while True:
            current_pos = copy(self.lines[-1])
            for _ in range(self.length):
                current_pos += current_direction
                for obstacle in obstacles:
                    borders = obstacle.rectangle
                    if borders.collidepoint(current_pos):
                        self.lines.append(current_pos)
                        current_direction = self.find_new_direction(current_pos - current_direction * 2,
                                                                    current_pos + current_direction * 2,
                                                                    current_direction,
                                                                    obstacle)
                        if current_direction is None:
                            return None
                        break
                else:
                    continue
                break
            else:
                self.lines.append(current_pos - self.direction)
                break

    def find_new_direction(self, old_pos: Vector2, current_pos: Vector2, current_direction: Vector2, obstacle):
        for start_line, end_line in obstacle.get_borders():
            collision_point = formula.line_intersection((old_pos, current_pos), (start_line, end_line))
            if collision_point is not None:
                # formula.angle_of_vectors(current_direction,Vector2(start_line) - Vector2(end_line))
                return self.reflect(current_direction, end_line, start_line)
        return None

    def reflect(self, current_direction, end_line, start_line):
        v = Vector2(end_line) - Vector2(start_line)
        n = Vector2(-v.y, v.x)
        s = current_direction.reflect(n)
        return s

    def draw(self, screen):
        pygame.draw.lines(screen, self.color, False, self.lines, 3)
