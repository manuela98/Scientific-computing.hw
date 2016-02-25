
#creado el 25 de febrero de 2016
#concentracion de un medicamento a traves de un tiempo
import numpy
import matplotlib
import matplotlib.pyplot

d=0.1
k=0.2
Q0=200
t=range(101)
Q=range(101)

for i in range(1,101,1):

    Q1=Q0-k*d*Q0
    Q0=Q1 
    Q[i]=Q1
    t[i]=i

Qnew=numpy.array(Q)
tnew=numpy.array(t)

print Qnew
print tnew

matplotlib.pyplot.plot(tnew,Qnew)
matplotlib.pyplot.show()

