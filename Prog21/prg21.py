'''

Perform the FFT transformation


'''

import numpy as np
import cv2

# in fft we take the absolute value

img  = cv2.imread('messi.jpg',0)
f1 = np.fft.fft2(img)
fft_shift = np.fft.fftshift(f1)
magtinude_spectrum = 20*np.log(np.abs(fft_shift))
cv2.imwrite('fft_img.jpg',magtinude_spectrum)