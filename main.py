import pygame
from sys import exit
from configs import *
from background import *
from spaceship import Spaceship
from random import choice, randint
from obstacle import *


pygame.init()
clock = pygame.time.Clock()

spaceship = pygame.sprite.GroupSingle()
spaceship.add(Spaceship(choice([1,2,3,4])))

obstacles = pygame.sprite.Group()
planet_timer = pygame.USEREVENT + 1
moon_timer = pygame.USEREVENT + 2
asteroid_timer = pygame.USEREVENT + 3

pygame.time.set_timer(planet_timer,3000)
pygame.time.set_timer(moon_timer,2400)
pygame.time.set_timer(asteroid_timer,1800) 

background = pygame.sprite.GroupSingle()
background.add(Background(choice([1,2,3,4,5,6])))


def score_counter():
    if ship_flying:
        score = (pygame.time.get_ticks() - start) // 1000
    else:
        score = 0
    return score

def display_score(score_x):

    score_surf = font.render(f'Score: {score_x}',False,'white')
    score_rect = score_surf.get_rect(midtop = (WIN_WIDTH / 2,WIN_HEIGHT / 10))
    screen.blit(score_surf,score_rect)


def check_planecollision():
    game_running = True
    for obs in obstacles:
        if pygame.sprite.collide_mask(spaceship.sprite,obs):
            game_running = False
        if spaceship.sprite.rect.top <= -10:
            game_running = False
        if spaceship.sprite.rect.bottom >= WIN_HEIGHT + 10:
            game_running = False  
    return game_running

while True:

    keys = pygame.key.get_pressed()
    clock.tick(FPS)
    current_score = score_counter()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()            

        if event.type == planet_timer and ship_flying:
      
                pos_spawn_planet = randint(0,490)
                planet = Planet(pos_spawn_planet, 'planet' + str(randint(1, 12)))
                obstacles.add(planet)
               

        if event.type == moon_timer and ship_flying:
 
                pos_spawn_moon = randint(0,540)
                moon = Moon(pos_spawn_moon, 'moon' + str(randint(1, 4)))  
                obstacles.add(moon)


        if event.type == asteroid_timer and ship_flying:
         
                pos_spawn_asteroid = randint(0,550)
                asteroid = Asteroid(pos_spawn_asteroid, 'asteroid' + str(randint(1, 4)))    
                obstacles.add(asteroid)
                    

    if game_active:
        
        background.draw(screen)
        obstacles.draw(screen)
        spaceship.draw(screen)
        display_score(current_score)
        
        if ship_flying:
            
            display_score(current_score)
            obstacles.update()
            spaceship.update()
            score_counter()
            last_score = current_score
            game_active = check_planecollision()
            
        else:
            if keys[pygame.K_SPACE]:
                ship_flying = True

    else:
        if keys[pygame.K_LCTRL]:
            start = pygame.time.get_ticks()
            game_active = True
            ship_flying = False            
            obstacles.empty()            
            spaceship.empty(), spaceship.add(Spaceship(choice([1,2,3,4])))
            background.empty(), background.add(Background(choice([1,2,3,4,5,6])))
            VELOCITY = 2

        screen.fill('Black')
        restart_text = font.render('Press LCTRL to Restart', False, 'white')
        restart_text_rect = restart_text.get_rect(midtop = (WIN_WIDTH/2, WIN_HEIGHT/2))
        last_score_text = font.render(f'Score = {last_score}', False, 'white')
        last_score_text_rect = last_score_text.get_rect(midtop = (WIN_WIDTH/2, WIN_HEIGHT/3))
        screen.blit(last_score_text,last_score_text_rect)
        screen.blit(restart_text,restart_text_rect)
    
    pygame.display.update()
