import numpy as np

def rwalk(m):
	a=range(m)
	p=0
	for h in range(m):
		lista=["cara","sello"]
		a[h] = np.random.choice(lista)
	print a[h]

	if a[h] == 'cara':
		p=p+1
	else:
		p=p-1
	return p
print rwalk(100)

	
