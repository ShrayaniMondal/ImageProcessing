'''Write a program for point processing based image enhancement using
a.Log and inverse log transformations 
b.Gamma correction(power law transformation) with negative and positive value of gamma'''

import numpy as np
import cv2

''' NOTE:- c is defined to normalize the resulting image to a valid (visible) range. Then a rational value for c could be:

c = (L - 1)/log(L) 

where L is the number of gray levels. So s would be:

s = log(r+1) * ((L – 1)/log(L)) 

or

s = log(r+1) * c

Then the inverted transformation would be:

s2 = (exp(r) ^ (log(L) / (L-1))) – 1

or

s2 = (exp(r) ^ (1/c)) – 1 '''

''' LOG TRANSFORMATION '''
file = input('Enter The File name')
img  = cv2.imread(file,-1)
dim = img.shape
log_trns = np.zeros((dim[0],dim[1],3),np.uint8)

for i in range(dim[0]):
	for j in range(dim[1]):
		try:
			log_trns[i][j][0] = ((256-1)/np.log(256))*(np.log(img[i][j][0] + 1))
			log_trns[i][j][1] = ((256-1)/np.log(256))*(np.log(img[i][j][1] + 1))
			log_trns[i][j][2] = ((256-1)/np.log(256))*(np.log(img[i][j][2] + 1))
		except IndexError:
			continue
cv2.imwrite('log_trns.jpg',log_trns)

''' INVERSE LOG TRANSFORM '''

file = input('Enter The File name')
img  = cv2.imread(file,-1)
dim = img.shape
inv_log_trns = np.zeros((dim[0],dim[1],3),np.uint8)

for i in range(dim[0]):
	for j in range(dim[1]):
		try:
			inv_log_trns[i][j][0] = np.exp(img[i][j][0] * np.log(256)/(256-1))-1
			inv_log_trns[i][j][1] = np.exp(img[i][j][1] * np.log(256)/(256-1))-1
			inv_log_trns[i][j][2] = np.exp(img[i][j][2] * np.log(256)/(256-1))-1
		except IndexError:
			continue
cv2.imwrite('inv_log_trns.jpg',inv_log_trns)

''' GAMMA TRANSFORM '''

file = input('Enter The File name')
img  = cv2.imread(file,-1)
dim = img.shape
gamma_trns = np.zeros((dim[0],dim[1],3),np.uint8)
c=20
gamma = 8

for i in range(dim[0]):
	for j in range(dim[1]):
		try:
			gamma_trns[i][j] = c*img[i,j]**gamma
		except IndexError:
			continue
cv2.imwrite('gamma_trns.jpg',gamma_trns)