import pygame
pygame.init()

from images import *
from sounds import *

WIDTH, HEIGHT = 1100, 700

HEAD_WIDTH = 1200
HEAD_HEIGHT = 700

FPS = 40
TILE = 32
HP_TANK = 5
DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0], [0, 0]]


LEFT = pygame.K_a
RIGHT = pygame.K_d
UP = pygame.K_w
DOWN = pygame.K_s
SHOOT = pygame.K_SPACE


PLAYR_LEFT = pygame.K_LEFT
PLAYR_RIGHT = pygame.K_RIGHT
PLAYR_UP = pygame.K_UP
PLAYR_DOWN = pygame.K_DOWN
PLAYR_SHOOT = pygame.K_KP_ENTER

window = pygame.display.set_mode((HEAD_WIDTH, HEAD_HEIGHT))
clock = pygame.time.Clock()