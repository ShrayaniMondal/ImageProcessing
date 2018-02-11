''' Program to perform histogram equilisation '''

import numpy as np
import cv2

file  = input('Enter the name of the file')
img = cv2.imread(file,0)

hist = {}
dim = img.shape

for i in range(dim[0]):
	for j in range(dim[1]):
		if img[i,j] in hist:
			hist[img[i,j]] = hist[img[i,j]] + 1
		else:
			hist[img[i,j]] = 1

cdf = {}
c = 0 

for i in sorted(hist) :
	c = c + hist[i]
	cdf[i] = c

cdf_min = cdf[min(cdf.keys())]

h = {}
L = 256
M = dim[0]
N = dim[1]

for i  in cdf:
	h[i] = int(round(1.0*(cdf[i]-cdf_min)/(M*N - cdf_min)*(L-1)))

hist_img = np.zeros((M,N),np.uint8)

for i in range(dim[0]):
	for j in range(dim[1]):
		hist_img[i,j] = h[img[i,j]]

cv2.imwrite('hist_img.jpg',hist_img)