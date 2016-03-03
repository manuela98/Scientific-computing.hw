#poblacion de animales en tiempo
#creado el marzo 1 del 2016

import numpy
import matplotlib
import matplotlib.pyplot



Ky=2.0
Kyx=0.01
Kx=1.06
Kxy=0.01
D=0.1
X0=15
Y0=100
x=range(101)
t=range(101)
y=range(101)
y[0]=Y0
x[0]=X0


for i in range(101):
	Y1=(D*Ky*Y0)-(D*Kxy*X0*Y0)+Y0
	Y0=Y1
	X1=(D*Kyx*Y0*X0)-(D*Kx*X0)+X0
	X0=X1
        y[i]=Y1
	x[i]=X1
	t[i]=i*0.1
	
	




ynew=numpy.array(y)
xnew=numpy.array(x)
tnew=numpy.array(t)

print ynew
print xnew
print tnew

matplotlib.pyplot.plot(xnew,ynew)
matplotlib.pyplot.plot(ynew,xnew)
matplotlib.pyplot.show()
   

