#!/usr/bin/python3

import pygame

# how many pixels should an object move on each tick?
from pygame.math import Vector2

from reflexionExplosive.timer import Timer
from reflexionExplosive.laser import Laser
from reflexionExplosive.obstacle import Obstacle
from reflexionExplosive.target import Target
from reflexionExplosive.player import Player

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
    screen = pygame.display.set_mode(SIZE)
    # screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    background = screen.copy()
    background.fill((0, 0, 0, 0))
    screen.blit(background, (0, 0))


init_display(800, 600)


def first_level():
    laser_objects = []
    obstacle_objects = []
    target_objects = []
    player_objects = []

    obstacle_objects.append(Obstacle(((150, 0), (150, 425), (250, 425), (250, 0))))
    obstacle_objects.append(Obstacle(((400, 0), (400, 425), (500, 425), (500, 0))))

    list_target = [(595, 80), (715, 80), (725, 215), (585, 215),
                   (290, 397), (329, 210), (372, 59), (745, 500), (470, 550)]
    for x, y in list_target:
        target_objects.append(Target((x, y)))

    player_objects.append(Player(100, 400, (255, 230, 0)))
    player_objects.append(Player(40, 400, (255, 102, 178), player2=True))

    laser_objects.append(Laser(Vector2(-10, 500), Vector2(1, 0)))

    return laser_objects, obstacle_objects, target_objects, player_objects


def second_level():
    laser_objects = []
    obstacle_objects = []
    target_objects = []
    player_objects = []

    obstacle_objects.append(Obstacle(((350, 100), (450, 100), (450, 500), (350, 500))))
    obstacle_objects.append(Obstacle(((150, 250), (650, 250), (650, 350), (150, 350))))

    laser_objects.append(Laser(Vector2(110, -10), Vector2(0, 1)))
    laser_objects.append(Laser(Vector2(690, 610), Vector2(0, -1)))

    list_target = [(250, 427), (325, 374), (495, 218), (558, 155), (49, 427), (734, 152),
                   (360, 85), (440, 85), (360, 515), (440, 515)]
    for x, y in list_target:
        target_objects.append(Target((x, y)))

    player_objects.append(Player(500, 400, (255, 230, 0)))
    player_objects.append(Player(300, 200, (255, 102, 178), player2=True))

    return laser_objects, obstacle_objects, target_objects, player_objects


def third_level():
    laser_objects = []
    obstacle_objects = []
    target_objects = []
    player_objects = []

    obstacle_objects.append(Obstacle(((0, 0), (0, 10), (800, 10), (800, 0)), reflect=True))
    obstacle_objects.append(Obstacle(((0, 600), (0, 590), (800, 590), (800, 600)), reflect=True))

    obstacle_objects.append(Obstacle(((245, 120), (290, 120), (290, 180), (245, 180))))
    obstacle_objects.append(Obstacle(((595, 400), (595, 450), (645, 450), (645, 400))))

    laser_objects.append(Laser(Vector2(-10, 300), Vector2(1, -3)))

    list_target = [(220, 145), (320, 145), (212, 516),
                   (555, 420), (685, 420)]
    for x, y in list_target:
        target_objects.append(Target((x, y)))

    player_objects.append(Player(480, 350, (255, 230, 0)))
    player_objects.append(Player(280, 280, (255, 102, 178), player2=True))

    return laser_objects, obstacle_objects, target_objects, player_objects


def fourth_level():
    laser_objects = []
    obstacle_objects = []
    target_objects = []
    player_objects = []

    obstacle_objects.append(Obstacle(((30, 0), (400, 290), (770, 0)), reflect=True))
    obstacle_objects.append(Obstacle(((30, 600), (400, 310), (770, 600)), reflect=True))

    laser_objects.append(Laser(Vector2(25, -10), Vector2(0, 1)))
    laser_objects.append(Laser(Vector2(775, -10), Vector2(0, 1)))

    list_target = [(710, 140), (710, 450), (625, 300),
                   (90, 260), (90, 325), (225, 295), ]
    for x, y in list_target:
        target_objects.append(Target((x, y)))

    player_objects.append(Player(480, 300, (255, 230, 0)))
    player_objects.append(Player(320, 300, (255, 102, 178), player2=True))

    return laser_objects, obstacle_objects, target_objects, player_objects


