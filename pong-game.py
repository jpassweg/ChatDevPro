import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
paddle_width, paddle_height = 10, 60
player_speed = 0
opponent_speed = 7

# Ball settings
ball_speed_x, ball_speed_y = 7, 7
ball_radius = 7

# Score
player_score = 0
opponent_score = 0
game_font = pygame.font.Font(None, 32)

# Rectangles for paddles and ball
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - paddle_height / 2, paddle_width, paddle_height)
opponent = pygame.Rect(10, SCREEN_HEIGHT / 2 - paddle_height / 2, paddle_width, paddle_height)
ball = pygame.Rect(SCREEN_WIDTH / 2 - ball_radius, SCREEN_HEIGHT / 2 - ball_radius, ball_radius * 2, ball_radius * 2)

clock = pygame.time.Clock()

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ball_speed_y *= -1
    ball_speed_x *= -1

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    if ball.left <= 0:
        player_score += 1
        ball_restart()

    if ball.right >= SCREEN_WIDTH:
        opponent_score += 1
        ball_restart()

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_restart()

    # Opponent AI
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    player_text = game_font.render(f"{player_score}", False, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT / 2))

    opponent_text = game_font.render(f"{opponent_score}", False, WHITE)
    screen.blit(opponent_text, (SCREEN_WIDTH / 2 - 32, SCREEN_HEIGHT / 2))

    pygame.display.flip()
    clock.tick(60)
