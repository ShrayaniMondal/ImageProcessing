'''remove gaussian noise : gaussian filter '''

import numpy as np
import cv2

file = input('Enter the name of the file')
img = cv2.imread(file,0)
gaussian_filtered = cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite('Gaussian_Filtered.jpg',gaussian_filtered)