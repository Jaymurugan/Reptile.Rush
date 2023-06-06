import pygame
import random

pygame.init()

# Colors
BACKGROUND_COLOR = (23, 32, 42)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
SCORE_COLOR = (255, 255, 255)
GAME_OVER_COLOR = (255, 0, 0)

# Display settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Snake settings
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# Fonts
FONT_STYLE = pygame.font.SysFont("comicsansms", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)


def show_score(score):
    score_text = SCORE_FONT.render("Score: " + str(score), True, SCORE_COLOR)
    window.blit(score_text, [10, 10])


def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(window, SNAKE_COLOR, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])


def display_message(msg, color):
    message = FONT_STYLE.render(msg, True, color)
    window.blit(message, [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = WINDOW_WIDTH / 2
    y1 = WINDOW_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(BACKGROUND_COLOR)
            display_message("Game Over! Press C to play again or Q to quit", GAME_OVER_COLOR)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if (
            x1 >= WINDOW_WIDTH
            or x1 < 0
            or y1 >= WINDOW_HEIGHT
            or y1 < 0
        ):
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(BACKGROUND_COLOR)
        pygame.draw.rect(window, FOOD_COLOR, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Initialize the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Snake Game')

# Initialize the clock
clock = pygame.time.Clock()

# Start the game loop
game_loop()