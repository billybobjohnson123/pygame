# Example file showing a basic pygame "game loop"
import pygame
from liquid import Liquid

def renderRectFromLiquid(liquid, screen, color, scale):
    for l in liquid.liquidPosition:
        pygame.draw.rect(screen,color,(l[0], l[1], scale, scale))
        print(l)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1080, 780))
clock = pygame.time.Clock()
running = True
color = (0, 0, 255)
scale = 100
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
            x, y = event.pos
            liquid = Liquid(x - scale / 2, y - scale / 2, scale)
            renderRectFromLiquid(liquid, screen, color, scale)
            liquid.flow()
            renderRectFromLiquid(liquid, screen, color, scale)
            liquid.flow()
            renderRectFromLiquid(liquid, screen, color, scale)
    # RENDER YOUR GAME HERE
  
  
# Drawing Rectangle






    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



