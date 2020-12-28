import pygame

WHITE = (255, 255, 255)


class Timer:
    def __init__(self, secondes):
        self.minute = secondes // 60
        self.seconde = secondes % 60
        self.milliseconde = 0

    def update(self, tick):
        if tick <= 100:
            self.milliseconde -= tick
            if self.milliseconde <= 0:
                self.seconde -= 1
                self.milliseconde += 1000
            if self.seconde <= 0:
                self.minute -= 1
                self.seconde += 60
            if self.milliseconde < 0 or self.seconde < 0 or self.minute < 0:
                self.minute = 0
                self.seconde = 0
                self.milliseconde = 0

    def is_done(self):
        return self.milliseconde == 0 and self.seconde == 0 and self.minute == 0

    def draw(self, screen):
        font = pygame.font.SysFont(None, 25)
        text = font.render(f"{self.minute:02d}:{self.seconde:02d}:{self.milliseconde % 10}", True, WHITE)
        screen.blit(text, (740, 0))
