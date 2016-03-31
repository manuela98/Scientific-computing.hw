#fecha 29 de marzo 

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
delta = 0.001
CM = 0.1 #uF/cm2
I = 15 #nA
V0 = -65 #mV
VK = -77 #mV
VNa = 50 #mV
VL = -54.4 #mV
gK = 36 #mS/cm2
gNa = 120 #mS/cm2
gL = 0.3 #mS/cm2
n0 = 0.317
m0 = 0.05
h0 = 0.6
T = 6.3 #gradosC
phi = 3 **((T-6.3)/10)

def fan(v):
	return phi * ((0.01 * v + 10))/(np.exp (((v+10)/10)- 1))

def fam(v):
	return phi * ((0.01 * v + 25))/(np.exp (((v+25)/10)- 1))

def fah(v):
	return phi * (0.07 * np.exp(v/29))

def fbn(v):
	return phi * (0.125 * np.exp(v/80))

def fbm(v):
	return phi * (4 * np.exp(v/18))

def fbh(v):
	return phi * (1/(np.exp((v+30)/10)+1))

def fn(n):
	return fan(V0) * (1-n) - fbn(V0)*n

def fm(m):
	return fam(V0) * (1-m) - fbm(V0)*m

def fh(h):
	return fah(V0) * (1-h) - fbh(V0)*h

def fv(v):
	s=(I - (gK**(fn(n0)**4))*(v-VK) - (gNa**((fm(m0)**3)*fh(h0)))*(v-VNa) - ((gL)*(v-VL))) / CM
#return (I - (gK**(fn(n0)**4))*(v-VK) - (gNa**((fm(m0)**3)*fh(h0)))*(v-VNa) - ((gL)*(v-VL))) / CM

	t = np.linspace(0, 90, num=5)
V = np.zeros(len(t))
n = np.zeros(len(t))
for i in range(len(t)):
	V1 = V0 + delta * fv(V0 + 0.5 * delta * fv(V0))
	V0 = V1
	n1 = n0 + delta * fn(n0 + 0.5 * delta * fn(n0))
	n0 = n1
	m1 = m0 + delta * fm(m0 + 1/2 * delta * fm(m0))
	m0 = m1
	h1 = h0 + delta * fh(h0 + 1/2 * delta * fh(h0))
	h0 = h1
	V[i] = V1	
	n[i] = n1
plt.plot(t,V )
plt.show()
