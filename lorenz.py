#atractor de lorenz
#creado jueves 3 de marzo 

import numpy
import matplotlib
import matplotlib.pyplot



sigma=10
beta=2.667
rho=28
x0=0
y0=1
z0=1.05
d=0.01
z=range(10000)
x=range(10000)
t=range(10000)
y=range(10000)
y[0]=y0
x[0]=x0
z[0]=z0

for i in range(10000):
	x1=(d*sigma*y0)-(d*sigma*x0)+x0
	y1=(d*x0*rho)-(d*x0*z0)-(d*y0)+y0
	z1=(d*x0*y0)-(d*beta*z0)+z0
	x0=x1
	y0=y1
	z0=z1
        y[i]=y1
	x[i]=x1
	z[i]=z1
	t[i]=i*d
	
	



xnew=numpy.array(x)
ynew=numpy.array(y)
znew=numpy.array(z)
tnew=numpy.array(t)

print ynew
print xnew
print tnew
print znew

matplotlib.pyplot.plot(xnew,znew)
matplotlib.pyplot.show()
   

