'''
WAP to read five image from folder A,5 image form folder B,then convert them
into binary image and save all of them in folder C

'''

import cv2
import numpy as np

img1 = cv2.imread('A/a_1.jpg',0)
img2 = cv2.imread('A/a_2.jpg',0)
img3 = cv2.imread('A/a_3.jpg',0)
img4 = cv2.imread('A/a_4.jpg',0)
img5 = cv2.imread('A/a_5.jpg',0)

img6 = cv2.imread('B/b_1.jpg',0)
img7 = cv2.imread('B/b_2.jpg',0)
img8 = cv2.imread('B/b_3.jpg',0)
img9 = cv2.imread('B/b_4.jpg',0)
img10 = cv2.imread('B/b_5.jpg',0)

def gray_to_bin(img,num):
	row , col = img.shape
	for i in range(row):
		for j in range(col):
			if (img[i,j]>=128):
				img[i,j] = 255
			else:
				img[i,j] = 0
	cv2.imwrite('C/'+str(num)+'.jpg',img)

num = 1

gray_to_bin(img1,num)
num = num+1
gray_to_bin(img2,num)
num = num+1
gray_to_bin(img3,num)
num = num+1
gray_to_bin(img4,num)
num = num+1
gray_to_bin(img5,num)
num = num+1
gray_to_bin(img6,num)
num = num+1
gray_to_bin(img7,num)
num = num+1
gray_to_bin(img8,num)
num = num+1
gray_to_bin(img9,num)
num = num+1
gray_to_bin(img10,num)
