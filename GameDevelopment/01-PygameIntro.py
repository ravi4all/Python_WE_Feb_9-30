import pygame

# Initialize pygame
# It will check 6 test cases
pygame.init()

width = 800
height = 600

red = 255,0,0

screen = pygame.display.set_mode((width,height))

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            # Will quit pygame
            pygame.quit()
            # Will quit python
            quit()

    screen.fill(red)

    pygame.display.update()