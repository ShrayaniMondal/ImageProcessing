'''

Quad Tree Decomposition

'''

import cv2
import numpy as np

def checkPixel(img,list_of_tuples):
	x1,y1,x2,y2 = list_of_tuples[0]
	x1 = int(x1)
	x2 = int(x2)
	y1 = int(y1)
	y2 = int(y2)
	for i in range(x1+1,x2-1):
		for j in range(y1+1,y2-1):
			d1 = abs(int(img[i][j]) - int(img[i+1][j]))
			d2 = abs(int(img[i][j]) - int(img[i-1][j]))
			d3 = abs(int(img[i][j]) - int(img[i][j+1]))
			d4 = abs(int(img[i][j]) - int(img[i][j-1]))
			if((d1>15) or (d2>15) or (d3>15) or (d4>15)):
				return 1
	return 0

def segmentImage(img,list_of_tuples):
	x1,y1,x2,y2 = list_of_tuples[0]
	del list_of_tuples[0]
	list_of_tuples.append((x1,y1,(x1+x2)/2,(y1+y2)/2))
	list_of_tuples.append(((x1+x2)/2,y1,x2,(y1+y2)/2))
	list_of_tuples.append((x1,(y1+y2)/2,(x1+x2)/2,y2))
	list_of_tuples.append(((x1+x2)/2,(y1+y2)/2,x2,y2))

	return(list_of_tuples)

def sameColour(img,list_of_tuples):
    x1,y1,x2,y2 = list_of_tuples[0]
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    val = img[x1,y1]
    for i in range(x1,x2):
        for j in range(y1,y2):
            if(i == x1 or i == x2-1 or j == y1 or j==y2-1):
                img[i,j] = 0
            else:
                img[i,j] = val
    return img


img = cv2.imread('fr.jpeg',0)
row,col = img.shape

list_of_tuples = []
init_co = (0,0,row-1,col-1)
list_of_tuples.append(init_co)

while(list_of_tuples):
	if(checkPixel(img,list_of_tuples)==1):
		list_of_tuples = segmentImage(img,list_of_tuples)
	else:
		img = sameColour(img,list_of_tuples)
		del list_of_tuples[0]

cv2.imwrite('QuadTree.jpg',img)

	