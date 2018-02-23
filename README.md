# ECEF2CENU
A program to transform coordinates into an ENU frame

# Overview
The program reads from the text file the ECEF coordinates, then by applying 
matrix multiplication, transforms ECEF to an ENU frame relative to the first 
coordinate in the text file. From then on, the program interpolates velocity 
and acceleration.  

# Graphs
![alt text](graphs.png)


# Software Requirements 

Ensure you have Python 2.7 installed. Download from [here](https://www.python.org/downloads/).

Also ensure you have the numpy, mpl_toolkits.mplot3d, and matplotlib.pyplot packages installed for python. If not installed follow the instructions [here](https://matplotlib.org/faq/installing_faq.html#clean-install). 


# Instructions

run `git clone git@github.com:codecofee19/ECEF2CENU.git` 

run  `cd ECEF2CENU`

run  `python ecef2enu.py` or if on Linux, Mac `chmod +x ecef2enu.py` and then `./ecef2enu.py`  

