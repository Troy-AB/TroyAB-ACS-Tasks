import pygame

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREY = (100,100,100)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    size = 10
    
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface(size, size

        )



### -- Game Loop


while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
    
    # -- Game logic goes after this comment
    
    # -- Screen background is BLACK
    screen.fill (GREY)
    
    # -- Draw here
    pygame.draw.rect(screen, WHITE, (450,150,200,20))
    pygame.draw.rect(screen, WHITE, (250,250,200,20))
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()