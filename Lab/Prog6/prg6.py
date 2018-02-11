''' contrast adjustment '''

import numpy as np
import cv2

file = input('Enter The File name')
img  = cv2.imread(file,1)
dim = img.shape
contrast = np.zeros((dim[0],dim[1],3),np.uint8)

for i in range(dim[0]):
	for j in range(dim[1]):
		for k in range(3):
			try:
				if img[i][j][k] > 90:
					contrast[i][j][k] = img[i][j][k]*2
				else:
					contrast[i][j][k] = img[i][j][k]/2
			except IndexError:
				continue

cv2.imwrite('contrast.jpg',contrast)
cv2.imshow('High Contrast', contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()