import pygame
pygame.init()

white = (225,225,225)
black = (0,0,0)
red = (225, 0, 0)

dis = pygame.display.set_mode((800,600))

pygame.display.set_caption('Zmija, okušaj se u izazovu.')

blue=(0,0,225)
red=(225,0,0)

game_over = False

x1 = 300
y1 = 300
x1_change= 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x1_change = -1
        y1_change = 0
      elif event.key == pygame.K_RIGHT:
        x1_change = 1
        y1_change = 0
      elif event.key == pygame.K_UP:
        x1_change = 0
        y1_change = -1
      elif event.key == pygame.K_DOWN:
        x1_change = 0
        y1_change = 1
  x1 += x1_change
  y1 += y1_change
  dis.fill(white)

  pygame.draw.rect(dis, black, [x1, y1, 10, 10])
  pygame.display.update()

  clock.tick(300)

pygame.quit()