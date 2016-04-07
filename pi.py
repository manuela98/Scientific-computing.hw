import numpy as np
import matplotlib 
import matplotlib.pyplot as plt


#print np.random.random()
#imprime numeros aleatorios en un rango de 0 
#np.random.seed(6)
#print np.random.random()

R=1
L=3
N=10000
n=0.0

for i in range(N):

	y= 1.5-np.random.random()*3
	x= 1.5-np.random.random()*3
	
	puntoxy=np.sqrt(x**2+y**2)
	
	if puntoxy <=R:
		n=n+1

print n
		
def fpi(L,N,R):
	print (n/float(N))*(L/R)**2

print fpi(3.,10000,1.)




	
