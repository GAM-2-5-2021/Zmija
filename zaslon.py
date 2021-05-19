import pygame
pygame.init()
dis = pygame.display.set_mode((600,300))
pygame.display.update()
pygame.display.set_caption('Zmija, okušaj se u izazovu.')
game_over = false
while not game_over:
  for event in pygame.event.get():
    print(event)

pygame.qiuit()
quit()