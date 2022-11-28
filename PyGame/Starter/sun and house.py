import pygame

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,165,0)

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


### -- Game Loop

x_coordinate = 0
y_coordinate = 0
i = 0

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
    
    # -- Game logic goes after this comment
    
    # -- Screen background is BLACK
    screen.fill (BLACK)
    
    # -- Draw here
    
    pygame.draw.rect(screen, BLUE, (220,350,200,150))
    pygame.draw.circle(screen, YELLOW, (x_coordinate,int(((3/1280)*(x_coordinate - 320)**2 ))), 50, 0)
        #sun((x,y),circle_width, infill) 

        # y = 1/1280(x-320)^2

    x_coordinate += 1

    if x_coordinate > 640:
        x_coordinate = 0
        
    



    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()