#fecha 29 de marzo 

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

T=6.3

phi= (3**T-6.3)/10

v=-65

an=phi*(0.01*(v+10)/np.exp(((v+10/10)-1)))

bn=phi*(0.125*(np.exp(v/80)))

n0=0.317

delta=0.001

n1=(an*(1-n0)-bn*n0*)*delta+n0

I=15
gk=36
vk=-77
gNa=120
vna=50


