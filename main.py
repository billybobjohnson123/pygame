# Example file showing a basic pygame "game loop"
import pygame
from liquid import Liquid

def renderRectFromLiquid(liquid, screen, color, scale):
    for l in liquid.liquidPosition:
        pygame.draw.rect(screen,color,(l[0], l[1], scale, scale))

# pygame setup
pygame.init()
height = 900
width = 900
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
color = (0, 0, 255)
scale = 100
objects = []


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for i in range(1, height // scale):
        pygame.draw.line(screen, (255, 255, 255), (scale * i, 0), (scale * i, width))
        pygame.draw.line(screen, (255, 255, 255), (0, scale * i), (height, scale * i))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
            x, y = event.pos
            pickedup = False
            for i in range(len(objects)):
                if objects[i].source == [(x // scale) * scale, (y // scale) * scale]:
                    objects[i].pickUp(pygame.time.get_ticks())
                    pickedup = True
            if not pickedup:
                liquid = Liquid(x, y, scale, pygame.time.get_ticks(), 3)
                objects.append(liquid)
            
            
    # RENDER YOUR GAME HERE
  
  
# Drawing Rectangle



    for obj in objects:
        obj.tick(pygame.time.get_ticks())
        renderRectFromLiquid(obj, screen, color, scale)


    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()