import pygame


def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))


def get_key(key_name):
    ans = False
    for event in pygame.event.get():
        pass

    key_input = pygame.key.get_pressed()
    key = getattr(pygame, f"K_{key_name}")

    if key_input[key]:
        ans = True
    pygame.display.update()

    return ans
