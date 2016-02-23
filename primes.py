def minimo(x,y):
	if x<y:
		return x
	else:
		return y

def mcd(x,y):
	m=minimo(x,y)
	for i in range(m,0,-1):
		if (x%i == 0) and (y%i==0):
			return i
#febrero 18
#la funcion devuelve a 1 si los argumentos son coprimos,0 otro caso
def arecoprime (a,b):
	m=mcd(a,b)
	if m == 1:
		return 1

	else :
		return 0

print  arecoprime (10,12)
