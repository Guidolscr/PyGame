import pygame
import random
from os import path
WIDTH = 480
HEIGHT = 600
from config import GAME, QUIT, INIT


def end_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    pygame.mixer.init()
    background = pygame.image.load('Flying_Fox_Game/assets/img/tela_terminox.jpg').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    score_font = pygame.font.Font('Flying_Fox_Game/assets/img/PressStart2P.ttf', 28)