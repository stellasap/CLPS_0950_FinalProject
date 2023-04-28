#import sys
import pygame
import button
import demo_camera # how to use demo camera in game?
import random

pygame.init()

screen_w = 700
screen_h = 700

screen = pygame.display.set_mode((screen_w, screen_h)) #idky but it needs 2 parentheses
pygame.display.set_caption("Menu")

#game variables
game_paused = True
menu_state = "main"

# fonts
font = pygame.font.SysFont("arialblack", 35)

# colors

text_col = (255, 255, 255) # white

#load button images
#start_img = pygame.image.load("images/start_button.jpeg").convert_alpha()
resume_img = pygame.image.load("images/start_button.jpeg").convert_alpha()
quit_img = pygame.image.load("images/exit_button.jpeg").convert_alpha()
#back_img = pygame.image.load('images/back_button.jpeg').convert_alpha()

#create button instances
#start_button = button.Button(255, 125, start_img, 0.2)
resume_button = button.Button(304, 125, resume_img, 0.2)
quit_button = button.Button(336, 375, quit_img, 0.2)
#back_button = button.Button(332, 450, back_img, 0.2)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((150, 100, 150)) # color

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
    #  if options_button.draw(screen):
    #    menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    #if menu_state == "options":
      #draw the different options buttons
      #if video_button.draw(screen):
      #  print("Video Settings")
      #if audio_button.draw(screen):
      #  print("Audio Settings")
      #if keys_button.draw(screen):
      #  print("Change Key Bindings")
     # if back_button.draw(screen):
     #   menu_state = "main"
  else: # during the game
    draw_text("Press SPACE to pause", font, text_col, 160, 250)

    # randomly choose a letter from A-Z except J, Z #################################
    chars = 'abcdefghiklmnopqrstuvwxy'
    randomLetter = random.choice(chars)
    draw_text(randomLetter, font, text_col, 125, 250) 
    #pygame.time.set_timer(2)
    # need to be able to code so that the game displays text, the person shows the hand shape
    # and if it's right it moves onto the next one and adds a score
#################################

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False


  pygame.display.update()

pygame.quit()
