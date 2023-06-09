import pygame
import button

# example of what buttons will look like

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('images/start_button.jpeg').convert_alpha()
exit_img = pygame.image.load('images/exit_button.jpeg').convert_alpha()

#create button instances
start_button = button.Button(100, 200, start_img, 0.15)
exit_button = button.Button(250, 200, exit_img, 0.15)

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		print('START')
	if exit_button.draw(screen):
		print('EXIT')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()