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

