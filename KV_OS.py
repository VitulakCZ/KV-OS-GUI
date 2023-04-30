# import
import pygame
from translate import Translator
from pygame import mixer
import sys
import time
from colorama import init, Fore, Style
		
#set title
pygame.display.set_caption('KV OS')

#Initializing Pygame modules
pygame.init()
mixer.init()


#intro
mixer.music.load("intro_sound.mp3")
mixer.music.play(1)
print(f"{Fore.GREEN}LOG:{Fore.RESET} intro zvuk")

# Initializing surface
surface = pygame.display.set_mode((800,	600))

# barvy
color = (0, 80, 200)
black = (0, 0, 0)
color_dark = (100, 100, 100)
color_light = (170, 170, 170)
green = (34,139,34)
blue = (30,144,255)
red = (255, 0, 64)

# Changing surface color
surface.fill(color)
pygame.display.flip()

# variables
X = surface.get_width()
Y = surface.get_height()

# font
bigfont = pygame.font.SysFont('Corbel', 55)
font = pygame.font.SysFont('Corbel', 35)
smallfont = pygame.font.SysFont('Corbel', 15)
jazykfont = pygame.font.SysFont('Arial', 40)

# kontrola Alt-F4, křížku nebo shutdownu
def ukonceni(events, v_hlavnim_menu):
	if events.type == pygame.QUIT or (v_hlavnim_menu and events.type == pygame.MOUSEBUTTONDOWN and shutdown.collidepoint(events.pos)):
		print(f"{Fore.GREEN}LOG:{Fore.RESET} vypnuti:menu")
		zustat = False
		while not zustat:
			# Modro
			pygame.draw.rect(surface, color, modro)
			
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
						print(f"{Fore.GREEN}LOG:{Fore.RESET} vypnuti:vypnuti{Fore.RESET}")
						pygame.quit()
						print(f"{Fore.RED}SHUTDOWN{Fore.RESET}")
						quit()
					if ne.collidepoint(events.pos):
						print(f"{Fore.GREEN}LOG:{Fore.RESET} vypnuti:zpět")
						surface.fill(color)
						zustat = True
						return True

