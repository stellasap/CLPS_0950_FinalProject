# TO DO:
# make falling letters. when person clicks on a letter it will ask them to sign it after a countdown. 
# after countdown, will take snapshot and send it to Stella's code. stella's code will compare it to database

#import sys
import pygame
from Camille import button
#import demo_camera # how to use demo camera in game?
import random
from Camille import anim
import gradio as gr
from get_letter import get_letter
#from Camille import capture_img

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
resume_img = pygame.image.load("images/start_button.png").convert_alpha()
quit_img = pygame.image.load("images/exit_button.jpeg").convert_alpha()
main_menu_background = pygame.image.load("images/asl_background.jpeg").convert_alpha()
main_menu_background = pygame.transform.scale(main_menu_background, (700, 700))
#back_img = pygame.image.load('images/back_button.jpeg').convert_alpha()

#create button instances
#start_button = button.Button(255, 125, start_img, 0.2)
resume_button = button.Button(250, 125, resume_img, 0.9)
quit_button = button.Button(250, 375, quit_img, 0.6)
#back_button = button.Button(332, 450, back_img, 0.2)

def draw_text(text, font, text_col, x, y): # so you don't have to blit every time
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
  pygame.display.update()

# MAKING CLOCK COUNTDOWN TIMER 
clock = pygame.time.Clock()
clock_counter = 5   
text = font.render(str(clock_counter), True, (0, 0, 0))
text_rect = text.get_rect(center = screen.get_rect().center)
clock_text = font.render(str(clock_counter), True, (0, 25, 0))

timer_event = pygame.USEREVENT+0
pygame.time.set_timer(timer_event, 1000)

#game loop
run = True
while run:
  
  #screen.fill((150, 100, 150)) # color

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      screen.blit(main_menu_background, (0,0))
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
  ####### BACKDROP

    screen_display = pygame.display   
    # Set caption of screen
    screen_display.set_caption('PRESS SPACE TO PAUSE')    
    # set the image which to be displayed on screen
    pretty_background = pygame.image.load("images/game_background.jpeg").convert_alpha() 
    # draw on image onto another
    screen.blit(pretty_background,(0,0))
    screen_display.update()

    letter = get_letter(1)
    draw_text(letter, font, (0, 0, 0), 150, 250)

    pygame.time.delay(2000)  
    event.type == timer_event
    for num in range(5,-1,-1):
      clock_counter -= 1
      #screen.blit(text, text_rect)
      draw_text(str(num), font, (0,0,0), 250, 250)
      # screen_display.update()
      pygame.time.delay(1000)
    if clock_counter == 0:
      pygame.time.set_timer(timer_event, 0) # set to 0 means end countdown  
      pygame.time.delay(2000)
      #capture_img()



    # randomly choose a letter from A-Z except J, Z #################################

    # delay after each event

    clock.tick(60) # >= 60 fps
    # for event in pygame.event.get():  
    #  if event.type == pygame.KEYDOWN:
    #   if event.key == pygame.K_RIGHT: # if ready to move on

      # letter = get_letter(1)
      # draw_text(letter, font, (0, 0, 0), 125, 250)
      # pygame.time.delay(1000)        
           # event.type == timer_event
           # clock_counter -= 1
           # text = font.render(str(clock_counter), True, (0, 0, 0))
           # text_rect = text.get_rect(center = screen.get_rect().center)
           # screen.blit(text, text_rect)
           # if clock_counter == 0:
           #   pygame.time.set_timer(timer_event, 0) # set to 0 means end countdown  



    # need to be able to code so that the game displays text, the person shows the hand shape
    # and if it's right it moves onto the next one and adds a score -- code something to 
    # reference back to Stella's code to see if it matches shape and if it returns 
    # # # # # MAYBE: with each letter, press the letter when you're ready to sign 
                  #  and then it will countdown to take a picture of you and then see if it matches

#################################

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True

        #pygame.display.flip()
      
     # if event.key == pygame.K_a:
     #   draw_text("a", font, text_col, 130, 240)
        # call Stella's function with (A)
      #if event.key == pygame.K_b:

    if event.type == pygame.QUIT:
      run = False


  pygame.display.update()

pygame.quit()
