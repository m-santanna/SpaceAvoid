import pygame
from configs import *

class Planet(pygame.sprite.Sprite):

    def __init__(self,posY_spawn,obstacle):
        super().__init__()
        self.image = pygame.image.load(f'SpaceAvoid/assets/obstacles/{obstacle}.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0,PLANET_SIZE).convert_alpha()
        self.rect = self.image.get_rect(topleft = (WIN_WIDTH,posY_spawn))
        self.mask = pygame.mask.from_surface(self.image)
        self.height = self.image.get_height()
        
    def planet_movement(self):
        self.rect.x -= VELOCITY


    def update(self):
        self.planet_movement()
        if self.rect.right <= -100:
            self.kill()


class Moon(pygame.sprite.Sprite):

    def __init__(self,posY_spawn,obstacle):
        super().__init__()
        self.image = pygame.image.load(f'SpaceAvoid/assets/obstacles/{obstacle}.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0,MOON_SIZE).convert_alpha()
        self.rect = self.image.get_rect(topleft = (WIN_WIDTH,posY_spawn))
        self.mask = pygame.mask.from_surface(self.image)
        self.height = self.image.get_height()

    def moon_movement(self):
        self.rect.x -= VELOCITY


    def update(self):
        self.moon_movement()
        if self.rect.right <= -50:
            self.kill()


class Asteroid(pygame.sprite.Sprite):

    def __init__(self,posY_spawn,obstacle):
        super().__init__()
        self.image = pygame.image.load(f'SpaceAvoid/assets/obstacles/{obstacle}.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0,ASTEROID_SIZE).convert_alpha()
        self.rect = self.image.get_rect(topleft = (WIN_WIDTH,posY_spawn))
        self.mask = pygame.mask.from_surface(self.image)
        self.height = self.image.get_height()

    def asteroid_movement(self):
        self.rect.x -= VELOCITY


    def update(self):
        self.asteroid_movement()
        if self.rect.right <= -50:
            self.kill()