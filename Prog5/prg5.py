''' Control the brightness of the image'''

import numpy as np
import cv2

file = input('Enter The File name')
key = input('Enter whether you want to increase or decrease brightness: i or d')
img = cv2.imread(file,-1)
dim = img.shape
decrease_bright = np.zeros((dim[0],dim[1],3),np.uint8)
increase_bright = np.zeros((dim[0],dim[1],3),np.uint8)

if(key == 'i'):
	for i in range(dim[0]):
		for j in range(dim[1]):
			for k in range(3):
				try:
					if img[i][j][k] <= 205:
						increase_bright[i][j][k] = img[i][j][k] + 50
				except IndexError:
					continue
	cv2.imshow('Brightness Increased',increase_bright)
	cv2.imwrite('Brightness_Increased.jpg',increase_bright)
				

elif(key == 'd'):
	for i in range(dim[0]):
		for j in range(dim[1]):
			for k in range(3):
				try:
					if img[i][j][k] >= 50:
						decrease_bright[i][j][k] = img[i][j][k] - 50
				except:
					continue
	cv2.imshow('Brightness Decreased',decrease_bright)
	cv2.imwrite('Brightness_Decreased.jpg',decrease_bright)
				
cv2.waitKey(0)
cv2.destroyAllWindows()

