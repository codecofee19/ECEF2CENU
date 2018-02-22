import re
import numpy as np 
# Read in input from file 



def ECEF2ENU(x, y, z):
	theta = 0
	lamda = np.arctan(y_0/x_0) 
	first_matrix = np.matrix([[x - x_0],[y - y_0],[z - z_0]])



i = 0
x_0 = 0
y_0 = 0 
z_0 = 0
x = 0 
y = 0 
z = 0
with open('ECEF.txt', 'r') as text:  
	for line in text:
		if line:
			result = re.split(r',\s+', line)
			print(result)
			# store the center of the ENU frame, (x_p, y_p, z_p)
			if(i == 2):
				x_0 = float(result[0])
				y_0 = float(result[1])
				z_0 = float(result[2])
				t_0 = float(result[3]) 
			if(len(result) == 4 and i >= 2): 
				x = float(result[0])
				y = float(result[1])
				z = float(result[2])
				t = float(result[3])
				ECEF2ENU(x,y, z)
		i += 1

a = np.matrix([[0], [1], [2]])
print(a.shape)
