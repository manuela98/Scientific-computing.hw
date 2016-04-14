
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

N1=100
N=1000
n=100
P=0.5
def rwalk(N,p):
	n=0
	for i in range(N):
		x = np.random.random()
		if x > p: #Cara
			n=n+1
		else: #Sello
			n=n-1
	return n


r=np.linspace(1,N1,num=N1,endpoint=True)
SUMA=0

for k in range(len(r)):
	r[k]=rwalk(100,0.5)
	#print r[k]
	SUMA=SUMA+r[k]
	#print SUMA
PROMEDIO=SUMA/N1
print PROMEDIO

manulin
 	


