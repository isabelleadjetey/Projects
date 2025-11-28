"""
-	calcola_sconto(prezzo, età)
-	Prende prezzo e età come parametri
-	Se età < 18: sconto 20%
-	Se età >= 65: sconto 30%
-	Altrimenti: nessuno sconto
-	Restituisce il prezzo finale
"""

def calcola_sconto(prezzo, eta):
	if eta <18:
		prezzo = prezzo * (100-20)/100
	elif eta >= 65:
		prezzo = prezzo * (100-30)/100
	return prezzo
#Test
print(calcola_sconto(100, 15))
print(calcola_sconto(100, 70))
print(calcola_sconto(100, 40))

