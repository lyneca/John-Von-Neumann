import pygame
from constants import *
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
		if event.type == pygame.QUIT:
			done = True
pygame.quit()