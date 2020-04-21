#!/usr/bin/python3.7

import pygame
import pong

pygame.init()
pygame.key.set_repeat(40)
pygame.display.set_caption('ping-pong')

clock = pygame.time.Clock()

game = pong.Pong()

while True:
    # handle events
    game.events()
    
    # update game
    game.update()

    # render game
    game.render()
        
    clock.tick(pong.Pong.FPS)

quit()
