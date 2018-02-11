''' Remove salt and pepper noise from the given image and display the restored image. '''
import cv2
import numpy as np

file = input('Enter the name of the file')
img = cv2.imread(file,0)
salt_pepper_removed = img

dim = img.shape

for i in range(1,dim[0]-1):
	for j in range(1,dim[1]-1):
		neighbour = []
		neighbour.append(img[i,j])
		neighbour.append(img[i,j-1])		
		neighbour.append(img[i,j+1])		
		neighbour.append(img[i-1,j])		
		neighbour.append(img[i-1,j-1])		
		neighbour.append(img[i-1,j+1])		
		neighbour.append(img[i+1,j])		
		neighbour.append(img[i+1,j-1])		
		neighbour.append(img[i+1,j+1])		

		neighbour.sort()
		salt_pepper_removed[i][j] = neighbour[4]

cv2.imwrite('salt_pepper_removed.jpg',salt_pepper_removed)
