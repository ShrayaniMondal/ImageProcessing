'''

Take a color image. Convert to :

1.Grayscale
2.Binary

'''
import numpy as np
import cv2

# Grayscale
img = cv2.imread('messi.jpg',0)
cv2.imwrite('Grayscale.jpg',img)

# Binary
dim = img.shape
bin_img = np.zeros((dim[0],dim[1]))
for i in range(dim[0]):
	for j in range(dim[1]):
		if img[i,j] <= 127:
			bin_img[i,j] = 0
		else:
			bin_img[i,j] = 255
cv2.imwrite('Binary.jpg',bin_img)