'''
1.Robert's operator
2.prewitt's operator
3.kirsch's operator
'''
import cv2
import numpy as np
import math

file = input('Enter the name of the file')
img = cv2.imread(file,0)
rows,cols = img.shape


#Robert
rob = np.zeros([rows,cols])
R_Vert = np.array([[1,0],[0,-1]])
R_Hor = np.array([[0,1],[-1,0]])

temp1 = np.zeros([rows,cols])
temp2 = np.zeros([rows,cols])

for i in range(0,rows-1):
	for j in range(0,cols-1):
		temp1[i][j] = img[i][j]*R_Vert[0][0] + img[i][j+1]*R_Vert[0][1] + img[i+1][j]*R_Vert[1][0] + img[i+1][j+1]*R_Vert[1][1]

for i in range(0,rows-1):
	for j in range(0,cols-1):
		temp2[i][j] = img[i][j]*R_Hor[0][0] + img[i][j+1]*R_Hor[0][1] + img[i+1][j]*R_Hor[1][0] + img[i+1][j+1]*R_Hor[1][1]

for i in range(0,rows):
	for j in range(0,cols):
		rob[i][j] = np.sqrt((temp1[i][j]**2) + (temp2[i][j]**2))		

cv2.imwrite('Robert.jpg',rob)


#Prewitt
P_Vert = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
P_Hor = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])

pre_vert = np.zeros([rows,cols])
pre_hor = np.zeros([rows,cols])

for i in range(1,rows-1):
	for j in range(1,cols-1):
		pre_vert[i][j] = img[i-1][j-1]*P_Vert[0][0] + img[i-1][j]*P_Vert[0][1] + img[i-1][j+1]*P_Vert[0][2] + img[i][j-1]*P_Vert[1][0] + img[i][j]*P_Vert[1][1] + img[i][j+1]*P_Vert[1][2] + img[i+1][j-1]*P_Vert[2][0] + img[i+1][j]*P_Vert[2][1] + img[i+1][j+1]*P_Vert[2][2]

for i in range(1,rows-1):
	for j in range(1,cols-1):
		pre_hor[i][j] = img[i-1][j-1]*P_Hor[0][0] + img[i-1][j]*P_Hor[0][1] + img[i-1][j+1]*P_Hor[0][2] + img[i][j-1]*P_Hor[1][0] + img[i][j]*P_Hor[1][1] + img[i][j+1]*P_Hor[1][2] + img[i+1][j-1]*P_Hor[2][0] + img[i+1][j]*P_Hor[2][1] + img[i+1][j+1]*P_Hor[2][2]

cv2.imwrite('Prewitt_Vert.jpg',pre_vert)
cv2.imwrite('Prewitt_Hor.jpg',pre_hor)

#Kirsch
kirsch_1 = np.array([[5,5,5],[-3,0,-3],[-3,-3,-3]])
kirsch_2 = np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]])
kirsch_3 = np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]])
kirsch_4 = np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]])
kirsch_5 = np.array([[-3, -3, -3],[-3, 0, -3],[5, 5, 5]])
kirsch_6 = np.array([[-3, -3, -3],[-3, 0, 5],[-3, 5, 5]])
kirsch_7 = np.array([[-3, -3, 5],[-3, 0, 5],[-3, -3, 5]])
kirsch_8 = np.array([[-3, 5, 5],[-3, 0, 5],[-3, -3, -3]])

i1 = np.zeros([rows,cols])
i2 = np.zeros([rows,cols])
i3 = np.zeros([rows,cols])
i4 = np.zeros([rows,cols])
i5 = np.zeros([rows,cols])
i6 = np.zeros([rows,cols])
i7 = np.zeros([rows,cols])
i8 = np.zeros([rows,cols])

for i in range(1,rows-1):
	for j in range(1,cols-1):
		i1[i][j] = img[i-1][j-1]*kirsch_1[0][0] + img[i-1][j]*kirsch_1[0][1] + img[i-1][j+1]*kirsch_1[0][2] + img[i][j-1]*kirsch_1[1][0] + img[i][j]*kirsch_1[1][1] + img[i][j+1]*kirsch_1[1][2] + img[i+1][j-1]*kirsch_1[2][0] + img[i+1][j]*kirsch_1[2][1] + img[i+1][j+1]*kirsch_1[2][2]

