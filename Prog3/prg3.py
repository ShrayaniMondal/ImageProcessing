#Convert a colour image to grayscale using formula
#Formula(memorise) : I = 0.29*R+0.58*G+0.11*B

'''Note channel 0: Blue
		channel 1: Green
		channel 2: Red'''

import numpy as np
import cv2

img = cv2.imread('3.jpg',-1)
dim = img.shape
img_in_grey = np.zeros([dim[0],dim[1]])

for i in range(dim[0]):
	for j in range(dim[1]):
		img_in_grey[i][j] = img[i][j][0]*0.11 + img[i][j][1]*0.58 + img[i][j][2]*0.29

cv2.imwrite('image_in_grey.jpg',img_in_grey)

cv2.imshow('Image in Grey',img_in_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()