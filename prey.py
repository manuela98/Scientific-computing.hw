#poblacion de animales en tiempo
#creado el marzo 1 del 2016

import numpy
import matplotlib
import matplotlib.pyplot



ky=2.0
kyx=0.01
kx=1.06
kxy=0.01
d=0.1
x0=15
y0=100
t=range(101)
y=range(101)
y[0]=y0
x[0]=x0


for i in range(1,101)
	y1=(d*ky*y0)-(d*kxy*x0*y0)+y0
	y0=y1
	x1=(d*kyx*y0*x0)-(d*kx*x0)+x0
	x0=x1
        y[i]=y1
	x[i]=x1
	t[i]=i*0.1
	
	




ynew=numpy.array(y)
xnew=numpy.array(x)
tnew=numpy.array(t)

print ynew
print xnew
print tnew

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.plot(tnew,xnew)
matplotlib.pyplot.show()
   

