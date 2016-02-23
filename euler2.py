#importamos libretas
#23 febrero
import numpy
import matplotlib
import matplotlib.pyplot


def g(t,r):
     return -r*t

def f(z,delta,r):
   
     return z+delta*g(z,r)
u0=0.1
delta=0.01
r=2.0
u=funcion(t,delta,r)
print u

n=100
t=range(n)
y=range(n)

for i in range (n):
     u1=f(u0,delta,r)
     y[i]=u1


