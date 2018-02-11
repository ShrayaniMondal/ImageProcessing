'''
Take an image, convert to grayscale, display only those pixels which are in a particular range.
'''

import numpy as np
import cv2

file =  input('Enter the name of the image')
img =  cv2.imread(file,0)
dim = img.shape

p1 = int(input('Enter the starting pixel value'))
p2 = int(input('Enter the ending pixel value'))

for i in range(dim[0]):
	for j in range(dim[1]):
		if (img[i,j]>p1 and img[i,j]<p2):
			continue
		else:
			img[i,j] = 255
cv2.imwrite('Result.jpg',img)