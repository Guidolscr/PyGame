import pygame
import random
from os import path
WIDTH = 480
HEIGHT = 600
from config import GAME, QUIT, INIT, IMG_DIR, FNT_DIR

def teste_screen(windown):
    clock = pygame.time.Clock()
    pygame.mixer.init()
    background = pygame.image.load(path. join(IMG_DIR , 'Infos.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(60)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
    


        windown.blit(background, background_rect)
        pygame.display.flip()

    return state
