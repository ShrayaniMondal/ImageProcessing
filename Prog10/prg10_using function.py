'''Write a program to detect
a.Horizontal line
b.vertical line'''


import numpy as np
import cv2

file = input('Enter The File name')
img  = cv2.imread(file,-1)

sobel_h = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 5) # Sobel(src,output image depth, derivative order x, derivative order y, kernel size)
sobel_v = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 5)

#########Detecting horizontal lines###############
i_h = cv2.addWeighted(sobel_h,0,sobel_v,1,0) # Calculates the weighted sum of two arrays
cv2.imwrite('hori_result.jpg',i_h)

#########Detecting vertical lines###############
i_v = cv2.addWeighted(sobel_h,1,sobel_v,0,0) # (img_arr1,weight of img_arr1, img_arr2, weight of img_arr2, depth of output)
cv2.imwrite('ver_result.jpg',i_v)