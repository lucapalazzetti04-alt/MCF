import math
def sumprod(n):
	if n<0:
		raise ValueError("N deve essere >=0")
	somma=0
	prodotto=1
	for i in  range(1, n+1):
		somma += i
		prodotto *= i 
	return somma, prodotto

def somma_rad(n):
        if n<0:
                raise ValueError("N deve essere >=0")
        somma_rad=0
        for i in  range(1, n+1):
                somma_rad += math.sqrt(i)
        return somma_rad

def sommatoria(n, a=1):
	if n<0:
                raise ValueError("N deve essere >=0")
	sommatoria=0
	for i in range(0, n+1):
		sommatoria += i**a
	return sommatoria
