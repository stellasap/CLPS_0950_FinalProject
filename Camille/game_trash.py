# asl_review = pygame.image.load("images/asl_review.png").convert_alpha() 
# asl_review = pygame.transform.scale(asl_review, (640, 480))

#back_img = pygame.image.load('images/back_button.jpeg').convert_alpha()

#asl_img = pygame.image.load("images/qmark_button.jpeg").convert_alpha()

#back_button = button.Button(332, 450, back_img, 0.2)
#asl_button = button.Button(200, 145, asl_img, 0.2)


  #screen.fill((150, 100, 150)) # color


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


  ####### BACKDROP
    #pygame.time.delay(3000)

   # if pygame.camera.init():
    #   pygame.display.set_caption("Your Letter is" + small_letter) # remind the person of their letter
    # pygame.display.update()
 

  # pygame.time.delay(1000) # delay longer , play countdown while showing the camera
     # grab next frame    
   # img = webcam.get_image()
   # screen.blit(img, (0,0))
   # pygame.display.flip()
    #small_letter = font.render(str(small_letter), True, (0, 0, 255)) 
    #      


    # screen.blit(img, (0,0))
    # pygame.display.flip()
    #pygame.time.delay(3000) # countdown into taking picture?


   # delay after each event

    # >= 60 fps
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


       #pygame.display.flip()
      
     # if event.key == pygame.K_a:
      #draw_text("a", font, text_col, 130, 240)
        # call Stella's function with (A)
      #if event.key == pygame.K_b:




import pygame


# white color
color = (255,255,255)
  
# light shade of the button when you hover over it
color_light = (200,200,200)
  
# dark shade of the button
color_dark = (50,50,50)
  
# stores the width of the
# screen into a variable
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
  
# rendering a text written in
# this font
text = smallfont.render('quit' , True , color)
  
while True:
      
    for event in pygame.event.get():
          
        if event.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
                  
    # fills the screen with a color
    screen.fill((30,50,125)) # dark blue
      
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
      
    # if mouse is hovered on a button it
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,135,30])
          
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,135,30])
      
    # superimposing the text onto our button
    screen.blit(text , (width/2+50,height/2))
      
    # updates the frames of the game
    pygame.display.update()



#========================================

# ENDED UP INTEGRATING THIS FUNCTION INTO THE GAME.PY

import pygame
import pygame.camera
from pygame.locals import *
import sys # to access the system
import cv2
import os 

pygame.init()
pygame.camera.init()

######### METHOD 3
import pygame.camera
import pygame.image
import sys

pygame.camera.init()

cameras = pygame.camera.list_cameras()

print("Using camera %s ..." % cameras[0])

directory = r'/Users/camilleaquino/Documents/GitHub/CLPS_0950_FinalProject/images/'


webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame


pygame.time.delay(1000) # delay longer , play countdown while showing the camera

img = webcam.get_image()

WIDTH = img.get_width()
HEIGHT = img.get_height()
print(WIDTH)
print(HEIGHT)

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption("pyGame Camera View")
screen.blit(img, (0,0))
pygame.display.flip()
img = webcam.get_image()

pygame.time.delay(3000) # countdown into taking picture?

filename = os.path.join(directory,"image.jpeg")
pygame.image.save(img, filename) #don't have to save because you just want to use it and send it to stella's


while True :
    for e in pygame.event.get() :
       if e.type != timer_event :
         # pygame.image.load(img)
         sys.exit()
            
    # draw frame
    screen.blit(img, (0,0))
    pygame.display.flip()
    # grab next frame    
    img = webcam.get_image()
            

   
# NEXT STEPS: SAVE IMAGE INTO IMAGES folders#######################################

#                               CAPTURE_IMG.PY


#camlist = pygame.camera.list_cameras() # asks for where the camera is in the computer
#if camlist:
#    cam = pygame.camera.Camera(camlist[1],(640,480)) 

#cam.start()
#image = cam.get_image()
#pygame.image.save(image, "image.jpg")
#img_name = str(image)

#cam.set_controls(hflip = True, vflip = False)
#cam.get_controls()

#img = cv2.imread(img_name, cv2.IMREAD_ANYCOLOR)

#while True:
#    cv2.imshow("image.jpg", image)
#    print(img)
#    cv2.waitKey(0) # waits until you exit or click close
#    sys.exit() # to exit from all the processes
 
#cv2.destroyAllWindows() # destroy all windows



############# OTHER METHOD
# program to capture single image from webcam in python

# importing OpenCV library
# from cv2 import *

# # initialize the camera
# # If you have multiple camera connected with
# # current device, assign a value in cam_port
# # variable according to that
# cam_port = 0
# cam = VideoCapture(cam_port)

# # reading the input using the camera
# result, image = cam.read()

# # If image will detected without any error,
# # show result
# if result:

# 	# showing result, it take frame name and image
# 	# output
# 	imshow("GeeksForGeeks", image)

# 	# saving image in local storage
# 	imwrite("GeeksForGeeks.png", image)

# 	# If keyboard interrupt occurs, destroy image
# 	# window
# 	waitKey(0)
# 	destroyWindow("GeeksForGeeks")

# # If captured image is corrupted, moving to else part
# else:
# 	print("No image detected. Please! try again")



#===========================

#           CLOCK.PY

# ENDED UP INTEGRATING THIS INTO THE GAME.PY


# import pygame

# pygame.init()
# window = pygame.display.set_mode((200, 200))
# clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 100)
# counter = 5
# text = font.render(str(counter), True, (0, 128, 0))

# timer_event = pygame.USEREVENT+1
# pygame.time.set_timer(timer_event, 1000)

# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         elif event.type == timer_event:
#             counter -= 1
#             text = font.render(str(counter), True, (0, 128, 0))
#             if counter == 0:
#                 pygame.time.set_timer(timer_event, 0)                

#     window.fill((255, 255, 255))
#     text_rect = text.get_rect(center = window.get_rect().center)
#     window.blit(text, text_rect)
#     pygame.display.flip()


# OTHER COUNTDOWN METHOD

import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Pose!'
        if e.type == pygame.QUIT: 
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)






#=========

#  score_rect = score_text.get_rect(center = screen.get_rect().center)
    # (left line, top line, right line, bottom line)



