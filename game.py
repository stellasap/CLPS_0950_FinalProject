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
import pygame.camera
import pygame.image
import sys
import os

pygame.init()

screen_w = 640
screen_h = 480

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
#asl_img = pygame.image.load("images/qmark_button.jpeg").convert_alpha()
quit_img = pygame.image.load("images/exit_button.jpeg").convert_alpha()

main_menu_background = pygame.image.load("images/asl_background.jpeg").convert_alpha()
main_menu_background = pygame.transform.scale(main_menu_background, (640, 400))

# asl_review = pygame.image.load("images/asl_review.png").convert_alpha() 
# asl_review = pygame.transform.scale(asl_review, (640, 480))

#back_img = pygame.image.load('images/back_button.jpeg').convert_alpha()

#create button instances
#start_button = button.Button(255, 125, start_img, 0.2)
resume_button = button.Button(100, 400, resume_img, 0.7)
#asl_button = button.Button(200, 145, asl_img, 0.2)
quit_button = button.Button(400, 400, quit_img, 0.4)
#back_button = button.Button(332, 450, back_img, 0.2)

def draw_text(text, font, text_col, x, y): # so you don't have to blit every time
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
  pygame.display.update()

# MAKING CLOCK COUNTDOWN TIMER 
clock = pygame.time.Clock()

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
      screen.fill((0,0,0))
      screen.blit(main_menu_background, (0,0))
      pygame.display.set_caption("Menu")
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      # if person wants to review ASL Alphabet
      # if asl_button.draw(screen):
      #  # pygame.event.clear()
      #   pygame.display.set_caption('PRESS SPACE TO GO BACK')    
      #   screen.fill(asl_review,(0,0))
      #   pygame.display.update()
      #   for event in pygame.event.get():
      #     if event.type == pygame.KEYDOWN:
      #       if event.key == pygame.K_SPACE:
      #         game_paused = True
        
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
    #pygame.time.delay(3000)

    screen_display = pygame.display
    pygame.display.set_mode((screen_w, screen_h))
    # Set caption of screen
    pygame.display.set_caption('PRESS SPACE TO PAUSE')    
    # set the image which to be displayed on screen
    pretty_background = pygame.image.load("images/game_background.jpeg").convert_alpha() 
    # draw on image onto another
    screen.blit(pretty_background,(0,0))
    
    letter = get_letter(1)
    letter_font = pygame.font.SysFont("antiquewhite", 650)
    letter = letter_font.render(letter, True, (0, 0, 0))
    screen.blit(letter,(190, 12)) # make this big and centered\
    
    screen_display.update()

    draw_text("Sign the Letter:", font, (0,0,0), 190, 0)
    screen_display.update()

    pygame.time.delay(5000)

    pygame.camera.init()
    cameras = pygame.camera.list_cameras()
    print("Using camera %s ..." % cameras[0])
    webcam = pygame.camera.Camera(cameras[0])
    webcam.start()
    img = webcam.get_image()
    WIDTH = img.get_width()
    HEIGHT = img.get_height()
    screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
    pygame.display.set_caption("pyGame Camera View")
   
    img = webcam.get_image()
    screen.blit(img, (0,0))

    pygame.display.flip()
  # pygame.time.delay(1000) # delay longer , play countdown while showing the camera

     # grab next frame    
    img = webcam.get_image()
    screen.blit(img, (0,0))
    pygame.display.flip()
    
    directory = r'/Users/camilleaquino/Documents/GitHub/CLPS_0950_FinalProject/images/'
  
    # screen.blit(img, (0,0))
    # pygame.display.flip()
    #pygame.time.delay(3000) # countdown into taking picture?
    
    event.type == timer_event
    clock_counter = 5   
    clock_text = font.render(str(clock_counter), True, (0, 25, 0))
    for num in range(clock_counter,0,-1):
      #screen.fill(pygame.Color("black")) # erases the entire screen surface
      img = webcam.get_image()
      screen.blit(img, (0,0))
      text = font.render(str(clock_counter), True, (255, 255, 255))
      text_rect = text.get_rect(center = screen.get_rect().center)
      screen.blit(text, text_rect)
     # draw_text(str(num), font, (0,0,0), 250, 250)
      screen_display.update()

      clock_counter -= 1

      pygame.time.delay(1000)

      if clock_counter == 0:
       img = webcam.get_image()
       screen.blit(img, (0,0))
       post_font = pygame.font.SysFont("arialblack", 100)
       get_ready = post_font.render("Pose!", True, (255, 255, 255))
       get_ready_rect = get_ready.get_rect(center = screen.get_rect().center)
       screen.blit(get_ready, get_ready_rect)
       pygame.time.set_timer(timer_event, 0) # set to 0 means end countdown  
       filename = os.path.join(directory,"image.jpeg")
       pygame.image.save(img, filename) #don't have to save because you just want to use it and send it to stella's
       pretty_background = pygame.transform.scale(pretty_background, (WIDTH, HEIGHT))
       screen_display.update()
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
