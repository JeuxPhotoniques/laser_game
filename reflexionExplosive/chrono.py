import pygame

WHITE = (255, 255, 255)


class Chrono:
    def __init__(self):
        self.minute = 0
        self.seconde = 0
        self.milliseconde = 0

    def update(self, tick):
        self.milliseconde += tick
        if self.milliseconde > 1000:
            self.seconde += 1
            self.milliseconde -= 1000
        if self.seconde > 60:
            self.minute += 1
            self.seconde -= 60

    def draw(self, screen):
        font = pygame.font.SysFont(None, 25)
        text = font.render(f"{self.minute:02d}:{self.seconde:02d}:{self.milliseconde % 10}", True, WHITE)
        screen.blit(text, (740, 0))
