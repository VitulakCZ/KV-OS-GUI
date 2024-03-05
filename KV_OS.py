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
smallfont = pygame.font.SysFont('Corbel', 30)
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
	global vyberJazykaTextStr
	global vyberJazykaText
	global hryTextStr
	global hryText
	global okText
	global texthryText
	global exceptText
	global hryKarta
	global hryTextKarta

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
	hryTextStr = translator.translate('Games')
	hryText = font.render(hryTextStr.upper(), True, green)
	okText = font.render(translator.translate('OK'), True, green)
	exceptText = font.render(translator.translate('File not found!'), True, red)
	zpetTextStr = translator.translate('Quit')
	zpetText = font.render(zpetTextStr, True, black)
	jazykZpetText = jazykfont.render(zpetTextStr, True, black)
	jazykText = font.render(translator.translate('Language'), True, black)
	vyberJazykaTextStr = translator.translate('Change language')
	vyberJazykaText = bigfont.render(vyberJazykaTextStr, True, red)
	texthryText = font.render(translator.translate('write name of game you want to run without .py'), True, green)
	# Přeložení Games karty
	hryKarta = pygame.Rect(20, 565, smallfont.size(hryTextStr)[0], 35)
	hryTextKarta = smallfont.render(hryTextStr, True, (0, 0, 255))
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

