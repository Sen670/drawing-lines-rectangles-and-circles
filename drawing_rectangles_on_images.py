import cv2
import numpy as np
import os

image1 = cv2.imread("lhama2.jpg")
start_point = (625,500)
end_point = (675,550)
colour = (0,0,255)
thickness = 3

image1 = cv2.rectangle(image1,start_point,end_point,colour,thickness)

cv2.imshow("image1",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()



























