''' crop image '''

import numpy as np
import cv2

file = input('Enter The File name')
img  = cv2.imread(file,-1)
dim = img.shape

top_left_x = input('Enter the Top Left x-coordinate')
top_left_y = input('Enter the Top Left y-coordinate')
bottom_right_x = input('Enter the Bottom Right x-coordinate')
bottom_right_y = input('Enter the Bottom Right y-coordinate')

rows = int(bottom_right_y) - int(top_left_y)
cols = int(bottom_right_x) - int(top_left_x)

crop = np.zeros((rows,cols,3),np.uint8)

for i in range(rows):
	for j in range(cols):
		crop[i][j][0] = img[i][j][0]
		crop[i][j][1] = img[i][j][1]
		crop[i][j][2] = img[i][j][2]

cv2.imwrite('crop.jpg',crop)
cv2.imshow('Cropped Image', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()