WHITE = (255, 255, 255)


def draw_score(screen, count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, WHITE)
    screen.blit(text, (0, 0))


def show_level(screen, level, score):
    running = True
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 100)
        text = font.render(f"Niveau {level}", True, WHITE)
        screen.blit(text, (260, 190))
        font = pygame.font.SysFont(None, 75)
        text = font.render(f"Score {score}", True, WHITE)
        screen.blit(text, (310, 260))
        font = pygame.font.SysFont(None, 50)
        text = font.render("appuyer sur espace", True, WHITE)
        screen.blit(text, (240, 330))
        pygame.display.update()
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False


def show_end(screen, score, time_total):
    running = True
    while running:
        screen.fill((0, 0, 0))
        if score <= 12:
            font = pygame.font.SysFont(None, 70)
            text = font.render(f"Meilleur chance la prochaine fois", True, WHITE)
            screen.blit(text, (10, 170))
        if score > 12:
            font = pygame.font.SysFont(None, 140)
            text = font.render(f"Félicitations!", True, WHITE)
            screen.blit(text, (80, 140))
        font = pygame.font.SysFont(None, 100)
        text = font.render(f"Score final: {score:02d}/21", True, WHITE)
        screen.blit(text, (120, 300))
        font = pygame.font.SysFont(None, 30)
        text = font.render(f"Temps restant: {time_total}", True, WHITE)
        screen.blit(text, (280, 370))
        pygame.display.update()
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_RETURN] \
                    or pygame.key.get_pressed()[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False


def show_start(screen):
    running = True
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 100)
        text = font.render(f"Réflexion explosive", True, WHITE)
        screen.blit(text, (85, 190))
        font = pygame.font.SysFont(None, 50)
        text = font.render(f"appuyer sur espace pour commencer", True, WHITE)
        screen.blit(text, (100, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False


def main():
    show_start(screen)
    level_number = 0
    level_time = 75
    score_total = 0
    time_total = 0
    score = 0
    show_level(screen, level_number + 1, score_total)
    level_list = [first_level(), second_level(), fourth_level(), third_level()]
    laser_objects, obstacle_objects, target_objects, player_objects = level_list[level_number]
    timer = Timer(level_time)

    #### Main update/draw/listen loop ####
    running = True
    while running:
        tick = clock.tick(FPS)  # Limit the framerate to FPS

        # DRAW GAME OBJECTS  # Fill entire screen.
        for x in target_objects:
            x.reset_state()

        for x in laser_objects:
            x.update(obstacle_objects + player_objects + target_objects)

        screen.fill((0, 0, 0))
        for x in laser_objects + obstacle_objects + player_objects + target_objects:
            x.draw(screen)

        count = sum([i.is_shot for i in target_objects])
        if score < count:
            score = count
        draw_score(screen, score)

        timer.update(tick)
        timer.draw(screen)

        pygame.display.update()
        # HANDLE EVENTS
        for x in player_objects:
            x.handle_keys(tick, obstacle_objects + target_objects)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

            if pygame.key.get_pressed()[pygame.K_RETURN]:
                score_total += score
                time_total += timer.total_seconde()
                level_number += 1
                score = 0
                if level_number < len(level_list):
                    show_level(screen, level_number + 1, score_total)
                    laser_objects, obstacle_objects, target_objects, player_objects = level_list[level_number]
                    timer = Timer(level_time)
                else:
                    show_end(screen, score_total, time_total)
                    return None

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(f"{pos}", end=", ")

        if timer.is_done():
            score_total += score
            score = 0
            time_total += level_time - timer.seconde
            level_number += 1
            show_level(screen, level_number, score_total)
            laser_objects, obstacle_objects, target_objects, player_objects = level_list[level_number]
            timer = Timer(level_time)


if __name__ == '__main__':
    main()
