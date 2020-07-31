################################################################
# File: drag and drop
# No: 6201012620082
# Date: 2020-07-29
################################################################
import pygame
import pygame.camera
from pygame.locals import *
import sys

def open_camera( frame_size=(640,480),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

screen_w, screen_h = 640, 480
pygame.init()
camera = open_camera()

if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)


screen = pygame.display.set_mode((screen_w, screen_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

img = None
# try to capture the next image from the camera 
img = camera.get_image()
pygame.image.save( img, 'image.jpg' ) # save image
# close the camera
camera.stop()
# Divided area
M,N = 5,5
rec_w = screen_w//M
rec_h = screen_h//N



for i in range(M):
    for j in range(N):
        # draw a green frame (tile)
        rect = (i*rec_w, j*rec_h, rec_w, rec_h)
        pygame.draw.rect(img, (0,255,0), rect,1) # create green frame in screen
        surface.blit( img, rect, rect)




def mouse_swap():
    mouse_pos = pygame.mouse.get_pos()
    pos_mdown , pos_mup = None, None
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        for i in range(M):
            for j in range(N):
                if i*rec_w <= mouse_pos[0] <= (i+1)*rec_w and j*rec_h <= mouse_pos[1] <= (j+1)*rec_h:
                    pos_mdown = [i*rec_w,j*rec_h]
                    #print(pos_mdown)
                    
    if event.type == pygame.MOUSEBUTTONUP:
        
        for i in range(M):
            for j in range(N):
                if i*rec_w <= mouse_pos[0] <= (i+1)*rec_w and j*rec_h <= mouse_pos[1] <= (j+1)*rec_h:
                    pos_mup = [i*rec_w,j*rec_h]
                    #print(pos_mup)
                    surface.blit( img, (pos_mdown[0], pos_mdown[1]), rect)
                    surface.blit( img, (pos_mup[0],pos_mup[1]), rect )
  
is_running = True 
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            is_running = False    

    # click mouse
    mouse_swap()
    
    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()



print('Done....')
#####################################
# reference
# pygame_camera_demo-1.py :RSP
