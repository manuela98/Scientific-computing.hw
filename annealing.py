import matplotlib.pyplot as plt
import numpy as np

def cost(x):
    c = np.exp(-(x-1)**2)*np.sin(8*x)+1
    return c


m = 200

k= range(m)

t = np.linspace(-3,3, num=m)


for i in range(m):
        k[i] = cost(t[i])
        

plt.plot(t,k)
plt.show()

    

def neighbor(x):
    return (2* np.random.random()-1) * step_size + x

f=np.random.uniform(-3,3)
t=1
tmin=10**-5

while t<tmin
for j in range(100):
	c1=neighbor(x)
	u=np.random.uniform(0,1)
	eq1=np.exp((x-c1)/t)

	if eq1>u:
		l=cost(eq1)



