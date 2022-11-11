import pygame

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

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


### BALL VARIABLES
# -- ball width
ball_width = 20

 # -- starting coordinataes of ball
x_pos = 150
y_pos = 200

# -- ball direction
x_direction = 2
y_direction = 2

### PADDLE VARIABLE
x_pos_padd = 0
y_pos_padd = 20







### -- Game Loop

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_pos_padd > 0:
        y_pos_padd -= 5
    #endif

    if keys[pygame.K_DOWN] and y_pos_padd < 420:
        y_pos_padd += 5
        
    #endif








    
    ### -- Game logic goes after this comment
    
    # -- Screen background is BLACK
    screen.fill (BLACK)


    ### PONG BALL
    # -- Draw here
    pygame.draw.rect(screen, WHITE, (x_pos,y_pos,ball_width,ball_width))
    
    # -- Position Logic of Ball
    x_pos = x_pos + x_direction
    y_pos = y_pos + y_direction

    if x_pos == 0 or x_pos == (640 - ball_width):
        x_direction = x_direction * -1

    if y_pos == 0 or y_pos == (480 - ball_width):
        y_direction = y_direction * -1

    ### PADDLE
    # -- Draw here
    pygame.draw.rect(screen, WHITE, (x_pos_padd,y_pos_padd,15,60))

    
















    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()