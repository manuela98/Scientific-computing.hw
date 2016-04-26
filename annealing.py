import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

def costos(a):
	b=-(a-1)**2
	EQ2=np.e**b*np.sin(8*a)+1
	return EQ2
x=np.linspace(-3,3, num=1000, endpoint=True)
for i in range(len(x)):
	x[i]=costos(i)

s=range(len(x))

plt.plot(s,x)
plt.show()

def neighbor(a):
	step_size=1
	return (2*np.random.random()-1)*step_size+a




