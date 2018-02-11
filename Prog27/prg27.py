'''
Take an image, convert to grayscale.
Perform Segmentation.
'''

import numpy as np
import cv2

################## SEGMENTATION #############################

img = cv2.imread('scene.jpg',0)
#cv2.imshow('img',img)
#cv2.waitKey(0)
cloud = img
water = img
trees = img

## showing cloud ##
row,col = cloud.shape

for i in range(0,row):
	for j in range(0,col):
		if(cloud[i,j]>240 and cloud[i,j]<=255):
			#print('cloud')
			continue
		else:
			cloud[i,j] = 0

cv2.imwrite('cloud.jpg',cloud)

## showing trees ##
row,col = trees.shape

for i in range(0,row):
	for j in range(0,col):
		if(trees[i,j]>=10 and trees[i,j]<150):
			#print('tree')
			continue
		else:
			trees[i,j] = 255


cv2.imwrite('trees.jpg',trees)

## showing water ##

row,col = water.shape


for i in range(0,row):
	for j in range(0,col):
		if(water[i,j]>=80 and water[i,j]<180):
			#print('water')
			continue
		else:
			water[i,j] = 255


cv2.imwrite('water.jpg',water)