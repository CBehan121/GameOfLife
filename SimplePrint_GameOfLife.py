import sys
from random import randint
import time
global endme
endme = 0
def main():
	x, y = 50, 50
	matrix = [[randint(0,1)] * x for _ in range (y + 1)]

	printer(matrix)
	secondGen(matrix, x, y)

def secondGen(matrix, x, y):
	time.sleep(0.1)
	print(chr(27) + "[2J")
	global endme
	endme = endme + 1
	future = [[0] * x for _ in range (y + 1)]
	for l in range(1, x-1):
		for m in range(1,y-1):
			livingneighbours = 0
			for i in range(-1,2):
					for j in range(-1,2):
						livingneighbours += matrix[l + i][m + j]
			
			livingneighbours = livingneighbours -  matrix[l][m]
			if ((matrix[l][m] == 1) and (livingneighbours < 2)):
				future[l][m] = 0
				
			elif ((matrix[l][m] == 1) and (livingneighbours > 3)):
				
				future[l][m] == 0
			elif ((matrix[l][m] == 0) and (livingneighbours == 3)):

				future[l][m] = 1
				
			else:
				future[l][m] = matrix[l][m]
		
	printer(future)
	if endme == 200:
		sys.exit()
	else:
		secondGen(future, x, y)	
def printer(matrix):
		for each in matrix:
			for single in each:
				if single == 1:
					print( "+" , end =" ") 
				else:
					print(" ", end =" ")
			print()


if __name__ == "__main__":
	main()