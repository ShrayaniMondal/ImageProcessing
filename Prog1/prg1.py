#WAP to store a image in different formats and record the size of these images

import numpy as np
import cv2
import os

img = cv2.imread('3.jpg',-1)

#size of png#
cv2.imwrite('3_as_png.png',img)
size_png = os.stat('3_as_png.png')
print('size of png file in bytes : '+str(size_png.st_size))

#size of tiff#
cv2.imwrite('3_as_tif.tif',img)
size_tif = os.stat('3_as_tif.tif')
print('size of tif file in bytes : '+str(size_tif.st_size))

#size of jpg#
cv2.imwrite('3_as_jpg.jpg',img)
size_jpg = os.stat('3_as_jpg.jpg')
print('size of jpg file in bytes : '+str(size_jpg.st_size))