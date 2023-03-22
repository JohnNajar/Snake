import pygame
import sys
import time
import random

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initializing pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game')
windowX = 720
windowY = 480
game_window = pygame.display.set_mode((720, 480))

# FPS controller
fps_controller = pygame.time.Clock()

score = 0
# Snake starting position
snakePos = [100, 100]
# Setting food at random position in the range of the window
foodPos = [random.randrange(1, (windowX // 10)) * 10, random.randrange(1, (windowY // 10)) * 10]

# Prints text on the screen
def message(text, fontColor, fontSize, position):
    font = pygame.font.SysFont('times new roman', fontSize)
    msg = font.render(text, True, fontColor)
    if position == "topleft":
        game_window.blit(msg, [30, 10])
    elif position == "topright":
        game_window.blit(msg, [650, 10])
    elif position == "center":
        game_window.blit(msg, [windowX/2, windowY/2.25])


def score():
    # This function should display the score on the screen and keeps track of it as the snake eats the apples
    return ""


def gameOver(message="", color=None, event=None):
    # This function should be called when the snake hits the edges of the screen
    # It also has to be called when the player wins or hits a certain score
    # It will display a message on the screen it will take in a string, and color
    # Needs to check if the player pressed Enter or Q
    return ""


def snake():
    # This function should set up the snake body size
    # Also it has to take in value to set the position of the snake on the screen while the main loop runs
    # It have to store the current position of the snake in snakePos, so it can be used to track the snake
    return ""


def moveSnake(event):
    # This function should take input from the users keyboard to move the snake up,down,left,right
    # It also have to move the snake depending on the input
    # I am passing the event on line 83 in a loop
    # These two examples are used to get the user key input
    # use example event.type == pygame.
    # another use example event.key == pygame
    return ""


def mainLoop(over=False, lost=False):
    while not over:

        while lost:
            pygame.display.update()
            game_window.fill(blue)
            gameOver(message="You Lost! Press Enter to Play Again or Q-Quit", color=red)
            score()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    gameOver(event=event)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                moveSnake(event)

        # Updates the display
        pygame.display.update()

        # This is the games fps it decides the snakes speed
        fps_controller.tick(25)


if __name__ == '__main__':
    mainLoop()
