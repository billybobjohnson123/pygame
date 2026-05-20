# Example file showing a basic pygame "game loop"
import pygame
from liquid import Liquid
from block import Block

def renderRectFromLiquid(liquid, screen, sourceColor, liquidColor, scale):
    pygame.draw.rect(screen, sourceColor,(liquid.source[0], liquid.source[1], scale, scale))
    for l in liquid.liquidPosition:
        if l != liquid.source:
            pygame.draw.rect(screen,liquidColor,(l[0], l[1], scale, scale))
def renderRectFromBlock(blocks, screen, color, scale):
    for b in blocks:
        pygame.draw.rect(screen, color, (b.x, b.y,scale, scale))

# pygame setup
pygame.init()
sourceColor =  (128, 0, 128)
height = 900
width = 900
screen = pygame.display.set_mode((width, height))
backround = pygame.surface.Surface((width, height))
clock = pygame.time.Clock()
running = True
color = (0, 0, 255)
scale = 100
objects = []
backround.fill((0,0,0))
blocks = []

while running:
    screen.blit(backround, (0,0))
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for i in range(1, height // scale):
        pygame.draw.line(screen, (255, 255, 255), (scale * i, 0), (scale * i, width))
        pygame.draw.line(screen, (255, 255, 255), (0, scale * i), (height, scale * i))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: 
            x, y = event.pos
            pickedup = False
            for i in range(len(objects)):
                if objects[i].source == [(x // scale) * scale, (y // scale) * scale]:
                    objects[i].pickUp(pygame.time.get_ticks())
                    pickedup = True
            if not pickedup:
                liquid = Liquid(x, y, scale, pygame.time.get_ticks(), 20)
                objects.append(liquid)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            x, y = event.pos
            block = Block(x, y, scale, (0, 0, 0))
            blocks.append(block)
            
    # RENDER YOUR GAME HERE
  
  
# Drawing Rectangle



    for obj in objects:
        obj.tick(pygame.time.get_ticks(), blocks)
        renderRectFromLiquid(obj, screen, sourceColor, color, scale)
    renderRectFromBlock(blocks, screen, (255, 255, 255), scale)
            
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()