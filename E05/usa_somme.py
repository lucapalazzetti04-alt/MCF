
import somme

def main():
	n=int(input("Inserisci n: "))

	sumprod_n = somme.sumprod(n)
	somma_rad_n = somme.somma_rad(n)
	print("La somma  è: " , sumprod_n[0] )
	print("Il prodotto  è: " , sumprod_n[1] )
	print("La somma  è: " , somma_rad_n)

	a=input("Inserisci a (se lasci vuoto prenderà come valore di default a=1): ")
	if a.strip() == "":
    		a = 1
	else:
    		a = int(a)
	sommatoria = somme.sommatoria(n, a)
	print("La Sommatoria è: ", sommatoria)

if __name__ == "__main__":
	main()
