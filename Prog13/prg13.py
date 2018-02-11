''' Program to apply mean transform on an image'''


import numpy as np
import cv2

file  = input('Enter the name of the file')
img = cv2.imread(file,0)
mean_img = img

dim = img.shape

mean_mask = np.ones((3,3))

for i in range(1,dim[0]-1):
	for j in range(1,dim[1]-1):

		mean_img[i][j] = (mean_mask[0][0]*img[i-1][j-1] + mean_mask[0][1]*img[i-1][j] + mean_mask[0][2]*img[i][j+1]+
						mean_mask[1][0]*img[i][j-1] + mean_mask[1][1]*img[i][j] + mean_mask[1][2]*img[i][j+1]+
						mean_mask[2][0]*img[i+1][j-1] + mean_mask[2][1]*img[i+1][j] + mean_mask[2][2]*img[i+1][j+1])/9

cv2.imwrite('mean_img.jpg',mean_img)
