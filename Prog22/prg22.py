'''

Perform the DST transformation


'''
import numpy as np
import cv2

# in dst we take the imaginary value

img = cv2.imread('messi.jpg',0)
f2 = np.fft.fft2(img)
fft_shift = np.fft.fftshift(f2)
magnitude_spectrum = 20*np.log(np.imag(fft_shift))
cv2.imwrite('dst_img.jpg',magnitude_spectrum)