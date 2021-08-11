from referencia.referencia.config import TEST
from config import RED
import pygame
import random
from os import path
from itertools import cycle

from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, FNT_DIR, TEST
text_states= ['JOGO DA NAVEZINHA', 'JOGO DA NAVEZINHA']
BLINK_EVENT = pygame.USEREVENT + 0


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    #https://living-sun.com/pt/python/720691-flashing-text-in-pygame-python-text-pygame.html
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    background_rect = background.get_rect()
    clock = pygame.time.Clock()
    font= pygame.font.SysFont(None, 42)
    text_index=0 
    on_text_surface = font.render(
"JOGO DA NAVEZINHA", True, pygame.Color("green3")
)
    off_text_surface = font.render(
"JOGO DA NAVEZINHA", True,(0,0,255))
    blink_surfaces = cycle([on_text_surface, off_text_surface])
    blink_surface = next(blink_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 100)



    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = TEST
                running = False

            if event.type == BLINK_EVENT:
                blink_surface= next(blink_surfaces)

        



        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        text_rect = blink_surface.get_rect()
        text_rect.midtop = (WIDTH / 2 ,  (HEIGHT - 400))
        screen.blit(blink_surface, text_rect)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
