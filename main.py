import numpy as np 
import matplotlib.pyplot as plt 
f = open('Galaxy1.txt', 'r') 
f.readline()
radius=[]
velocity=[]
dRadius=[]
dVelocity=[]
mass=[]
predictedVelocity=[]
G=4.3*(10**-6)

for line in f:
  radius.append(float(line.split('\t')[0]))
  velocity.append(float(line.split('\t')[1]))
  dRadius.append(float(line.split('\t')[2]))
  dVelocity.append(float(line.split('\t')[3]))
  mass.append(float(line.split('\t')[4]))
  predictedVelocity.append(((float(G)) * (float(line.split('\t')[4])) / (float(line.split('\t')[0])))**(1/2))

x=np.array(radius)
y=np.array(velocity)
y1=np.array(predictedVelocity)


plt.plot(x,y)
plt.plot(x,y1)
plt.title('A graph of velocity(km/h) against radius(kpc)')
plt.xlabel('radius(kpc)')
plt.ylabel('velocity(km/h)')
plt.show()  