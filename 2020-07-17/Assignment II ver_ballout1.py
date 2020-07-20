# File: Assignment II
# No: 6201012620082
# Date: 2020-07-17
################################################################

# Note this Python script requires PyGame.
import pygame 
from random import randint

# set window caption
pygame.display.set_caption('PyGame Assignment II') 
# create a clock
clock = pygame.time.Clock()
# Set up the drawing window (800 x 600 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))
# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# create position for input random position
pos_x = []
pos_y = []
# create size for input random radius
size_rand =[]
# create list for input color
list_color = []
count_circle = 10
#speed_x = 5
#speed_y = 4

def countnum(count_circle):
  #global speed_x, speed_y
  for i in range(count_circle):
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
    x = randint(r,scr_w-r)
    y = randint(r,scr_h-r)

    # add random in list position and size
    pos_x.append(x)
    pos_y.append(y)
    size_rand.append(r)
    list_color.append(rand_color)
    pygame.draw.circle(screen,list_color[i],(pos_x[i],pos_y[i]),size_rand[i])

    speed_x = 5
    speed_y = 4    
    pos_x[i] += speed_x
    pos_y[i] += speed_y
#########################################################################################
    if (pos_x.right and pos_y.right) >= scr_w or p(os_x.left and pos_y.left) <= 0:
      pos_x *= -1
    if (pos_x.bottom and pos_y.bottom) >= scr_h or (pos_x.top and pos_y.top) <= 0:
      pos_y *= -1
#########################################################################################
    if speed_y > 550 or speed_y < 10:
      speed_y = speed_y * -1
    if speed_x > 750 or speed_x < 10:
      speed_x = speed_x * -1

# Run until the user asks to quit
running = True
while running:
    # fill the screen with the white color
    screen.fill((255,255,255))

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mouse click
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x,mouse_y = pygame.mouse.get_pos()
        #print((mouse_x,mouse_y))
        for j in range(count_circle):
            if (pos_x[j] - 20) <= mouse_x <= (pos_x[j] + 20) and (pos_y[j] - 20)<= mouse_y <= (pos_y[j] + 20):
                pos_x[j] = -50
                pos_y[j] = -50
        
    countnum(count_circle)     
    # draw the surface on the screen
    screen.blit(surface, (0,0))
    # update the screen display
    pygame.display.update()
   
pygame.quit()

# refferance
# pygame_demo-1