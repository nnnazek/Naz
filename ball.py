import pygame
import random
#pylint: disable=no-member

pygame.init()

screen_width=600
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Red circle')


ballsurface = pygame.Surface(( 50, 50))
ballsurface.set_colorkey((0, 0, 0))

radius=25
pygame.draw.circle(ballsurface, (255,0,0), (25,25), radius)

x = 350
y = 420

clock = pygame.time.Clock()

mainloop = True

while mainloop:
    screen.fill((255,255,255))
    clock.tick(20)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            mainloop = False
    
    screen.blit(ballsurface, (x, y))
    keypressed=pygame.key.get_pressed()
    if keypressed[pygame.K_UP]:
        y-=20
    if keypressed[pygame.K_DOWN] :
        y+=20
    if keypressed[pygame.K_RIGHT] :
        x+=20
    if keypressed[pygame.K_LEFT] :
        x-=20

    if x < 0:
        x = 0
    elif x + 50 > screen_width:
        x = screen_width - 50
    if y < 0:
        y = 0
    elif y + 50 > screen_height:
        y = screen_height - 50   
                 
    pygame.display.flip()
    pygame.display.update()

pygame.quit()