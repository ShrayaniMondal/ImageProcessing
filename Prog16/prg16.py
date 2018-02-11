'''
Separate color image into 3 separate R,G,B
#Enhance R plane by +30
#Enhance G plane by -30
#Enhance B plane by +20

Combine the resultant R,G,B to set new colour image

'''

import cv2
import numpy as np

file = input('Enter the name of the file')
img = cv2.imread(file,-1)
split_and_merge = img

row,col,channel = img.shape

b,g,r = cv2.split(img)

for i in range(row):
	for j in range(col):
		b[i,j] = min(b[i,j]+20,255)

for i in range(row):
	for j in range(col):
		g[i,j] = max(g[i,j]-20,0)

for i in range(row):
	for j in range(col):
		r[i,j] = min(r[i,j]+30,255)

for i in range(row):
	for j in range(col):
		split_and_merge[i,j,0] = b[i,j]
		split_and_merge[i,j,1] = g[i,j]
		split_and_merge[i,j,2] = r[i,j]

cv2.imwrite('split_and_merge.jpg',split_and_merge)
		