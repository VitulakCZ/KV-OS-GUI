# import
import pygame
from pygame import mixer
import sys
import time
  
# set title
pygame.display.set_caption('KV OS')
 
# Initializing Pygame modules
pygame.init()
mixer.init()


#into
#mixer.music.load("intro_sound.mp3")
#mixer.music.play(1)

# Initializing surface
surface = pygame.display.set_mode((800, 600))
screen = pygame.display.set_mode((800, 600))
sample_surface = pygame.display.set_mode((800,600))
 
# barvy
color = (0, 80, 200)
menu = (0, 0, 0)
color_dark = (100,100,100)
color_light = (170,170,170)
green = (34,139,34)
blue = (30,144,255)

# Changing surface color
surface.fill(color)
pygame.display.flip()

#variebels
width = screen.get_width()
height = screen.get_height()
running = True
X = width
Y = screen.get_height()

#font
font = pygame.font.SysFont('Corbel',35)
smallfont = pygame.font.SysFont('Corbel',15)
##render
buttonText = font.render('menu' , True , color)

#text
vypnout = font.render('SHUTDOWN', True, green)
vypnoutRect = vypnout.get_rect()
vypnoutRect.center = (X // 8, Y // 1.6)
#
optins = font.render('OPTIONS', True, green)
optinsRect = optins.get_rect()
optinsRect.center = (X // 1.9, Y // 1.6)
#
priprava = font.render('Připravujeme', True, green)
pripravaRect = priprava.get_rect()
pripravaRect.center = (X // 3, Y // 3)


#idk
font = pygame.font.SysFont('Georgia',40,bold=True)
surf = font.render('Shut Down', True, 'white')

##mainofbuttons
shutdown = pygame.Rect(75,300,50,50)
options = pygame.Rect(400,290,50,50)
OK = pygame.Rect(350,400,50,50)

#

#

#main loop

vybarveno = False
while running:
    a,b = pygame.mouse.get_pos()
    
    
    #text
    if not vybarveno:
        surface.blit(vypnout, vypnoutRect)
        surface.blit(optins, optinsRect)
    
    for events in pygame.event.get():
            
        if events.type == pygame.QUIT:
           pygame.quit()
           
        #buttons
        #shutdown
        if events.type == pygame.MOUSEBUTTONDOWN:
            if shutdown.collidepoint(events.pos):
                pygame.quit()
                quit()
        if not vybarveno:
            if shutdown.x <= a <= shutdown.x + 50 and shutdown.y <= b <= shutdown.y +50:
                pygame.draw.rect(screen,(180,180,180),shutdown )
            else:
                pygame.draw.rect(screen, (15,150,15),shutdown)
        #options
        if events.type == pygame.MOUSEBUTTONDOWN:
            if options.collidepoint(events.pos):
                surface.blit(priprava, pripravaRect)
                pygame.display.update()
                time.sleep(1.5)
                surface.fill(color)
                vybarveno = True
        if not vybarveno:
            if options.x <= a <= options.x + 50 and options.y <= b <= options.y +50:
                pygame.draw.rect(screen,(180,180,180),options )
            else:
                pygame.draw.rect(screen, (15,150,15),options)
            
    a,b = pygame.mouse.get_pos()
    #lista
    pygame.draw.rect(sample_surface, menu, pygame.Rect(00, 565, 1000, 35))
    
    #update
    pygame.display.update()
  
# Quit the GUI game
pygame.quit()
