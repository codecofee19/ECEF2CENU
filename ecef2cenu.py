import re
# Read in input from file 
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

