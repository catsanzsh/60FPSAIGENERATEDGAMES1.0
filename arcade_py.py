 # Import the Pygame library
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
FPS = 60

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the ball
ball_x, ball_y = WIDTH / 2, HEIGHT / 2
ball_vel_x, ball_vel_y = 5, 5

# Set up the paddles
paddle1_x, paddle1_y = PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2
paddle2_x, paddle2_y = WIDTH - PADDLE_WIDTH * 2, HEIGHT / 2 - PADDLE_HEIGHT / 2

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= 5
    if keys[pygame.K_s]:
        paddle1_y += 5
    if keys[pygame.K_UP]:
        paddle2_y -= 5
    if keys[pygame.K_DOWN]:
        paddle2_y += 5

    # Move the ball
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Collision detection
    if ball_y < BALL_RADIUS or ball_y > HEIGHT - BALL_RADIUS:
        ball_vel_y *= -1
    if ball_x < BALL_RADIUS and paddle1_y < ball_y + BALL_RADIUS and ball_y < paddle1_y + PADDLE_HEIGHT:
        ball_vel_x *= -1
    elif ball_x < BALL_RADIUS:
        print("Player 1 wins!")
        pygame.quit()
        sys.exit()
    if ball_x > WIDTH - BALL_RADIUS and paddle2_y < ball_y + BALL_RADIUS and ball_y < paddle2_y + PADDLE_HEIGHT:
        ball_vel_x *= -1
    elif ball_x > WIDTH - BALL_RADIUS:
        print("Player 2 wins!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
 # Game loop
