import pygame

pygame.init()
windows = pygame.display.set_mode((1200,800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()