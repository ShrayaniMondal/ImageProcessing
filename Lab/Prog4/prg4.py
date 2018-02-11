#Convert a grayscale image to a colour image with the following adjustments:
# if I>245 then R=I-20,G=I-10,B=I-5
# else R=I+10,G=I+10,B=I+5
# I have changed the differeneces in order to make the change more prominent

import numpy as np
import cv2

img = cv2.imread('45g.jpg',0)
dim = img.shape
colour_image = np.zeros((dim[0],dim[1],3),np.uint8)

for i in range(dim[0]):
	for j in range(dim[1]):
		if img[i][j] > 245:
			colour_image[i][j][0] = img[i][j] - 15
			colour_image[i][j][1] = img[i][j] - 20
			colour_image[i][j][2] = img[i][j] - 25
		else:
			colour_image[i][j][0] = img[i][j] + 35
			colour_image[i][j][1] = img[i][j] + 50
			colour_image[i][j][2] = img[i][j] + 20
				

cv2.imwrite('colour_image.jpg',colour_image)

cv2.imshow('Image in Colour',colour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
