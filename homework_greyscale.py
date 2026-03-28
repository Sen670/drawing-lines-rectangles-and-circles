import cv2
import numpy as np
import os

image1 = cv2.imread("octopus.jpg")
image2 = cv2.imread("tulips_1.jpg")
edges = cv2.Canny(image2,100,200)
grey_image = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
image3 = cv2.imread("giraffe.jpg")
hsv_image = cv2.cvtColor(image3,cv2.COLOR_BGR2HSV)


cv2.imshow("original image",image1)
cv2.waitKey(0)
cv2.imshow("original image 2",image2)
cv2.waitKey(0)
cv2.imshow("original image 3",image3)
cv2.waitKey(0)
cv2.imshow("Greyscale image",grey_image)
cv2.waitKey(0)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.imshow("hsv_image",hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

