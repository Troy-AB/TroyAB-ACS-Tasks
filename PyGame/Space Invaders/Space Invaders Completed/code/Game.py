import pygame, sys
from player import Player
import obstacle

class Game:
    def __init__(self):
        #this is where we add sprite classes
        player_sprite = Player((screen_width / 2 , screen_height), screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()

    def create_obstacle(self):
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if columnm == 'x':
                    x = column_index * self.block_size
                    y = row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241,79,800), x, y)
                    self.blocks.add(block)
        

    def run(self):
        #update all sprite groups
        #draw all sprite groups
        self.player.update()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)

if __name__ == '__main__':
    pygame.init()

    #initialize the screeen
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60)


    