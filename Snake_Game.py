import pygame
import random
import time

pygame.init()

width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Food position
food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Snake direction
direction = 'RIGHT'
change_to = direction

snake_speed = 12
clock = pygame.time.Clock()


def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render("Your Score is: " + str(len(snake_body)), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 2)
    display.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# Main function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validation of direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = change_to
    if change_to == 'DOWN' and direction != 'UP':
        direction = change_to
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = change_to
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = change_to

    # Moving snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    display.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(display, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(display, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game over
    if snake_pos[0] < 0 or snake_pos[0] > width - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > height - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    pygame.display.update()
    clock.tick(snake_speed)
