import pygame
import random
import math

# Global Constants

#create Sprite class
class snow(pygame.sprite.Sprite):
    #define the constructor for Snow
    def __init__(self, color, width, height, speed):
        #set the speed
        self.speed = random.randrange(speed,speed + 2)
        #call the sprite constructor
        super().__init__()
        #create the sprite and fill it with the color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
    #class snow update
    def update(self):
        self.rect.y = self.rect.y + self.speed
        
        #reset snow position
        if self.rect.y == 480:
            self.rect.y = 0
            self.rect.x = random.randrange(0, 640)
    

    #endprocedure
#endclass

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# Initialise PyGame
pygame.init()

# Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# Title of new window/screen
pygame.display.set_caption("Snow")

# Exit game flag set to false
done = False

#create a list of hte snow blocks
snow_group = pygame.sprite.Group()

#create a list of all sprites
all_sprites_group = pygame.sprite.Group()

#create snowflakes
number_of_flakes = 100
for x in range (number_of_flakes):
    my_snow = snow(WHITE, 3, 3, 1)
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)
#endfor

# Manages how fast screen refreshes
clock = pygame.time.Clock()



### Game Loop

while not done:
    # User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
    
    ### Game logic goes after this comment

    # Screen background is BLACK
    screen.fill (BLACK)
    
    # Draw here
    all_sprites_group.draw(screen)

    #snow class update
    all_sprites_group.update()
    
    # flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()