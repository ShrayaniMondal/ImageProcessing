#Convert a grayscale image to binary

import numpy as np
import cv2

img = cv2.imread('45g.jpg',0)
dim = img.shape
img_binary = np.zeros([dim[0],dim[1]])

for i in range(dim[0]):
	for j in range(dim[1]):
		if img[i][j]>127:
			img_binary[i][j] = 255
		else:
			img_binary[i][j] = 0
cv2.imwrite('img_binary.jpg',img_binary)

cv2.imshow('Image in Binary',img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()