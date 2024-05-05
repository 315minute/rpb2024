import numpy as np


def dfs(table):
	Y, X = np.shape(table)
	dx_dy = [(0,1), (0,-1), (1, 0), (-1,0)]
	max_buffer = 0
	for i in range(Y):
		for j in range(X):
			check = np.zeros(Y,X)
			buffer = 0
			if table[i][j] == 0:
				check[i][j] = 1
				buffer += 1
				for k in range dx_dy:
					if table			
				
	
	


if __name__ == '__main__':
	say()

