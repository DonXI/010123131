# File: Assignment I
# No: 6201012620082
# Date: 2020-07-24
import threading
import time
import cmath # complex number
import pygame
#from random import randint, randrange, random

print( 'File:', __file__ )


def mandelbrot(c,max_iters=50):   # max_iters is iteration
    i = 0
    z = complex(0,0)    # z start 0
    while abs(z) <= 2 and i < max_iters:
        z = z * z  + c      # f(z) = z^2 + c 
        i += 1 
    return i

# initialize pygame
pygame.init()
# create a screen of width=600 and height=400
screen_w = 600
screen_h = 400
screen = pygame.display.set_mode( (screen_w, screen_h) )
# set window caption
pygame.display.set_caption('Fractal Image : Mandelbrot') 
# create a clock
clock = pygame.time.Clock()
# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

first_create = True 
running = True
w_half, h_half = screen_w/2, screen_h/2 # half width, half screen

# set the number of threads to be created
N = 100
# create a thread lock 
lock = threading.Lock()
# create a barrier
barrier = threading.Barrier(N+1)
# create a list of semaphores 
list_semaphores = [ threading.Semaphore(0) for i in range(N) ]
# a list for keeping the thread objects
list_threads = []

def func_thread(i,surface,lock,barrier,sem):
    if sem.acquire(timeout=0.1):
        scale = 0.006
        offset = complex(-0.55,0.0)  
        # plot in x and y
        for x in range(screen_w):
            for y in range(screen_h):
                re = scale*(x-w_half) + offset.real
                im = scale*(y-h_half) + offset.imag
                c = complex( re, im )
                color = mandelbrot(c, 63)
                r = (color << 6) & 0xc0
                g = (color << 4) & 0xc0
                b = (color << 2) & 0xc0
                surface.set_at( (x, y), (255-r,255-g,255-b) )
        with lock:
            # draw a circle on the surface
            pygame.draw.circle( surface, color, (x,y), r )
        # pass the barrier
        try:
            barrier.wait()
        except threading.BrokenBarrierError:
            pass


for t in list_threads:
    t.start()

while running:
    for sem in list_semaphores:
        sem.release()
    try:
        barrier.wait()
    except threading.BrokenBarrierError:
        pass

    with lock:
        # draw the surface on the screen
        screen.blit( surface, (0,0) )


    # update the display
    pygame.display.update()

    clock.tick(1.0) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
barrier.reset()
pygame.quit()
print( 'PyGame done...')