import pygame
from configs import *


class Spaceship(pygame.sprite.Sprite):

    def __init__(self,ship_chosen):
        super().__init__()

        self.gravity = 0
        self.image_original = pygame.image.load(f'SpaceAvoid/assets/spaceship/spaceship{ship_chosen}.png').convert_alpha()
        self.images = [pygame.transform.rotozoom(self.image_original,45,SHIP_SIZE),
        pygame.transform.rotozoom(self.image_original,135,SHIP_SIZE)]
        self.image = self.images[0]
        self.rect = self.image.get_rect(midleft = (30,WIN_HEIGHT/2))
        self.mask = pygame.mask.from_surface(self.image)


    def ship_moviment(self):

        keys = pygame.key.get_pressed()
        
        self.rect.y += self.gravity
        self.image = self.images[0]
        self.gravity = VELOCITY*3
        self.mask = pygame.mask.from_surface(self.image)


    
        if keys[pygame.K_SPACE]:

            self.image = self.images[1]
            self.gravity = -VELOCITY*2
            self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.ship_moviment()