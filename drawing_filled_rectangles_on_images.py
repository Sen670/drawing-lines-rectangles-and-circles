import cv2
import numpy as np
import os

image1 = cv2.imread("guy1.jpg")
start_point = (300,200)
end_point = (500,250)
colour = (0,0,0)
thickness = -1

image1 = cv2.rectangle(image1,start_point,end_point,colour,thickness)

cv2.imshow("image1",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()



























