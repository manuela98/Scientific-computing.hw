
#creado el ocho de marzo
#rk algorithm

import numpy
import matplotlib
import matplotlib.pyplot
d=0.1
k=0.2
y0=200
t=range(101)
y=range(101)
y0=200
def f(x):
     return -k*x

for i in range(101):
	y1=y0+d*f(y0+1/2*d*f(y0))
	y0=y1
	y[i]=y1
	t[i]=i*d

print y

ynew=numpy.array(y)
tnew=numpy.array(t)
print ynew
print tnew

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.show()





