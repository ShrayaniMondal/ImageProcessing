''' Perform the following operations : 
	Crop a region of an image
	Enhance the cropped region
	Paste it back to the original image at the same place
'''
import numpy as np
import cv2

file =  input('Enter the name of the file')
img = cv2.imread(file,0)

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

rows = x2-x1+1
cols = y2-y1+1

crop = np.zeros((rows,cols),np.uint8)

k=0
for i in range(x1,x2):
	l=0
	for j in range(y1,y2):
		crop[k,l] = img[i,j]
		l=l+1
	k=k+1

crop_enhance = cv2.equalizeHist(crop)

x = x1
for i in range(rows):
	y = y1
	for j in range(cols):
		img[x,y] = crop_enhance[i,j]
		y = y + 1
	x = x + 1

cv2.imwrite('crcp_enhance.jpg',img)
