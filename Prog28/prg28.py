'''
first and second order derivative of
single dimension image:
60 60 100 100 100
'''
import cv2
import numpy as np

img = np.array([0,0,60,60,100,100,100,0,0])
r = img.size

# FIRST DERIVATIVE
list_first_der = []

for i in range(r-1):
	list_first_der.append(img[i+1]-img[i])
print('First Order Derivative:' + str(list_first_der))

# SECOND DERIVATIVE
list_second_der = []
r = len(list_first_der)

for i in range(r-1):
	list_second_der.append(list_first_der[i+1]-list_first_der[i])
print('Second Order Derivative:' + str(list_second_der))

