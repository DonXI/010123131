################################################################
# File: Assignment I
# No: 6201012620082
# Date: 2020-07-15
################################################################

# Note this Python script requires PyGame.
import pygame 
from random import randint

# set window caption
pygame.display.set_caption('PyGame Assignment I') 

# create a clock
clock = pygame.time.Clock()

# Set up the drawing window (800 x 600 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )



# c = count circle 10
c = 10
for i in range(c):
    # random size between 10-20
    r = randint(10,20)
    # random color level between 50-255
    alpha = randint(50,255)
    #create num1, num2, num3 for randon number for color
    num1 = randint(0,255)
    num2 = randint(0,255)
    num3 = randint(0,255)
    # create a random color with alpha level between 0-225 for (RGBA) 
    rand_color = (num1,num2,num3,alpha)
    # random position (x,y)
    x,y = randint(r,scr_w-r), randint(r,scr_h-r)

    # draw a circle filled with the random color on the surface
    pygame.draw.circle(surface, rand_color,(x,y), r )


# Run until the user asks to quit
running = True
while running:

    # This limits the while loop to a max of 10 times per second.
    clock.tick( 10 ) 


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with the white color
    screen.fill((255,255,255))
    # draw the surface on the screen
    screen.blit(surface, (0,0))
    # update the screen display
    pygame.display.update()

pygame.quit()

