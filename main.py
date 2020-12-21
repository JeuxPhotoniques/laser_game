#!/usr/bin/python3
import formula

import pygame

# how many pixels should an object move on each tick?
from pygame.math import Vector2

from laser import Laser
from obstacle import Obstacle
from target import Target
from player import Player
from timer import Timer

ANIM_SPEED = 1
# limit frame rate to FPS with clock.tick(FPS) in your main loop.
FPS = 60
# go fullscreen on 'f' keypress.
FULLSCREEN_DIM = (1366, 768)
# prepend log statements with 'if VERBOSE == True:' and quickly toggle it on/off for debugging.
VERBOSE = True

clock = pygame.time.Clock()
pygame.init()


def init_display(WIDTH, HEIGHT):
    global screen, background
    SIZE = WIDTH, HEIGHT
    if WIDTH <= 800:
        screen = pygame.display.set_mode(SIZE)
    if WIDTH > 800:
        screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    background = screen.copy()
    background.fill((0, 0, 0, 0))
    screen.blit(background, (0, 0))


init_display(800, 600)


def first_level():
    animated_objects = []
    obstacle_objects = []
    target_objects = []
    player_objects = []

    obstacle_objects.append(Obstacle(((150, 0), (150, 425), (250, 425), (250, 0))))
    obstacle_objects.append(Obstacle(((400, 0), (400, 425), (500, 425), (500, 0))))

    list_target = [(595, 80), (715, 80), (725, 215), (585, 215),
                   (290, 397), (329, 210), (372, 59), (745, 500), (470, 550)]
    for x, y in list_target:
        target_objects.append(Target((x, y)))

    player_objects.append(Player(40, 400, (255, 230, 0)))
    player_objects.append(Player(100, 400, (255, 102, 178)))

    p = player_objects[1]
    p.up = pygame.K_w
    p.down = pygame.K_s
    p.left = pygame.K_a
    p.right = pygame.K_d
    p.rotate_left = pygame.K_q
    p.rotate_right = pygame.K_e

    animated_objects.append(Laser(Vector2(-10, 500), Vector2(1, 0)))

    return animated_objects, obstacle_objects, target_objects, player_objects


WHITE = (255, 255, 255)


def score(screen, count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, WHITE)
    screen.blit(text, (0, 0))


def main():
    # create_laser()
    # create_obstacles()
    animated_objects, obstacle_objects, target_objects, player_objects = first_level()
    timer = Timer()

    #### Main update/draw/listen loop ####
    running = True
    while running:
        tick = clock.tick(FPS)  # Limit the framerate to FPS

        # DRAW GAME OBJECTS
        screen.fill((0, 0, 0))  # Fill entire screen.

        for x in target_objects + animated_objects:
            x.update(obstacle_objects + player_objects + target_objects)

        for x in animated_objects + obstacle_objects + player_objects + target_objects:
            x.draw(screen)

        count = sum([i.is_shot for i in target_objects])
        score(screen, count)

        timer.update(tick)
        timer.draw(screen)

        pygame.display.update()
        # HANDLE EVENTS
        for x in player_objects:
            x.handle_keys(tick, obstacle_objects + target_objects)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(f"{pos}", end=", ")

        if count > 4:
            while running:
                font = pygame.font.SysFont(None, 50)
                text = font.render("Winner!", True, WHITE)
                screen.blit(text, (350, 280))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        running = False
                pygame.display.update()


if __name__ == '__main__':
    main()
