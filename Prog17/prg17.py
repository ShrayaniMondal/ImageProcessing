'''Compute intersection of two images(take minimum pixel)
merge two grayscale images using XOR and XNOR
'''
import cv2
import numpy as np

file1 = input('Enter the name of the file')
img1 = cv2.imread(file1,0)
file2 = input('Enter the name of the file')
img2 = cv2.imread(file2,0)

dim1 = img1.shape
dim2 = img2.shape

if dim1[0]>dim2[0]:
	row = dim1[0]
else:
	row = dim2[0]

if dim1[1]>dim2[1]:
	col = dim1[1]
else:
	col = dim2[1]

img1 = cv2.resize(img1,(row,col))
img2 = cv2.resize(img2,(row,col))

''' INTERSECTION '''
intersection = np.zeros((row,col),np.uint8)
for i in range(row):
	for j in range(col):
		intersection[i,j] = min(img1[i,j],img2[i,j])

''' XOR '''
xor = np.zeros((row,col),np.uint8)
for i in range(row):
	for j in range(col):
		xor[i,j] = (img1[i,j]^img2[i,j])

''' XOR '''
xnor = np.zeros((row,col),np.uint8)
for i in range(row):
	for j in range(col):
		xnor[i,j] = ~(img1[i,j]^img2[i,j])

cv2.imwrite('intersection.jpg',intersection)
cv2.imwrite('xor.jpg',xor)
cv2.imwrite('xnor.jpg',xnor)