hryRect = hryText.get_rect()
hryRect.center = (X // 2.8, Y // 1.87)

input_rect = pygame.Rect(200, 200, 140, 32)

okRect = okText.get_rect()
okRect.center = (X // 2, Y // 2.80)

texthryRect = texthryText.get_rect()
texthryRect.center = (X // 2, Y // 3.30)

exceptRect = exceptText.get_rect()
exceptRect.center = (X // 2, Y // 2.30)

hryKarta = pygame.Rect(20, 565, smallfont.size(hryTextStr)[0], 35)
hryTextKarta = smallfont.render(hryTextStr, True, (0, 0, 255))
hryRectKarta = hryTextKarta.get_rect()
hryRectKarta.x = 20
hryRectKarta.y = Y- 27

hryKartaBool = False
vyberJazykaKartaBool = False
def vyber_jazyku():
	global hryKarta
	global vyberJazykaTextKarta
	global vyberJazykaRectKarta
	global vyberJazykaKarta
	global vyberJazykaKartaBool

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
	jazykZpetRect.center = (X // 1.1, Y - 75)

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
		#lista
		pygame.draw.rect(surface, black, pygame.Rect(0, 565, 1000, 35))

		vyberJazykaTextKarta = smallfont.render(vyberJazykaTextStr, True, (0, 0, 255))
		vyberJazykaRectKarta = vyberJazykaTextKarta.get_rect()
		vyberJazykaRectKarta.x = 20
		vyberJazykaRectKarta.y = Y - 27
		vyberJazykaKartaX = smallfont.size(vyberJazykaTextStr)[0]
		vyberJazykaKarta = pygame.Rect(20, 565, smallfont.size(vyberJazykaTextStr)[0], 35)
		pygame.draw.rect(surface, color_light, vyberJazykaKarta)
		surface.blit(vyberJazykaTextKarta, vyberJazykaRectKarta)

		if hryKartaBool:
			hryKarta = pygame.Rect(smallfont.size(vyberJazykaTextStr)[0] + 22, 565, smallfont.size(hryTextStr)[0] + 17, 35)
			hryRectKarta.x = smallfont.size(vyberJazykaTextStr)[0] + 30
			pygame.draw.rect(surface, color_dark, hryKarta)
			surface.blit(hryTextKarta, hryRectKarta)
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.MOUSEBUTTONDOWN:
				if vyberJazykaKarta.collidepoint(events.pos):
					surface.fill(color)
					vyberJazykaKartaBool = True
					print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:minimalizovat")
					vybirani = False
					break
				if vyberJazykaKartaBool and hryKartaBool:
					vybirani = not karta(events, False)
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
OK = pygame.Rect(50, 400, 50, 50)
zpet = pygame.Rect(450, 300, 100, 35)
jazyk = pygame.Rect(230, 300, 100, 35)
hry = pygame.Rect(230, 300, 100, 35)

zustat = False
log1 = False
log2 = False
active = False

def settings(stiskla_karta):
	global vybrany_jazyk
	global vyberJazykaKartaBool
	for events in pygame.event.get():
		if events.type == pygame.MOUSEBUTTONDOWN and jazyk.collidepoint(events.pos):
			print(f"{Fore.GREEN}LOG:{Fore.RESET} settings:jazyk")
			surface.blit(pripravaText, pripravaRect)
			pygame.display.update()
			time.sleep(.3)
			surface.fill(color)
			vybrany_jazyk = vyber_jazyku()
			if vybrany_jazyk == None:
				return True
			elif not vybrany_jazyk:
				print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:zpet")
				vyberJazykaKartaBool = False
				return True
			print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:nacitani")
			preklad(vybrany_jazyk)
			print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:vybran")
			vyberJazykaKartaBool = False
			return True
		if events.type == pygame.MOUSEBUTTONDOWN and zpet.collidepoint(events.pos):
			print(f"{Fore.GREEN}LOG:{Fore.RESET} settings:zpet")
			surface.fill(color)
			return True
		konec_check = ukonceni(events, False)
		if konec_check:
			return True
	a,b = pygame.mouse.get_pos()
	if stiskla_karta:
		surface.blit(pripravaText, pripravaRect)
		surface.fill(color)
		vybrany_jazyk = vyber_jazyku()
		if vybrany_jazyk == None:
			return True
		elif not vybrany_jazyk:
			print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:zpet")
			vyberJazykaKartaBool = False
			return True
		print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:nacitani")
		preklad(vybrany_jazyk)
		print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:vybran")
		vyberJazykaKartaBool = False
		return True

executing = False
def hryFunkce(stiskla_karta):
	global hryKarta
	global hryKartaBool
	global executing

	surface.fill(color)
	if stiskla_karta and executing:
		executing = False
		return True
	executing = True
	user_text = ''

	hryKartaBool = True
	zustat = False
	print(f"{Fore.GREEN}LOG:{Fore.RESET} hry:maximalizovat")
	while not zustat:
		pygame.draw.rect(surface, green, input_rect)
		text_surface = font.render(user_text, True, (255, 255, 255))
		surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
		input_rect.w = max(100, text_surface.get_width()+10)
		surface.blit(okText, okRect)
		surface.blit(texthryText, texthryRect)
		#lista
		pygame.draw.rect(surface, black, pygame.Rect(0, 565, 1000, 35))
		if vyberJazykaKartaBool:
			hryKarta = pygame.Rect(smallfont.size(vyberJazykaTextStr)[0] + 22, 565, smallfont.size(hryTextStr)[0] + 17, 35)
			hryRectKarta.x = smallfont.size(vyberJazykaTextStr)[0] + 30
			pygame.draw.rect(surface, color_light, hryKarta)
			surface.blit(hryTextKarta, hryRectKarta)

			pygame.draw.rect(surface, color_dark, vyberJazykaKarta)
			surface.blit(vyberJazykaTextKarta, vyberJazykaRectKarta)
		else:
			hryKarta = pygame.Rect(20, 565, smallfont.size(hryTextStr)[0], 35)
			hryRectKarta.x = 20
			pygame.draw.rect(surface, color_light, hryKarta)
			surface.blit(hryTextKarta, hryRectKarta)
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.MOUSEBUTTONDOWN:
				if okRect.collidepoint(events.pos):
					try:
						with open(f"{user_text}.py") as hra:
							exec(hra.read())
							zustat = True
					except:
						surface.blit(exceptText, exceptRect)
				zustat = karta(events, True)
				if hryKarta.collidepoint(events.pos):
					print(f"{Fore.GREEN}LOG:{Fore.RESET} hry:minimalizovat")
					surface.fill(color)
					return True
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_BACKSPACE:
					user_text = user_text[:-1]
				else:
					user_text += events.unicode
			ukonceni(events, False)

def karta(events, v_hre):
	global executing
	if vyberJazykaKartaBool and vyberJazykaKarta.collidepoint(events.pos):
		print(f"{Fore.GREEN}LOG:{Fore.RESET} jazyk:maximalizovat")
		if v_hre:
			executing = not executing
		surface.fill(color)
		return settings(True)

	if hryKartaBool and hryKarta.collidepoint(events.pos):
		zustat = hryFunkce(True)
		return zustat

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
	surface.blit(hryText, hryRect)

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
					zustat = settings(False)
					pygame.display.update()
				if not konec_check:
					ukonceni(events, True)
			# Hry
			if hry.collidepoint(events.pos):
				hryFunkce(False)
			# Karta
			if not zustat:
				zustat = karta(events, False)
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
	if vyberJazykaKartaBool:
		pygame.draw.rect(surface, color_dark, vyberJazykaKarta)
		surface.blit(vyberJazykaTextKarta, vyberJazykaRectKarta)
	if hryKartaBool:
		pygame.draw.rect(surface, color_dark, hryKarta)
		surface.blit(hryTextKarta, hryRectKarta)
	# update
	pygame.display.update()