for i in range(1,rows-1):
	for j in range(1,cols-1):
		i2[i][j] = img[i-1][j-1]*kirsch_2[0][0] + img[i-1][j]*kirsch_2[0][1] + img[i-1][j+1]*kirsch_2[0][2] + img[i][j-1]*kirsch_2[1][0] + img[i][j]*kirsch_2[1][1] + img[i][j+1]*kirsch_2[1][2] + img[i+1][j-1]*kirsch_2[2][0] + img[i+1][j]*kirsch_2[2][1] + img[i+1][j+1]*kirsch_2[2][2]

for i in range(1,rows-1):
	for j in range(1,cols-1):
		i3[i][j] = img[i-1][j-1]*kirsch_3[0][0] + img[i-1][j]*kirsch_3[0][1] + img[i-1][j+1]*kirsch_3[0][2] + img[i][j-1]*kirsch_3[1][0] + img[i][j]*kirsch_3[1][1] + img[i][j+1]*kirsch_3[1][2] + img[i+1][j-1]*kirsch_3[2][0] + img[i+1][j]*kirsch_3[2][1] + img[i+1][j+1]*kirsch_3[2][2]

for i in range(1,rows-1):
	for j in range(1,cols-1):
		i4[i][j] = img[i-1][j-1]*kirsch_4[0][0] + img[i-1][j]*kirsch_4[0][1] + img[i-1][j+1]*kirsch_4[0][2] + img[i][j-1]*kirsch_4[1][0] + img[i][j]*kirsch_4[1][1] + img[i][j+1]*kirsch_4[1][2] + img[i+1][j-1]*kirsch_4[2][0] + img[i+1][j]*kirsch_4[2][1] + img[i+1][j+1]*kirsch_4[2][2]

for i in range(1,rows-1):
	for j in range(1,cols-1):
		i5[i][j] = img[i-1][j-1]*kirsch_5[0][0] + img[i-1][j]*kirsch_5[0][1] + img[i-1][j+1]*kirsch_5[0][2] + img[i][j-1]*kirsch_5[1][0] + img[i][j]*kirsch_5[1][1] + img[i][j+1]*kirsch_5[1][2] + img[i+1][j-1]*kirsch_5[2][0] + img[i+1][j]*kirsch_5[2][1] + img[i+1][j+1]*kirsch_5[2][2]

for i in range(1,rows-1):
	for j in range(1,cols-1):
		i6[i][j] = img[i-1][j-1]*kirsch_6[0][0] + img[i-1][j]*kirsch_6[0][1] + img[i-1][j+1]*kirsch_6[0][2] + img[i][j-1]*kirsch_6[1][0] + img[i][j]*kirsch_6[1][1] + img[i][j+1]*kirsch_6[1][2] + img[i+1][j-1]*kirsch_6[2][0] + img[i+1][j]*kirsch_6[2][1] + img[i+1][j+1]*kirsch_6[2][2]

for i in range(1,rows-1):
	for j in range(1,cols-1):
		i7[i][j] = img[i-1][j-1]*kirsch_7[0][0] + img[i-1][j]*kirsch_7[0][1] + img[i-1][j+1]*kirsch_7[0][2] + img[i][j-1]*kirsch_7[1][0] + img[i][j]*kirsch_7[1][1] + img[i][j+1]*kirsch_7[1][2] + img[i+1][j-1]*kirsch_7[2][0] + img[i+1][j]*kirsch_7[2][1] + img[i+1][j+1]*kirsch_7[2][2]

for i in range(1,rows-1):
	for j in range(1,cols-1):
		i8[i][j] = img[i-1][j-1]*kirsch_8[0][0] + img[i-1][j]*kirsch_8[0][1] + img[i-1][j+1]*kirsch_8[0][2] + img[i][j-1]*kirsch_8[1][0] + img[i][j]*kirsch_8[1][1] + img[i][j+1]*kirsch_8[1][2] + img[i+1][j-1]*kirsch_8[2][0] + img[i+1][j]*kirsch_8[2][1] + img[i+1][j+1]*kirsch_8[2][2]

cv2.imwrite('Kirsch1.jpg',i1)
cv2.imwrite('Kirsch2.jpg',i2)
cv2.imwrite('Kirsch3.jpg',i3)
cv2.imwrite('Kirsch4.jpg',i4)
cv2.imwrite('Kirsch5.jpg',i5)
cv2.imwrite('Kirsch6.jpg',i6)
cv2.imwrite('Kirsch7.jpg',i7)
cv2.imwrite('Kirsch8.jpg',i8)
