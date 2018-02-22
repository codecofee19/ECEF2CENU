import re
# Read in input from file 
i = 0
with open('ECEF.txt', 'r') as text:  
	for line in text:
		if line:
			result = re.split(r',\s+', line)
			print(result)
			if(len(result) == 4): 
				x = result[0]
				y = result[1]
				z = result[2]
				t = result[3]
			if(i == 2):
				x_p = result[0]
				y_p = result[1]
				z_p = result[2]
				t_p = result[3]
		i += 1

print(x_p)
print(y_p)
print(z_p)
print(t_p)
