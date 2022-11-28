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

#get font
font = pygame.font.Font(pygame.font.get_default_font(), 36)

###CONSTANTS 
# -- ball width
ball_width = 20

 # -- starting coordinataes of ball
x_pos = 150
y_pos = 200

# -- ball direction
x_direction = 3
y_direction = 3

#paddle coordinates
x_pos_padd = 0
y_pos_padd = 20

#paddle size
paddle_width = 15   
paddle_height = 60

#lives
lives = 5



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

    #draw paddle
    pygame.draw.rect(screen, WHITE, (x_pos_padd,y_pos_padd,paddle_width,paddle_height))

    #draw ball
    pygame.draw.rect(screen, WHITE, (x_pos,y_pos,ball_width,ball_width))

    score_text = font.render(f"Lives: {lives}", True, WHITE)

    screen.blit(
        score_text,
        (size[0] / 2 - score_text.get_width() / 2, 10),
    )

    #Position Logic of Ball
    x_pos = x_pos + x_direction
    y_pos = y_pos + y_direction

    #bounce off walls
    if x_pos >= (640 - ball_width):
        x_direction = x_direction * -1
    if y_pos >= (480 - ball_width) or y_pos <= 0:
        y_direction = y_direction * -1

    #reset pos
    if x_pos < -10:
        x_pos = 320
        y_pos = 240
        lives = lives - 1


    #collision detection
    if (x_pos <= x_pos_padd + paddle_width) and (y_pos > y_pos_padd - ball_width) and (y_pos < y_pos_padd + paddle_height):
        x_direction = x_direction * -1
        

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()