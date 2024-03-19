import pygame
import sys
from settings import *
from game_objects import Paddle, Ball, Brick
from settings import BRICK_COLORS
# from settings import PADDLE_COLOR, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED



def show_start_screen(screen):
    start_screen_running = True
    while start_screen_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start_screen_running = False

        screen.fill(BG_COLOR)  # Fill the background

        # Render the start text
        font = pygame.font.Font(None, 36)
        text = font.render('Press S to start', True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Cap the frame rate


def main():
    pygame.init()

    lives = 3
    score = 0
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Brick Breaker')

    # Show the start screen
    show_start_screen(screen)

    # Game initialization
    # Inside main function or the appropriate section of your main.py
    paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR, PADDLE_SPEED)


    # ball = Ball()  # You'll need to add parameters and define this class

    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SPEED_X, BALL_SPEED_Y, BALL_RADIUS, BALL_COLOR)
    # bricks = [Brick(x, y) for x in range() for y in range()]  # Generate bricks
    # Directly modify the ball's speed attributes
    ball.speed_x *= 0.2  # Reduce horizontal speed
    ball.speed_y *= 0.2  # Reduce vertical speed

    # Generate bricks
    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLUMNS):
            x = BRICK_OFFSET_LEFT + col * (BRICK_WIDTH + BRICK_PADDING)
            y = BRICK_OFFSET_TOP + row * (BRICK_HEIGHT + BRICK_PADDING)
            color = BRICK_COLORS[row % len(BRICK_COLORS)]  # Cycle through the colors
            brick = Brick(x, y, BRICK_WIDTH, BRICK_HEIGHT, color)
            bricks.append(brick)


    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Inside the game loop in main.py
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move("left", SCREEN_WIDTH)
        if keys[pygame.K_RIGHT]:
            paddle.move("right", SCREEN_WIDTH)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:  # This will be True for both 'Q' and 'q'
            running = False

        # Game logic
        # Move paddle, ball, check for collisions, etc.


        # Ball and paddle collision
        if ball.rect.colliderect(paddle.rect):
            ball.speed_y *= -1  # Reverse the ball's vertical direction

        # Ball and bricks collision
        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                ball.speed_y *= -1  # Reverse ball direction
                bricks.remove(brick)  # Remove the brick
                score += 10  # Increase score

        for brick in bricks:
            brick.draw(screen)

        # Inside the game loop in main.py
        screen.fill(BG_COLOR)  # Clear the screen with the background color
        paddle.draw(screen)  # Draw the paddle
        ball.move()
        print(f"Ball position: x={ball.x}, y={ball.y}")
        ball.draw(screen)  # Draw the ball
        for brick in bricks:  # Draw the bricks
            brick.draw(screen)

        lives_text = font.render(f'Lives: {lives}', True, (255, 255, 255))
        screen.blit(lives_text, (10, 10))  # Adjust position as needed

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        score_text_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))  # Adjust margins as needed
        screen.blit(score_text, score_text_rect)

        pygame.display.flip()  # Update the display

        # Inside the main game loop
        if ball.rect.bottom > SCREEN_HEIGHT:
            lives -= 1  # Lose a life
            if lives > 0:
                # Reset ball position and speed
                ball.x = SCREEN_WIDTH // 2
                ball.y = SCREEN_HEIGHT // 2
                #ball.speed_x = BALL_SPEED_X  # Assuming initial speeds are constants or variables
                #ball.speed_y = BALL_SPEED_Y
            else:
                # Handle game over (e.g., break out of the loop to end the game or show a game over screen)
                print("Game Over")  # Placeholder action
                break  # This exits the main game loop, ending the game.


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
