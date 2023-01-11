import pygame
import random
import math

# Global Constants

#create invader class
class invader(pygame.sprite.Sprite):
    #define the constructor for invader
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
    #class invader update
    def update(self):
        self.rect.y = self.rect.y + self.speed

#create player class
class player(pygame.sprite.Sprite):
    #define the constructor for player
    def __init__(self, color, width, height):
        #set the speed
        self.speed = 0
        #call the sprite constructor
        super().__init__()
        #create the sprite and fill it with the color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #set the position of the sprite
        self.rect = (320, 240)
    #class player update
    def update(self):
        self.rect.y = self.rect.y + self.speed
        
        #reset player position
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
PURPLE = (255,0,255)

# Initialise PyGame
pygame.init()

# Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# Title of new window/screen
pygame.display.set_caption("invader")

# Exit game flag set to false
done = False

#create a list of the invader blocks
invader_group = pygame.sprite.Group()

#create a list of all sprites
all_sprites_group = pygame.sprite.Group()

#create invaderS
number_of_invaders = 10
for x in range (number_of_invaders):
    my_invader = invader(PURPLE, 10, 10, 1)
    invader_group.add(my_invader)
    all_sprites_group.add(my_invader)
#endfor

#create the player
my_player = player(YELLOW, 10, 10)
all_sprites_group.add(my_player)



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

    #invader class update
    all_sprites_group.update()
    
    # flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()