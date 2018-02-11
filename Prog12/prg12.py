import numpy as np
import cv2

file = input('Enter The File name')
img  = cv2.imread(file,-1)

sobel_h = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 5) # Sobel(src,output image depth, derivative order x, derivative order y, kernel size)
sobel_v = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 5)

i = cv2.addWeighted(sobel_h,0.5,sobel_v,0.5,0) # Calculates the weighted sum of two arrays
cv2.imwrite('edge_result.jpg',i)