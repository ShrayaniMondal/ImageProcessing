'''Enhance the grayscale image using median filter of size 3*3 and 5*5 mask.'''

import cv2
import numpy as np

file = input('Enter the name of the file')
img = cv2.imread(file,0)
temp = cv2.imread(file,0)

dim = img.shape

###################3*3 mask median filter##################################

for i in range(1,dim[0]-1):
	for j in range(1,dim[1]-1):

		my_list = []
		for k in range(i-1,i+2):
			for l in range(j-1,j+2):
				my_list.append(img[k][l])

		my_list.sort()

		temp[i][j] = my_list[4]

cv2.imwrite('3by3median.jpg',temp)

##########################5*5 mask median filter##############################

temp = cv2.imread(file,0)

for i in range(2,dim[0]-2):
	for j in range(2,dim[1]-2):

		my_list = []
		for k in range(i-2,i+3):
			for l in range(j-2,j+3):
				my_list.append(img[k][l])

		my_list.sort()

		temp[i][j] = my_list[12]

cv2.imwrite('5by5median.jpg',temp)
