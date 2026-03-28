import cv2
import numpy as np
import os

image1 = cv2.imread("cat_1.jpg")
start_point = (650,125)
start_point2 = (640,225)
ending_point = (810,125)
ending_point2 = (800,225)
colour = (0,0,255)
colour2 = (0,0,0)
thickness = 10
font = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
text_thickness = 3
text_start = (50,50)
text_start2 = (820,135)
text_start3 = (810,235)

image1 = cv2.line(image1,start_point,ending_point,colour,thickness)
image1 = cv2.line(image1,start_point2,ending_point2,colour,thickness)
image1 = cv2.putText(image1,"Body parts of a cat",text_start,font,fontScale,colour2,text_thickness,cv2.LINE_AA)
image1 = cv2.putText(image1,"Ears",text_start2,font,fontScale,colour2,text_thickness,cv2.LINE_AA)
image1 = cv2.putText(image1,"Eyes",text_start3,font,fontScale,colour2,text_thickness,cv2.LINE_AA)


cv2.imshow("original image",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()






