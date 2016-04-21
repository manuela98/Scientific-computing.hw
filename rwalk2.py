import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

def brownian(n):

	x=np.random.normal(0,1,n)
	h=np.cumsum(x)
	
	h[0]=0
	
	return h

plt.plot(brownian(200))
plt.show()



k=5	
for h in range(k):
	d=brownian(5)
	return d
	
	
	
