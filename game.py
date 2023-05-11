# TO DO:
# add point tracker system
# edit interface design
# Add comments / clean up

import pygame
#pygame.font.get_fonts()
from Camille import button
from Camille import anim
from get_letter import get_letter
import pygame.camera
import pygame.image
import os
import sys
import random
#import copy_of_classifier

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
score_font = pygame.font.SysFont("menlo", 16, italic=True)

# colors
white_col = (255, 255, 255) # white
black_col = (0,0,0) # black
red_col = (255,0,0)
green_col = (0,255,0)
blue_col = (0,0,255)
purple_col = (160, 32, 240)

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

# Game pictures
bear_head = pygame.image.load("images/bear_head.png").convert_alpha()
bear_honey = pygame.image.load("images/bear_honey.png").convert_alpha()
bear_honey = pygame.transform.scale(bear_honey, (80, 80))

bear_w_heart = pygame.image.load("images/bear_heart.png").convert_alpha()
bear_w_heart = pygame.transform.scale(bear_w_heart, (300,300))

cute_bear = pygame.image.load("images/cute_bear.png").convert_alpha()
cute_bear = pygame.transform.scale(cute_bear, (60, 60))

empty_heart = pygame.image.load("images/empty_heart.png").convert_alpha()
empty_heart = pygame.transform.scale(empty_heart, (30, 30))

footpath = pygame.image.load("images/footpath.png").convert_alpha()
full_heart = pygame.image.load("images/full_heart.png").convert_alpha()
full_heart = pygame.transform.scale(full_heart, (30, 30))

heart = pygame.image.load("images/heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (30, 30))


honey = pygame.image.load("images/honey.png").convert_alpha()
honey = pygame.transform.scale(honey, (50, 50))

minus_10 = pygame.image.load("images/minus_10.png").convert_alpha()
minus_10 = pygame.transform.scale(minus_10, (30, 30))

minus_20 = pygame.image.load("images/minus_20.png").convert_alpha()
minus_20 = pygame.transform.scale(minus_20, (30, 30))

minus_30 = pygame.image.load("images/minus_30.png").convert_alpha()
minus_30 = pygame.transform.scale(minus_30, (30, 30))

minus_40 = pygame.image.load("images/minus_40.png").convert_alpha()
minus_40 = pygame.transform.scale(minus_40, (30, 30))

sleepy_bear = pygame.image.load("images/sleepy_bear.png").convert_alpha()
sleepy_bear = pygame.transform.scale(sleepy_bear, (350,350))


def draw_text(text, font, text_col, x, y): # Draws text onto screen, call this so you don't have to 'blit' text every time
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
  pygame.display.update()

def disp_score(score, score_font, x, y): # display score
  score_text = score_font.render(f'Score: {score}', True, white_col)
  screen.blit(score_text, (x, y)) 
#  pygame.display.flip()

#  pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60), 2) # 2 means only the boundaries
  pygame.display.flip()

# MAKING CLOCK COUNTDOWN TIMER 
clock = pygame.time.Clock()
timer_event = pygame.USEREVENT+0
pygame.time.set_timer(timer_event, 1000)
clock.tick(60) # 60 frames can pass per sec (max)

# Score Keeping
score = 0
hits = 5
score_inc = 10

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
    pygame.display.flip()

    screen.blit(footpath, (0,410))
    screen.blit(cute_bear, (575, 370))
    screen.blit(heart, (590, 340))
    pygame.display.flip()

  # Moving the honey

    if score == 0:
      screen.blit(honey, (0,370))
    elif score == 10:
      screen.blit(honey, (100,370))
    elif score == 20:
      screen.blit(honey, (200,370))
    elif score == 30:
      screen.blit(honey, (300,370))
    elif score == 40:
      screen.blit(honey, (400,370))
    elif score == 50:
      screen.blit(honey, (500,370))
    elif score == 60:
      screen.blit(bear_honey, (570, 370))
    elif score >= 70:
      screen.fill(white_col)
      draw_text("You win! Feel free to", font, black_col, 0, 0)
      draw_text("keep practicing :)", font, black_col, 0, 30)
      screen.blit(bear_w_heart, (180,100))
      pygame.display.flip()
      pygame.time.delay(5000)
      heart = full_heart

# If you make a mistake, you hurt Bruno's heart!
    if hits == 1:
      screen.blit(minus_10, (590, 340))
    if hits == 2:
      screen.blit(minus_20, (590, 340))
    if hits == 3:
      screen.blit(minus_30, (590, 340))
    if hits == 4:
      screen.blit(minus_40, (590, 340))
    if hits == 5:
      screen.blit(empty_heart, (590, 340))
    if hits == 6:
      screen.fill(black_col)
      draw_text("You killed Bruno >.< !!", font, white_col, 5, 0)
      draw_text("HOW COULD YOU!! ", font, white_col, 5, 40)
      draw_text("Try again! :)", font, white_col, 5, 80)
      screen.blit(sleepy_bear, (150,100))
      pygame.display.flip()
      pygame.time.delay(5000)
      # score = 0
      # hits = 0
      sys.exit()


#    pygame.draw.rect(screen, purple_col, (0, 450, 640, 80))
    pygame.draw.rect(screen, black_col, (0, 445, 200, 30))
    disp_score(score, score_font, 10, 450) # (width, height)
    
    # Display letter
    letter = get_letter(1)
    small_letter = letter # to be displayed with webcame footage
    letter_font = pygame.font.SysFont("antiquewhite", 650)
    letter = letter_font.render(letter, True, black_col)
    screen.blit(letter,(190, 15)) # make this big and centered
    draw_text("Sign the letter to feed Bruno!", font, black_col, 50, 0)

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

    disp_score(score, score_font, 10, 10)

    pygame.display.flip()
    
    # (For Debugging purposes): now image will be sent to images folder so we can check that it's screenshotting at the right time
    camille = True
    if camille:
      directory = r'/Users/camilleaquino/Documents/GitHub/CLPS_0950_FinalProject/images/'
    else: 
      directory = r'/Users/stylianisapantzi/Documents/GitHub/CLPS_0950_FinalProject/images/' # is this her path? !!!!!

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
       #pretty_background = pygame.transform.scale(pretty_background, (WIDTH, HEIGHT))
       screen_display.update()
       pygame.time.delay(2000)
       
       # Now send picture to Stella's function
       stella_func = random.randint(-1, 1)
     # if copy_of_classifier(img) == small_letter: !!!!!!!!!!!!!!!!!! Integration?
       
       if stella_func > 0:
         screen.fill(black_col)
         #  ADD POINTS
         score += score_inc
         disp_score(score, score_font, 10, 10)

         draw_text("CORRECT!", bigger_font_true, green_col, 0, 168)
         pygame.time.delay(2000)

       else:
        screen.fill(black_col)
         # SUBTRACT POINTS
        score -= score_inc
        disp_score(score, score_font, 10, 10)
        hits+=1
        draw_text("INCORRECT!", bigger_font_false, red_col, 0, 168)
        pygame.time.delay(2000)
      
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
