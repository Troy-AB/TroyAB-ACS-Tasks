import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Space Invaders")

# Load the player image
player_image = pygame.image.load("player.png")

# Load the enemy image
enemy_image = pygame.image.load("enemy.png")

# Set the player starting position
player_x = 400
player_y = 550

# Set the enemy starting position
enemy_x = random.randint(0, 750)
enemy_y = 50

# Set the enemy movement speed
enemy_speed = 1

# Set the player movement speed
player_speed = 5

# Set the player's bullet speed
bullet_speed = 5

# Set the player's bullet state to "ready"
# "ready" means the bullet is not currently moving
bullet_state = "ready"

# Set the player's bullet starting position
bullet_x = 0
bullet_y = 550

# Set the player's score to 0
score = 0

# Set the font for displaying the score
font = pygame.font.Font(None, 36)

# Run the game loop
running = True
while running:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Check if the enemy has reached the edge of the screen
    if enemy_x > 750 or enemy_x < 0:
        # If the enemy has reached the edge of the screen, change its direction
        enemy_speed *= -1
        enemy_y += 20

    # Move the enemy
    enemy_x += enemy_speed

    # Draw the player on the screen
    screen.blit(player_image, (player_x, player_y))

    # Draw the enemy on the screen
    screen.blit(enemy_image, (enemy_x, enemy_y))

    # Check if the player's bullet is "firing"
    if bullet_state == "firing":
        # If the bullet is firing, draw it on the screen
        screen.blit(bullet_image, (bullet_x, bullet_y))

    # Check if the player's bullet has hit the enemy
    if bullet_y < enemy_y + 50 and bullet_y > enemy_y:
        if bullet_x > enemy_x and bullet_x < enemy_x + 50:
            # If the bullet has hit the enemy, reset the bullet and increase the player's score
            bullet_state = "ready"
            bullet_x = player_x
            bullet_y = player_y
            score += 1

    # Display the player's score on the screen
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (700, 10))

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check
