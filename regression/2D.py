# 2D_Data_Starter
# Basic plotting of 2D data.

# Import the matplotlib package and alias the pyplot module 
import matplotlib.pyplot as plt
import numpy as np

# Create the plot object
fig, ax = plt.subplots()

# Set the viewing window in the plot from -50 to 50  in both directions
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)

# Read in the data
# Data format: x,y,

xdata = []
ydata = []

f = open("2D.txt")
data = f.readlines()
f.close()

# Parse the data into lists of x's and y's

for i in range(len(data)):
  datapoint = data[i].split(',')
  xdata.append(float(datapoint[0]))
  ydata.append(float(datapoint[1]))
  

# Here we define the set of x- and y-coordinates beforehand
# The 'ro' option yields red unconnected dots

plt.plot(xdata,ydata, 'ro')

onesVector = np.ones(len(xdata))
m_t = np.array([onesVector, xdata])
m = np.matrix_transpose(m_t)
v = np.matrix_transpose(np.array([ydata]))
coefficients = np.linalg.matmul(np.linalg.matmul(np.linalg.inv(np.linalg.matmul(m_t, m)), m_t), v)

print(f"y = {coefficients[1][0]}x + {coefficients[0][0]}")

# This plots the line from (0,5) to (20,1), i.e. the line y = -0.2x + 5 
plt.plot([-25,25], [-50,50],'b')

def toYCoordinates(xCoordinates, coefficients):
    l = []
    for x in xCoordinates:
       l.append(coefficients[1][0] * x + coefficients[0][0])
    return l

lineBounds = [-50, 50]
plt.plot(lineBounds, toYCoordinates(lineBounds, coefficients))

# This shows the object (Must ctrl-c out of this in the console)
# Commented out because this does not work in Github Codespaces
# plt.show() 

# Save plot to output.png
plt.savefig('2D_Data_output.png')