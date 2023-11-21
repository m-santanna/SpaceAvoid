import pygame
from configs import *

screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption('SpaceAvoid')

class Background(pygame.sprite.Sprite):

    def __init__(self,background_selected):
        super().__init__()

        self.image = pygame.image.load(f'SpaceAvoid/assets/backgrounds/background{background_selected}.png')
        self.width = self.image.get_width()
        self.rect = self.image.get_rect(topleft = (0,0))

