''' erosion and dialation'''
import numpy as np
import cv2

img = cv2.imread('j.png',0)
rows,cols = img.shape
#converting to binary
bin_img = np.zeros([rows,cols])
for i in range(rows):
	for j in range(cols):
		if(img[i,j]>=127):
			bin_img[i,j] = 255
		else:
			bin_img[i,j] = 0

erosion = np.zeros([rows,cols])
dialation = np.zeros([rows,cols])

#dialation
for i in range(1,rows-1):
	for j in range(1,cols-1):
		if (bin_img[i][j]==0):
			if((img[i-1][j-1]==255) or (img[i][j-1]==255) or (img[i+1][j-1]==255) or (img[i-1][j]==255) or (img[i+1][j]==255) or (img[i-1][j+1]==255) or (img[i][j+1]==255) or (img[i+1][j+1]==255)):
				dialation[i][j] = 255
			else:
				dialation[i][j] = bin_img[i][j]
		else:
			dialation[i][j] = bin_img[i][j]

#erosion
for i in range(1,rows-1):
	for j in range(1,cols-1):
		if (bin_img[i][j]==255):
			if((img[i-1][j-1]==0) or (img[i][j-1]==0) or (img[i+1][j-1]==0) or (img[i-1][j]==0) or (img[i+1][j]==0) or (img[i-1][j+1]==0) or (img[i][j+1]==0) or (img[i+1][j+1]==0)):
				erosion[i][j] = 0
			else:
				erosion[i][j] = bin_img[i][j]
		else:
			erosion[i][j] = bin_img[i][j]

cv2.imwrite('Erosion.jpg',erosion)
cv2.imwrite('Dialation.jpg',dialation)