import pygame
pygame.init()

score = 0
start = 0
last_score = 0

WIN_HEIGHT = 600
WIN_WIDTH = 800
FPS = 60

game_active = True
ship_flying = False

VELOCITY = 2
SHIP_SIZE = 2.5
PLANET_SIZE = 1.7
MOON_SIZE = 1.7
ASTEROID_SIZE = 2

font = pygame.font.Font("SpaceAvoid/assets/font/pixelfont.ttf", 30)

sinal = False