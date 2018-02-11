import cv2
import numpy as np

file =  input('Enter the name of the file')
res = cv2.imread(file,1)
img = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

h,w = img.shape

cost = np.zeros([h,w,1],np.uint8)

for i in range(h):
	for j in range(w):
		if (i==0 or j==0):
			cost[i][j] = img[i][j]
		else:
			cost[i][j] = min(cost[i-1][j], cost[i-1][j-1], cost[i][j-1]) + img[i][j]

print(cost[h-1][w-1])
img1  = cv2.cvtColor(cost,cv2.COLOR_GRAY2BGR)
cv2.imwrite('MinCost.jpg',img1)
cv2.imshow('img',img1)
cv2.waitKey(0)
