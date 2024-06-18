import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Snowflake class
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-50, -10)
        self.speed_y = random.randint(1, 5)
        self.size = random.randint(2, 5)
    
    def fall(self):
        self.y += self.speed_y
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snowfall Animation")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Create a list of snowflakes
snowflakes = [Snowflake() for _ in range(100)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw snowflakes
    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
