import pygame
import pygame.camera
from pygame.locals import *
import sys # to access the system
import cv2

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras() # asks for where the camera is in the computer
if camlist:
    cam = pygame.camera.Camera(camlist[1],(640,480)) 

cam.start()
image = cam.get_image()
img_name = str(image)

cam.set_controls(hflip = True, vflip = False)
cam.get_controls()

img = cv2.imread(img_name, cv2.IMREAD_ANYCOLOR)
 
while True:
    cv2.imshow("Sheep", img)
    cv2.waitKey(0) # waits until you exit or click close
    sys.exit() # to exit from all the processes
 
#cv2.destroyAllWindows() # destroy all windows