import math
import pygame


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = round(det(d, xdiff) / div)
    y = round(det(d, ydiff) / div)

    def between(s, x, e):
        return s <= x <= e or s >= x >= e

    # if between(line1[0][0], x, line1[1][0]) and between(line2[0][0], x, line2[1][0])\
    #         and between(line1[0][1], y, line1[1][1]) and between(line2[0][1], y, line2[1][1]):
    return x, y
    # else:
    #     return None


def collideLineLine(l1_p1, l1_p2, l2_p1, l2_p2):
    # normalized direction of the lines and start of the lines
    P = pygame.math.Vector2(*l1_p1)
    line1_vec = pygame.math.Vector2(*l1_p2) - P
    R = line1_vec.normalize()
    Q = pygame.math.Vector2(*l2_p1)
    line2_vec = pygame.math.Vector2(*l2_p2) - Q
    S = line2_vec.normalize()

    # normal vectors to the lines
    RNV = pygame.math.Vector2(R[1], -R[0])
    SNV = pygame.math.Vector2(S[1], -S[0])
    RdotSVN = R.dot(SNV)
    if RdotSVN == 0:
        return False

    # distance to the intersection point
    QP = Q - P
    t = QP.dot(SNV) / RdotSVN
    u = QP.dot(RNV) / RdotSVN

    if not (t > 0 and u > 0 and t * t < line1_vec.magnitude_squared() and u * u < line2_vec.magnitude_squared()):
        return False

    return True


# a = collideLineLine((0,0),(10,0),(0,1),(10,-2))
# print(a)

def colideRectLine(rect, p1, p2):
    return (collideLineLine(p1, p2, rect.topleft, rect.bottomleft) or
            collideLineLine(p1, p2, rect.bottomleft, rect.bottomright) or
            collideLineLine(p1, p2, rect.bottomright, rect.topright) or
            collideLineLine(p1, p2, rect.topright, rect.topleft))


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
