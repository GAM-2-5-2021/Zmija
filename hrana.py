import pygame
import time
import random

pygame.init()
pygame.event.get()

white = (225,225,225)
black = (0,0,0)
red = (225, 0, 0)
blue = (0, 0, 225)

dis_width = 800
dis_height = 600

game_close = 0

dis = pygame.display.set_mode((800,600))

pygame.display.set_caption('Zmija, okušaj se u izazovu.')

blue=(0,0,225)
red=(225,0,0)

game_over = False

x1 = dis_width/2
y1 = dis_height/2

snake_block = 10

x1_change= 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 20

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():
  game_over = False
  game_close = False

foodx = round (random.randrange(0, dis_width - snake_block)/ 10)*10
foody = round (random.randrange(0, dis_width - snake_block)/ 10)*10

while not game_over:
   while game_close == True:
     dis.fill(white)
     message ('Izgubio si! Za igrati opet pretisni P, a za dovršiti igru O', red)

   for event in pygame.event.get():
     if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_o:
         game_over = True
       if event.type == pygame.K_p:
         gameLoop()
     if event.type == pygame.QUIT:
       game_over = True
     if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
         x1_change = -snake_block
         y1_change = 0
       elif event.key == pygame.K_RIGHT:
         x1_change = snake_block
         y1_change = 0
       elif event.key == pygame.K_UP:
         x1_change = 0
         y1_change = -snake_block
       elif event.key == pygame.K_DOWN:
         x1_change = 0
         y1_change = snake_block

   if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
     game_over = True

   x1 += x1_change
   y1 += y1_change
   dis.fill(white)

   pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
   pygame.draw.rect(dis, black, [foody, foodx, snake_block, snake_block])
   pygame.display.update()

   if x1 == foodx and y1 == foody:
     print('+1')

   clock.tick(snake_speed)

pygame.quit()

gameLoop()