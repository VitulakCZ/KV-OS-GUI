# import
import pygame
from pygame import mixer
import sys
import time
		
#set title
pygame.display.set_caption('KV OS')

#Initializing Pygame modules
pygame.init()
mixer.init()


#into
mixer.music.load("intro_sound.mp3")
mixer.music.play(1)

# Initializing surface
surface = pygame.display.set_mode((800,	600))

# barvy
color = (0, 80, 200)
black = (0, 0, 0)
color_dark = (100, 100, 100)
color_light = (170, 170, 170)
green = (34,139,34)
blue = (30,144,255)

# Changing surface color
surface.fill(color)
pygame.display.flip()

# variables
width =	surface.get_width()
height = surface.get_height()
running	= True
X = width
Y = surface.get_height()

# font
bigfont = pygame.font.SysFont('Corbel', 55)
font = pygame.font.SysFont('Corbel', 35)
smallfont = pygame.font.SysFont('Corbel', 15)
## render
buttonText = font.render('menu', True, color)

# text
vypnoutText = font.render('SHUTDOWN', True, green)
vypnoutRect = vypnoutText.get_rect()
vypnoutRect.center = (X	// 8, Y // 1.25)

optionsText = font.render('OPTIONS', True, green)
optionsRect = optionsText.get_rect()
optionsRect.center = (X // 1.9,	Y // 1.25)

pripravaText = font.render('Připravujeme', True, green)
pripravaRect = pripravaText.get_rect()
pripravaRect.center = (X //	3, Y // 3)

opravduText = bigfont.render('Opravdu?', True, (255, 0, 64))
opravduRect = opravduText.get_rect()
opravduRect.center = (X // 2, Y // 2.5)

anoText = font.render('Ano', True, (64, 0, 64))
anoRect = opravduText.get_rect()
anoRect.center = (X // 2.35, Y // 1.85)

neText = font.render('Ne', True, (64, 0, 64))
neRect = opravduText.get_rect()
neRect.center = (X // 1.4, Y // 1.85)

# idk
font = pygame.font.SysFont('Georgia', 40, bold=True)
surf = font.render('Shut Down', True, 'white')

## mainofbuttons
shutdown = pygame.Rect(75, 400, 50, 50)
options = pygame.Rect(400, 400, 50, 50)
ano = pygame.Rect(230, 300, 100, 35)
ne = pygame.Rect(450, 300, 100, 35)
OK = pygame.Rect(350, 400, 50, 50)

#

#

vybarveno = False

# main loop
while running:
	a,b = pygame.mouse.get_pos()
	
	# text
	if not vybarveno:
		surface.blit(vypnoutText, vypnoutRect)
		surface.blit(optionsText, optionsRect)
	
	for events in pygame.event.get():
		if events.type == pygame.QUIT or (events.type == pygame.MOUSEBUTTONDOWN and shutdown.collidepoint(events.pos)):
			zustat = False
			while not zustat:
				surface.blit(opravduText, opravduRect)
				# Ano
				pygame.draw.rect(surface, green, ano)
				surface.blit(anoText, anoRect)
				# Ne
				pygame.draw.rect(surface, green, ne)
				surface.blit(neText, neRect)
				
				a,b = pygame.mouse.get_pos()
				if ano.x <= a <= ano.x + 100 and ano.y <= b <= ano.y + 35:
					pygame.draw.rect(surface, color_light, ano)
					surface.blit(anoText, anoRect)
				if ne.x <= a <= ne.x + 100 and ne.y <= b <= ne.y + 35:
					pygame.draw.rect(surface, color_light, ne)
					surface.blit(neText, neRect)
					
				pygame.display.update()
				for events in pygame.event.get():
					if events.type == pygame.MOUSEBUTTONDOWN:
						if ano.collidepoint(events.pos):
							pygame.quit()
						if ne.collidepoint(events.pos):
							surface.fill(color)
							zustat = True
		# options
		if events.type == pygame.MOUSEBUTTONDOWN:
			if options.collidepoint(events.pos):
				surface.blit(pripravaText, pripravaRect)
				pygame.display.update()
				time.sleep(1.5)
				surface.fill(color)
				vybarveno = True
		
		if not vybarveno:
			if shutdown.x <= a <= shutdown.x + 50 and shutdown.y <=	b <= shutdown.y	+ 50:
				pygame.draw.rect(surface, color_light, shutdown)
			else:
				pygame.draw.rect(surface, (15,150,15), shutdown)
			
			if options.x <= a <= options.x + 50 and options.y <= b <= options.y + 50:
				pygame.draw.rect(surface, color_light, options)
			else:
				pygame.draw.rect(surface, (15,150,15), options)
			
	# lista
	pygame.draw.rect(surface, black, pygame.Rect(0, 565, 1000, 35))
	
	# update
	pygame.display.update()
	
# Quit the GUI game
pygame.quit()
