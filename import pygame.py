import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game Variables
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
PLAYER_SIZE = (50, 50)
PIPE_WIDTH = 100
PIPE_GAP = 200
PIPE_DISTANCE = 300
SPEED = 5

# Initialize Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Player
player = pygame.rect.Rect((SCREEN_WIDTH / 2) - (PLAYER_SIZE[0] / 2), (SCREEN_HEIGHT / 2) - (PLAYER_SIZE[1] / 2), PLAYER_SIZE[0], PLAYER_SIZE[1])

# Pipes
pipe_list = []
for i in range(0, 2):
    pipe_height = random.randint(0, SCREEN_HEIGHT - PIPE_GAP - PIPE_DISTANCE)
    bottom_pipe = pygame.rect.Rect(SCREEN_WIDTH + i * (PIPE_WIDTH + PIPE_DISTANCE), pipe_height, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height - PIPE_GAP)
    top_pipe = pygame.rect.Rect(SCREEN_WIDTH + i * (PIPE_WIDTH + PIPE_DISTANCE), 0, PIPE_WIDTH, pipe_height - PIPE_DISTANCE)
    pipe_list.append([bottom_pipe, top_pipe])

# Game Loop
while True:
    # Fill Screen with Black
    screen.fill(BLACK)

    # Draw Pipes
    for pipe in pipe_list:
        pygame.draw.rect(screen, GREEN, pipe[0])
        pygame.draw.rect(screen, GREEN, pipe[1])

    # Draw Player
    pygame.draw.rect(screen, RED, player)

    # Update Pipes
    for pipe in pipe_list:
        pipe[0].x -= SPEED
        pipe[1].x -= SPEED

    # Update Player
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        player.y -= 10
    player.y += SPEED

    # Collision Detection
    for pipe in pipe_list:
        if (player.colliderect(pipe[0]) or player.colliderect(pipe[1])):
            pygame.quit()
            sys.exit()

    # Score
    for pipe in pipe_list:
        if pipe[0].x + PIPE_WIDTH < 0:
            pipe_list.remove(pipe)
            pipe_height = random.randint(0, SCREEN_HEIGHT - PIPE_GAP - PIPE_DISTANCE)
            bottom_pipe = pygame.rect.Rect(SCREEN_WIDTH + len(pipe_list) * (PIPE_WIDTH + PIPE_DISTANCE), pipe_height, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height - PIPE_GAP)
            top_pipe = pygame.rect.Rect(SCREEN_WIDTH + len(pipe_list) * (PIPE_WIDTH + PIPE_DISTANCE), 0, PIPE_WIDTH, pipe_height - PIPE_DISTANCE)
            pipe_list.append([bottom_pipe, top_pipe])

    # Add new pipe
    if len(pipe_list) < 2:
        pipe_height = random.randint(0, SCREEN_HEIGHT - PIPE_GAP - PIPE_DISTANCE)
        bottom_pipe = pygame.rect.Rect(SCREEN_WIDTH + len(pipe_list) * (PIPE_WIDTH + PIPE_DISTANCE), pipe_height, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height - PIPE_GAP)
        top_pipe = pygame.rect.Rect(SCREEN_WIDTH + len(pipe_list) * (PIPE_WIDTH + PIPE_DISTANCE), 0, PIPE_WIDTH, pipe_height - PIPE_DISTANCE)
        pipe_list.append([bottom_pipe, top_pipe])

    # Draw Score
    font = pygame.font.Font(None, 36)
    text = font.render(str(len(pipe_list) - 1), 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    # Update Screen
    pygame.display.flip()

    # Frame Rate
    clock.tick(30)