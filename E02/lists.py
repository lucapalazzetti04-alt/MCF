

lgg = [ 'lunedi', 'martedi', 'mercoledi', 'giovedi', 'venerdi', 'sabato', 'domenica']
primo_ottobre=2
ottobre_2025 =[]
for i in range(31):
	indice=(primo_ottobre +i ) % 7
	ottobre_2025= ottobre_2025 + [lgg[indice]]
ottobre_dict = {}
for j in range(1,32):
	ottobre_dict[j]= ottobre_2025[j-1]
print(ottobre_dict)
