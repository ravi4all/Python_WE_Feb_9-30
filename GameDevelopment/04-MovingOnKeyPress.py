import pygame

# Initialize pygame
# It will check 6 test cases
pygame.init()

width = 800
height = 600

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((width,height))

x = 0
y = 0

move_x = 0
move_y = 0

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            # Will quit pygame
            pygame.quit()
            # Will quit python
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 0.3
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -0.3
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 0.3
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -0.3
                move_x = 0

    screen.fill(red)

    pygame.draw.rect(screen,black,[x,y,50,60])

    x += move_x
    y += move_y

    pygame.display.update()