import cv2
import numpy as np
import os

image1 = cv2.imread("manatee.jpg")
centre_point = (475,425)
radius = 100
colour = (0,0,255)
thickness = 5

image1 = cv2.circle(image1,centre_point,radius,colour,thickness)


cv2.imshow("image1",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()












