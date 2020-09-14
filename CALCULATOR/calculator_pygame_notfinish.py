import pygame,sys
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
SKYBLUE = (135,206,235)
ORANGE = (255,165,0)
PINK = (255,192,203)

pygame.init()

clock = pygame.time.Clock()
scr_w,scr_h = 420,600
screen = pygame.display.set_mode((scr_w,scr_h))
width, height = 80, 80

pygame.font.init() 
fonts = pygame.font.get_fonts()
text_font = pygame.font.SysFont('Leelawadeeui', 14)



def draw_rect():
# row 1
    button_AC = pygame.draw.rect(screen,RED,(20,100,width,height))
    #text_AC = create_text('AC')
    button_C = pygame.draw.rect(screen,PINK,(120,100,width,height))
    button_invert = pygame.draw.rect(screen,ORANGE,(220,100,width,height))
    button_divide = pygame.draw.rect(screen,ORANGE,(320,100,width,height))
# row 2
    button_7 = pygame.draw.rect(screen,WHITE,(20,200,width,height))
    button_8 = pygame.draw.rect(screen,WHITE,(120,200,width,height))
    button_9 = pygame.draw.rect(screen,WHITE,(220,200,width,height))
    button_multiply = pygame.draw.rect(screen,ORANGE,(320,200,width,height))
# row 3
    button_4 = pygame.draw.rect(screen,WHITE,(20,300,width,height))
    button_5 = pygame.draw.rect(screen,WHITE,(120,300,width,height))
    button_6 = pygame.draw.rect(screen,WHITE,(220,300,width,height))
    button_minus = pygame.draw.rect(screen,ORANGE,(320,300,width,height))
# row 4
    button_1 = pygame.draw.rect(screen,WHITE,(20,400,width,height))
    button_2 = pygame.draw.rect(screen,WHITE,(120,400,width,height))
    button_3 = pygame.draw.rect(screen,WHITE,(220,400,width,height))
    button_plus = pygame.draw.rect(screen,ORANGE,(320,400,width,height))
# row 5
    button_percent = pygame.draw.rect(screen,ORANGE,(20,500,width,height))
    button_0 = pygame.draw.rect(screen,WHITE,(120,500,width,height))
    button_dot = pygame.draw.rect(screen,WHITE,(220,500,width,height))
    button_equal = pygame.draw.rect(screen,SKYBLUE,(320,500,width,height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    
    draw_rect()
    pygame.display.flip()
    clock.tick(60)