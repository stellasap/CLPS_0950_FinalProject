# TO DO:
# add point tracker system
# edit interface design
# Add comments / clean up

import pygame
from Camille import button
from Camille import anim
from get_letter import get_letter
import pygame.camera
import pygame.image
import os

# Start Pygame
pygame.init()

# Create display
screen_w = 640
screen_h = 480
screen = pygame.display.set_mode((screen_w, screen_h)) #idky but it needs double parentheses

#game variables
game_paused = True
menu_state = "main"

# fonts
font = pygame.font.SysFont("arialblack", 35)
pose_font = pygame.font.SysFont("arialblack", 100)
bigger_font_true = pygame.font.SysFont("arialblack", 110)
bigger_font_false = pygame.font.SysFont("arialblack", 90)

# colors
white_col = (255, 255, 255) # white
black_col = (0,0,0) # black
red_col = (255,0,0)
green_col = (0,255,0)
blue_col = (0,0,255)

#load button images
resume_img = pygame.image.load("images/start_button.png").convert_alpha()
quit_img = pygame.image.load("images/exit_button.jpeg").convert_alpha()

#create button instances
resume_button = button.Button(100, 400, resume_img, 0.7)
quit_button = button.Button(400, 400, quit_img, 0.4)

# Backgrounds
main_menu_background = pygame.image.load("images/asl_background.jpeg").convert_alpha()
main_menu_background = pygame.transform.scale(main_menu_background, (640, 400))
pretty_background = pygame.image.load("images/game_background.jpeg").convert_alpha() 
#pretty_background = pygame.transform.scale(pretty_background, (640, 400))

def draw_text(text, font, text_col, x, y): # Draws text onto screen, call this so you don't have to 'blit' text every time
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
  pygame.display.update()

# MAKING CLOCK COUNTDOWN TIMER 
clock = pygame.time.Clock()
timer_event = pygame.USEREVENT+0
pygame.time.set_timer(timer_event, 1000)
clock.tick(60) # 60 frames can pass per sec (max)

#game loop
run = True
while run:

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      screen.fill(black_col) # picture doesn't cover whole screen, fill rest with black
      screen.blit(main_menu_background, (0,0))
      pygame.display.set_caption("Main Menu")
     
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
        
      if quit_button.draw(screen):
        run = False

  else: # during the game
 # Set caption of screen
    pygame.display.set_caption('PRESS SPACE TO PAUSE / REVIEW!')   
     
    screen_display = pygame.display
    pygame.display.set_mode((screen_w, screen_h))
    pygame.display.update()

    # General game background
    screen.blit(pretty_background,(0,0))
    
    # Random letterfrom A-Z (except J, Z) gets displayed

    letter = get_letter(1)
    small_letter = letter # to be displayed with webcame footage
    letter_font = pygame.font.SysFont("antiquewhite", 650)
    letter = letter_font.render(letter, True, black_col)
    screen.blit(letter,(190, 15)) # make this big and centered
    draw_text("Sign the Letter:", font, black_col, 190, 0)
    screen_display.update()

    pygame.time.delay(3000)

    # Start the camera, display webcam footage
    #     NOTE: sometimes my iphone connects with my laptop and it gets confused about which camera to display from
    #     just run and start the game again
    pygame.camera.init()
    cameras = pygame.camera.list_cameras() # tells code which camera to use
    print("Using camera %s ..." % cameras[0])  
    webcam = pygame.camera.Camera(cameras[0])
    webcam.start()
   
    # Display a frame
    img = webcam.get_image()
    WIDTH = img.get_width()
    HEIGHT = img.get_height()
    screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
    img = webcam.get_image()
    screen.blit(img, (0,0))
    pygame.display.flip()
    
    # (For Debugging purposes): now image will be sent to images folder so we can check that it's screenshotting at the right time
    directory = r'/Users/camilleaquino/Documents/GitHub/CLPS_0950_FinalProject/images/'

    # Starting Countdown from 5, person has time to adjust their hand shape
    event.type == timer_event
    clock_counter = 5   
    clock_text = font.render(str(clock_counter), True, (0, 25, 0))

    for num in range(clock_counter,0,-1):
      img = webcam.get_image()
      screen.blit(img, (0,0))

      draw_text("Your letter is: " + small_letter, font, blue_col, 150, 0)
      text = font.render(str(clock_counter), True, white_col)
      text_rect = text.get_rect(center = screen.get_rect().center)
      screen.blit(text, text_rect)
      
      screen_display.update()

      clock_counter -= 1

      pygame.time.delay(1000)

      # At Countdown = 0, take a picture
      if clock_counter == 0:
       img = webcam.get_image()
       screen.blit(img, (0,0))
       get_ready = pose_font.render("Pose!", True, white_col)
       get_ready_rect = get_ready.get_rect(center = screen.get_rect().center)
       screen.blit(get_ready, get_ready_rect)
       pygame.time.set_timer(timer_event, 0) # set to 0 means end countdown  
       filename = os.path.join(directory,"image.jpeg")
       pygame.image.save(img, filename) #don't have to save because you just want to use it and send it to stella's
       pretty_background = pygame.transform.scale(pretty_background, (WIDTH, HEIGHT))
       screen_display.update()
       pygame.time.delay(2000)
       
       # Now send picture to Stella's function
       # stella_func(img, small_letter)


       stella_func = True
       if stella_func:
         screen.fill(black_col)
         draw_text("CORRECT!", bigger_font_true, green_col, 0, 168)
         pygame.time.delay(2000)

        #  ADD POINTS
          

       else:
        screen.fill(black_col)
        draw_text("INCORRECT!", bigger_font_false, red_col, 0, 168)
        pygame.time.delay(2000)
        
        # SUBTRACT POINTS

          # NEXT STEPS: add points bar whenever game is unpaused
          # when person fills up the bar they win the game, load "YOU WIN! on screen??

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
