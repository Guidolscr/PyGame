from config import RED
import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, FNT_DIR
text_states= ['JOGO DA NAVEZINHA, JOGO DA NAVEZINHA']

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    background_rect = background.get_rect()
    clock = pygame.time.Clock()
    font= pygame.font.SysFont(None, 16)
    text_index=0 



    running = True
    while text_index < len(text_states) and running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        if text_index < len(text_states):
            text = text_states[text_index]
        else:
            text= ''
            text_image = font.render(text, True, RED)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
