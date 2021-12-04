import pygame
import sys


elementSize = 25
snake = [[13,13],[13,14]] # [13,13] is the head of the snake. [13,14] is the first body part of the snake
direction = 0   # 0 = up, 1 = right, 2 = down, 3 = left

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([700,700]) # 700 is the size of the gamefield

def draw():
    screen.fill((0, 102, 0))

    head = True
    for x in snake:
        coordinate = [x[0] * elementSize, x[1] * elementSize] # To identify at which point on the screen the head of the snake is. x[0] represents the x coordinate and equals 13 whereas x[1] represents the y coordinate and equals 14
        if head:
            pygame.draw.rect(screen, (0,0,0), (coordinate[0], coordinate[1], elementSize, elementSize),0) # rect is a square. (0,0,0) is the color black. coordinate[0] = x coordinate, coordinate[1] = y coordinate. elementSize = width and height of the square. 0 = square is filled out
            head = False
        else:
            pygame.draw.rect(screen, (47, 79, 79), (coordinate[0], coordinate[1], elementSize, elementSize), 0) # (47, 79, 79) is a grey color


# Main Loop
go = True # The game runs as long as the go variable is True
snakeAttachment = None
appleIndex = -1
end = False
score = 0

while go:
    for event in pygame.event.get():    # all the reactions to the different types of events like button presses are defined in the for loop
        if event.type == pygame.QUIT: sys.exit()    # If the game window gets close, the game will be closed
        if event.type == pygame.KEYDOWN:                        # the following if cases will only allow to move the snake in a certain direkction, if it is not moving in the opposite direction at the moment
            if event.key == pygame.K_UP and direction != 2:     # it is forbidden to move the snake upwards if it is moving downwards. It first have to move left or right
                direction = 0                                   # If direction is not up, the snake can be moved up (direction 0)
            if event.key == pygame.K_RIGHT and direction != 3:
                direction = 1
            if event.key == pygame.K_DOWN and direction != 0:
                direction = 2
            if event.key == pygame.K_LEFT and direction != 1:
                direction = 3

    number = len(snake) - 1
    for i in range(1, len(snake)):                  # iterate through the snake but with the starting point at the first body point directly behind the head of the snake
        snake[number] = snake[number - 1].copy()    # body parts of the snake are moved by one element to the front to the place where the penultimate element was
        number -= 1

    if direction == 0:          # if direction = 0 (up) then the y coordinate of the head should be decreased by one
        snake[0][1] -= 1
    if direction == 1:          # if direction = 1 (right) then the x coordinate of the head should be increased by one
        snake[0][0] += 1
    if direction == 2:          # if direction = 2 (down) then the y coordinate of the head should be increased by one
        snake[0][1] += 1
    if direction == 3:          # if direction = 3 (left) then the x coordinate of the head should be decreased by one
        snake[0][0] -= 1

    if end == False:            # check for colision with a wall or the snake itself
        draw()
        pygame.display.update()     # changes of the screen will be printed
    else:
        print("You achieved " + str(score) + " points")
        sys.exit()
    clock.tick(10)