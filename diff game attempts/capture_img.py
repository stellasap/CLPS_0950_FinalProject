import pygame
import pygame.camera
from pygame.locals import *
import sys # to access the system
import cv2

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
if camlist:
    cam = pygame.camera.Camera(camlist[1],(640,480))

cam.start()
image = cam.get_image()

cam.set_controls(hflip = True, vflip = False)
cam.get_controls()

img = cv2.imread(image, cv2.IMREAD_ANYCOLOR)
 
while True:
    cv2.imshow("Sheep", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes
 
#cv2.destroyAllWindows() # destroy all windows