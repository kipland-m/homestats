# create window for custom display to run on CCTV monitor

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font1 = pygame.font.Font(None, 72)
pygame.display.set_caption("lets monitor shit")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    text = font1.render("Test text", True, (155,155,155))
    screen.blit(text, (50, 50))


    pygame.display.flip()

pygame.quit()

