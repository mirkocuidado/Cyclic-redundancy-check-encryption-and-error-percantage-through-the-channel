import numpy as np
import random
import matplotlib.pyplot as plt


# KLASICAN XOR

def xor(a, b): 
 
    rezultat = [] 
 
    for i in range(1, len(b)): 
        if (a[i] == b[i]): 
            rezultat.append(0) 
        else: 
            rezultat.append(1) 
  
    return rezultat

# RACUNANJE OSTATKA NA DRUGACIJI NACIN POMOCU DUZINE DELIOCA I OPERACIJE XOR

def special_poly_div(ix, g, brG):

    delic = ix[0 : brG] 
  
    while brG < len(ix): 
  
        if (delic[0] == 1): 
            delic = xor(g, delic) + [ix[brG]]
        else:
            delic = xor([0]*brG, delic) + [ix[brG]]
  
        brG = brG + 1
  
    if (delic[0] == 1): 
        delic = xor(g, delic) 
    else: 
        delic = xor([0]*brG, delic) 
   
    return delic

def crc(i, g): 
  
    ix = i + [0]*(brG-1)

    cypher = i + special_poly_div(ix, g, brG)

    return cypher
  

pKanal = 0
paket = 0

iDelovi = []

pKanala = [0.1, 0.01, 0.001, 0.0001]
rezultati = []

i = []

for ind in range(0,1000000):
	if(random.uniform(0,1)>0.5):	
		i.append(1)
	else:
		i.append(0)

# OVDE SE MOZE PROMENITI VREDNOST ULAZNOG POLINOMA g(x):

g = [1,1,1,0,1,0,1,0,1,1,1,0,1,0] # OVO JE VREDNOST KOJU SAM SLUCAJNO ODABRAO

brG = len(g)

paket = input("Unesite velicinu paketa za kanal:")
paket = int(paket)
while(paket<=0):
	paket = input("Neispravna vrednost. Unesite velicinu paketa za kanal ponovo:")
	paket = int(paket)

pocetak = 0
kraj = paket
duz = len(i) / paket
ostatak = len(i) % paket

iKanal = []

#ISECKATI NA DELOVE ODREDJENE VELICINE:

if(len(i)!=paket):
	if(duz == 0):
		iDelovi = i
	else:
		while(duz!=0):
			iDelovi.append(i[pocetak:kraj])
			pocetak = kraj
			kraj = kraj + paket
			duz = duz - 1
		if(ostatak>0):
			iDelovi.append(i[pocetak:])

	for ind in iDelovi:
		cypher = []

		cypher = crc(ind, g)

		iKanal.append(cypher)
else:
	cypher = []
	cypher = crc(i, g)

	iKanal.append(cypher)


# PROVESTI OVU SEKVENCU KROZ KANAL I ZA SVAKU OD VEROVATNOCA VIDETI KOLIKO JE USPESNO PRENETIH PAKETA:

brojac = 0
brojac1 = 0
iPosleKanala = []

pomoc = []
lucky = []

flag = True

for abc in iKanal:
	for fed in abc:
		pomoc.append(fed)
	lucky.append(pomoc)
	pomoc = []

for pKanal in pKanala:

	iPosleKanala = []
	iKanal = []

	for abc in lucky:
		for fed in abc:
			pomoc.append(fed)
		iKanal.append(pomoc)
		pomoc = []

	for i in iKanal:

		pazi = []

		for ind in range(0,len(i)):

			if(random.uniform(0,1) < pKanal and i[ind]==1):
				pazi.append(0)
			elif(random.uniform(0,1) < pKanal and i[ind]==0):
				pazi.append(1)
			else:
				pazi.append(i[ind])

		pomocnik = special_poly_div(pazi,g, brG)

		if(pomocnik.count(1)==0):
			brojac1 = brojac1 + 1

			for blabla in range(0,len(i)):
				if(pazi[blabla]!=i[blabla]):
					flag = False
					break

			if(flag):
				brojac = brojac + 1

			flag = True

	rezultati.append(brojac)

	#print("Verovatnoca greske u kanalu: %f" %(pKanal))
	#print("Broj blokova za koje je A = 0: %d" %(brojac1))
	#print("Broj uspesno prenetih blokova: %d" %(brojac))
	#print("")

	brojac = 0
	brojac1 = 0

#ISCRTAJ:

plt.plot(pKanala, rezultati) 
plt.xlabel('VEROVATNOĆA GREŠKE U KANALU') 
plt.ylabel('BROJ USPEŠNO PRENETIH PAKETA') 
plt.title('Domaći') 
  
plt.show() 