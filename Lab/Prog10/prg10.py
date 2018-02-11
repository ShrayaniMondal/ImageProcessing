''' edge detection using sobel '''

import cv2
import numpy as np

filename = input('Enter Filename : ')
img = cv2.imread(filename,0)
rows, cols = img.shape

hor_edge = np.zeros([rows,cols])
ver_edge = np.zeros([rows,cols])
diag_edge = np.zeros([rows,cols])

H= [[-1, -1, -1],
[2, 2, 2],
[-1, -1, -1]]

V= [[-1, 2, -1],
[-1, 2, -1],
[-1, 2, -1]]

D1 = [[1, 1, 2],
[1, 2, 1],
[2, 1, 1]]

D2 = [[2, 1, 1],
[1, 2, 1],
[1, 1, 2]]


for i in range(1, rows-1):
	for j in range(1, cols-1):
		hor_edge[i][j] = img[i-1][j-1]*H[0][0] + img[i-1][j]*H[0][1] + img[i-1][j+1]*H[0][2] + img[i][j-1]*H[1][0] + img[i][j]*H[1][1]+ img[i][j+1]*H[1][2] + img[i+1][j-1]*H[2][0] + img[i+1][j]*H[2][1] + img[i+1][j+1]*H[2][2]


for i in range(1, rows-1):
	for j in range(1, cols-1):
		ver_edge[i][j] = img[i-1][j-1]*V[0][0] + img[i-1][j]*V[0][1] + img[i-1][j+1]*V[0][2] + img[i][j-1]*V[1][0] + img[i][j]*V[1][1]+ img[i][j+1]*V[1][2] + img[i+1][j-1]*V[2][0] + img[i+1][j]*V[2][1] + img[i+1][j+1]*V[2][2]

for i in range(1, rows-1):
	for j in range(1, cols-1):
		diag_edge[i][j] = img[i-1][j-1]*D1[0][0] + img[i-1][j]*D1[0][1] + img[i-1][j+1]*D1[0][2] + img[i][j-1]*D1[1][0] + img[i][j]*D1[1][1]+ img[i][j+1]*D1[1][2] + img[i+1][j-1]*D1[2][0] + img[i+1][j]*D1[2][1] + img[i+1][j+1]*D1[2][2]

for i in range(1, rows-1):
	for j in range(1, cols-1):
		diag_edge[i][j] = img[i-1][j-1]*D2[0][0] + img[i-1][j]*D2[0][1] + img[i-1][j+1]*D2[0][2] + img[i][j-1]*D2[1][0] + img[i][j]*D2[1][1]+ img[i][j+1]*D2[1][2] + img[i+1][j-1]*D2[2][0] + img[i+1][j]*D2[2][1] + img[i+1][j+1]*D2[2][2]

cv2.imwrite('hor_edge.jpg',hor_edge)
cv2.imwrite('ver_edge.jpg',ver_edge)
cv2.imwrite('diag_edge.jpg',diag_edge)
