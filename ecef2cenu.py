import re
import numpy as np 
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# these are global variables needed throughout file
x_0 = 0
y_0 = 0 
z_0 = 0
x = 0 
y = 0 
z = 0
ENU_list = []
vel_list = []
Accel_list = []



def calcvel(enu1, enu2):
	enu1_matrix, time1 = enu1
	enu2_matrix, time2 = enu2
	time = 1 / (time1 - time2) 
	mat = np.subtract(enu1_matrix, enu2_matrix)
        mat = mat * time
	return mat 

def calcaccel(vel1, vel2):
	vel1_matrix, time1 = vel1 
	vel2_matrix, time2 = vel2 
	time = 1 / (time1 - time2) 
	result =  np.subtract(vel1_matrix,vel2_matrix)
	result = result * time 
	return result 



# method takes in x, y, z from ECEF and translates to ENU vector
def ECEF2ENU(x, y, z):
	theta = 0
	lamda = np.arctan(y_0/x_0) 
	first_matrix = np.matrix([[x - x_0,y - y_0,z - z_0]])
	r = math.sqrt(math.pow(x, 2.0) + math.pow(y, 2.0) + math.pow(z, 2.0))
	phi = np.arcsin(z/r)
	cos_lamda = math.cos(lamda)
	sin_lamda = math.sin(lamda)
	cos_phi = math.cos(phi)
	sin_phi = math.sin(phi)	
	second_matrix = np.matrix([[-sin_lamda, cos_lamda, 0], 
			[-sin_phi*cos_lamda, -sin_phi*sin_lamda, cos_phi],
			[cos_phi * cos_lamda, cos_phi * sin_lamda, sin_phi ]])

	result = first_matrix.dot(second_matrix)
	return result

# Read in input from file 
with open('ECEF.txt', 'r') as text:  
	for idx, line in enumerate(text):
		if line:
			result = re.split(r',\s+', line)
			# store the center of the ENU frame, (x_0, y_0, z_0)
			if(idx == 2):
				x_0 = float(result[0])
				y_0 = float(result[1])
				z_0 = float(result[2])
				time_0 = float(result[3]) 
			if(len(result) == 4 and idx >= 2): 
				x = float(result[0])
				y = float(result[1])
				z = float(result[2])
				time = float(result[3])
				enu = ECEF2ENU(x,y, z)
				pair = enu,time
				ENU_list.append(pair)

#for time, enu in enumerate(ENU_list):
x = []
y = []
z = []
for a,b in enumerate(ENU_list[1:]): 
	s = calcvel(b, ENU_list[a-1])
	enu, time = b 
	x.append(s[:,0])
	y.append(s[:,1])
	z.append(s[:,2])
	vel_pair = calcvel(b, ENU_list[a-1]), time
	vel_list.append(vel_pair)	
	
x_delta = [] 
y_delta = []
z_delta = []
for a,b in enumerate(vel_list[1:]): 
	result = calcaccel(b, vel_list[a-1])
	x_delta.append(result[:,0])
	y_delta.append(result[:,1])
	z_delta.append(result[:,2])
	
fig = plt.figure()
ax = fig.add_subplot(211,projection = '3d') 
ax.set_title("Velocity for ENU frame")
ax.scatter(x, y, z, c = 'r', marker = 'o')


ax.set_xlabel('E label')
ax.set_xlabel('N label')
ax.set_xlabel('U label')

ax = fig.add_subplot(212,projection = '3d') 
ax.set_title("Acceleration for ENU frame")

ax.scatter(x_delta, y_delta, z_delta, c = 'r', marker = 'o')


plt.show()