def preklad(jazyk):
	global buttonText
	global vypnoutText
	global optionsText
	global pripravaText
	global opravduText
	global anoText
	global neText
	global zpetTextStr
	global zpetText
	global jazykZpetText
	global jazykText
	global vyberJazykaText
	
	surface.fill(color)
	pygame.display.update()
	translator = Translator(to_lang=jazyk)
	
	pripravaText = font.render('Připravujeme ...', True, green)
	pripravaRect = pripravaText.get_rect()
	pripravaRect.center = (X //	3, Y // 3)
	surface.blit(pripravaText, pripravaRect)
	pygame.display.update()
	
	buttonText = font.render(translator.translate("menu"), True, color)
	vypnoutText = font.render(translator.translate("shutdown").upper(), True, green)
	optionsText = font.render(translator.translate('options').upper(), True, green)
	opravduText = bigfont.render(translator.translate('Really?'), True, red)
	anoText = font.render(translator.translate('Yes'), True, black)
	neText = font.render(translator.translate('No'), True, black)
	zpetTextStr = translator.translate('Back')
	zpetText = font.render(zpetTextStr, True, black)
	jazykZpetText = jazykfont.render(zpetTextStr, True, black)
	jazykText = font.render(translator.translate('Language'), True, black)
	vyberJazykaText = bigfont.render(translator.translate('Change language'), True, red)
	surface.fill(color)

vybrany_jazyk = "en"
preklad(vybrany_jazyk)
# text
vypnoutRect = vypnoutText.get_rect()
vypnoutRect.center = (X	// 8, Y // 1.25)

optionsRect = optionsText.get_rect()
optionsRect.center = (X // 1.9,	Y // 1.25)

pripravaRect = pripravaText.get_rect()
pripravaRect.center = (X //	3, Y // 3)

opravduRect = opravduText.get_rect()
opravduRect.center = (X // 2, Y // 2.5)

anoRect = anoText.get_rect()
anoRect.center = (X // 2.8, Y // 1.87)

neRect = neText.get_rect()
neRect.center = (X // 1.6, Y // 1.87)

jazykRect = jazykText.get_rect()
jazykRect.center = (X // 2.6, Y // 1.87)

zpetRect = zpetText.get_rect()
zpetRect.center = (X // 1.6, Y // 1.87)

def vyber_jazyku():
	vyberJazykaRect = vyberJazykaText.get_rect()
	vyberJazykaRect.center = (X // 2, Y - 550)
	
	ceskyText = jazykfont.render("Česky", True, black)
	ceskyRect = ceskyText.get_rect()
	ceskyRect.x = 50
	ceskyRect.y = 100
	
	anglickyText = jazykfont.render("English", True, black)
	anglickyRect = ceskyText.get_rect()
	anglickyRect.x = 50
	anglickyRect.y = 150
	
	nemeckyText = jazykfont.render("Deutsch", True, black)
	nemeckyRect = nemeckyText.get_rect()
	nemeckyRect.x = 50
	nemeckyRect.y = 200
	
	spanelskyText = jazykfont.render("Español", True, black)
	spanelskyRect = spanelskyText.get_rect()
	spanelskyRect.x = 50
	spanelskyRect.y = 250
	
	ruskyText = jazykfont.render("Русский", True, black)
	ruskyRect = ruskyText.get_rect()
	ruskyRect.x = 50
	ruskyRect.y = 300
	
	jazykZpetRect = jazykZpetText.get_rect()
	jazykZpetRect.center = (X // 1.1, Y - 50)
	
	texty = {"Česky": "cs", "English": "en", "Deutsch": "de", "Español": "es", "Русский": "ru", zpetTextStr: False}
	textykeys = list(texty.keys())
	recty = [ceskyRect, anglickyRect, nemeckyRect, spanelskyRect, ruskyRect, jazykZpetRect]
	
	vybirani = True
	vybranyJazyk = None
	while vybirani:
		surface.blit(vyberJazykaText, vyberJazykaRect)
		surface.blit(ceskyText, ceskyRect)
		surface.blit(anglickyText, anglickyRect)
		surface.blit(nemeckyText, nemeckyRect)
		surface.blit(spanelskyText, spanelskyRect)
		surface.blit(ruskyText, ruskyRect)
		surface.blit(jazykZpetText, jazykZpetRect)
		
		for events in pygame.event.get():
			if events.type == pygame.MOUSEBUTTONDOWN:
				a,b = pygame.mouse.get_pos()
				for rect in enumerate(recty):
					#print(rect)
					#print(jazykfont.size(textykeys[rect[0]])[0])
					if rect[1].x <= a <= rect[1].x + jazykfont.size(textykeys[rect[0]])[0] and rect[1].y <= b <= rect[1].y + jazykfont.size(textykeys[rect[0]])[1]:
						vybranyJazyk = textykeys[rect[0]]
						break
				# Neklikl na text
				else:
					break
				
				surface.fill(color)
				return texty.get(vybranyJazyk)
			ukonceni(events, False)
		pygame.display.update()

## mainofbuttons
shutdown = pygame.Rect(75, 400, 50, 50)
options = pygame.Rect(400, 400, 50, 50)
modro = pygame.Rect(230, 200, 330, 135)
ano = pygame.Rect(230, 300, 100, 35)
ne = pygame.Rect(450, 300, 100, 35)
OK = pygame.Rect(350, 400, 50, 50)
zpet = pygame.Rect(450, 300, 100, 35)
jazyk = pygame.Rect(230, 300, 100, 35)

zustat = False
log1 = False
log2 = False

# main loop
while True:
	zustat = False
	a,b = pygame.mouse.get_pos()
	
	# text
	if not log1:
		print(f"{Fore.GREEN}LOG:{Fore.RESET} menu:text")
		log1 = True
	surface.blit(vypnoutText, vypnoutRect)
	surface.blit(optionsText, optionsRect)
	
	konec_check = False
	for events in pygame.event.get():
		# options
		if events.type == pygame.MOUSEBUTTONDOWN:
			if options.collidepoint(events.pos):
				print(f"{Fore.GREEN}LOG:{Fore.RESET} settings:menu")
				while not zustat:
					# Jazyk
					pygame.draw.rect(surface, green, jazyk)
					surface.blit(jazykText, jazykRect)
					# Zpět
					pygame.draw.rect(surface, green, zpet)
					surface.blit(zpetText, zpetRect)
					
					a,b = pygame.mouse.get_pos()
					if zpet.x <= a <= zpet.x + 100 and zpet.y <= b <= zpet.y + 35:
						pygame.draw.rect(surface, color_light, zpet)
						surface.blit(zpetText, zpetRect)
					if jazyk.x <= a <= jazyk.x + 100 and jazyk.y <= b <= jazyk.y + 35:
						pygame.draw.rect(surface, color_light, jazyk)
						surface.blit(jazykText, jazykRect)
					
					pygame.display.update()
					for events in pygame.event.get():
						if events.type == pygame.MOUSEBUTTONDOWN:
							if jazyk.collidepoint(events.pos):
								print(f"{Fore.GREEN}LOG:{Fore.RESET} settings:jazyk")
								surface.blit(pripravaText, pripravaRect)
								pygame.display.update()
								time.sleep(.3)
								surface.fill(color)
								vybrany_jazyk = vyber_jazyku()
								if not vybrany_jazyk:
									print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:zpet")
									zustat = True
									break
								print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:nacitani")
								preklad(vybrany_jazyk)
								print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:vybran")
								zustat = True
							if zpet.collidepoint(events.pos):
								print(f"{Fore.GREEN}LOG:{Fore.RESET} settings:zpet")
								surface.fill(color)
								zustat = True
						konec_check = ukonceni(events, False)
						if konec_check:
							zustat = True
		if not konec_check:
			ukonceni(events, True)
				
		if not log2:
			print(f"{Fore.GREEN}LOG:{Fore.RESET} menu:tlacitka")
			log2 = True
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
