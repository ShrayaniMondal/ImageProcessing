''' Resize an image --- in this case making it bigger'''

import numpy as np
import cv2

file = input('Enter The File name')
img  = cv2.imread(file,-1)
dim = img.shape

rows = dim[0]*2
cols = dim[1]*2

resize = np.zeros((rows,cols,3),np.uint8)

for i in range(rows):
		for j in range(cols):
			for k in range(3):
				resize[i][j][k] = img[i/2][j/2][k]

cv2.imwrite('resize.jpg',resize)
cv2.imshow('Resized Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


