import pygame
import random

# FUNCTIONS
def move(position: list, direction: list):
    x,y = position
    return [x+direction[0]*40, y+direction[1]*40]

def renderSnake(head: pygame.Rect, pos: list):
    pygame.draw.rect(SCREEN, BLUE, head)

def renderFood():
    pygame.draw.rect()

# CONSTANTS
SIZE = (900, 760)
FPS = 60
DARK_GREEN = pygame.Color(26, 42, 39)
BG_GREEN = pygame.Color(141, 167, 60)
BLUE = pygame.Color(22, 30, 45)
UNIT = 40

# PLAYER POSITION
position =[int(SIZE[0]/2), int(SIZE[1]/2)]
moved = 0

direction = [1, 0]

running = True

pygame.init()
SCREEN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MOVEMENT
        if event.type == pygame.KEYDOWN:
            # UP
            if event.key == pygame.K_UP and direction != [0, 1]:
                direction = [0, -1]
            # DOWN
            if event.key == pygame.K_DOWN and direction != [0, -1]:
                direction = [0, 1]
            # LEFT
            if event.key == pygame.K_LEFT and direction != [1, 0]:
                direction = [-1, 0]
            # RIGHT
            if event.key == pygame.K_RIGHT and direction != [-1, 0]:
                direction = [1, 0]
        
    head = pygame.Rect((position[0], position[1]), (UNIT, UNIT))
    food = pygame.Rect(())

    #RENDERING
    SCREEN.fill(BG_GREEN)           #background
    renderSnake(head, (position[0], position[1]))
    position = move(position, direction)

    pygame.time.delay(100)

    pygame.display.flip()
    clock.tick(FPS)

