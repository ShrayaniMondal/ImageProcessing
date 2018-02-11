'''
minimum cost of shortest path

2 8 6
3 5 4
4 3 2
'''

import cv2
import numpy as np

img = np.array([[2,8,6],[3,5,4],[4,3,2]])

h = 3
w = 3

cost = np.zeros([h,w,1],np.uint8)

for i in range(0,h):
	for j in range(0,w):
			if (i==0 or j==0):
				cost[i][j] = img[i][j]
			else:
				cost[i][j] = min(cost[i-1][j-1],cost[i][j-1],cost[i-1][j]) + img[i][j]
print(cost[h-1][w-1])