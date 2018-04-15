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

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            # Will quit pygame
            pygame.quit()
            # Will quit python
            quit()

    screen.fill(red)

    pygame.draw.rect(screen,black,[x,y,50,60])

    x += 0.1
    y += 0.3

    pygame.display.update()