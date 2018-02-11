'''

Perform the DCT transformation


'''
import numpy as np
import cv2

# in dct we take the imaginary value

img = cv2.imread('messi.jpg',0)
f3 = np.fft.fft2(img)
fft_shift = np.fft.fftshift(f3)
magnitude_spectrum = 20*np.log(np.real(fft_shift))
cv2.imwrite('dct_img.jpg',magnitude_spectrum)