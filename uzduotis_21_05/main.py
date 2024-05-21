# *** Pirma Uzduotis ***
from typing import List

print("Hello, World!")

# *** Antra Uzduotis ***

# Integer tik skaiciai be kablelio
x = 10

# Float skaiciai su kableliu
y = 3.14

# String sudarytas is raidziu
name = "Linas"

# Boolean tai tik dvi reiksmes Taip/Ne
ar_lempa_dega = 'True'

# *** Trecia Uzduotis ***
vardas = input('Koks tavo vardas? -> ')
metai = input('Ir kiek jums metu? -> ')

print('Jusu vardas', vardas, 'Ir jums metu', metai)

# *** Ketvirta uzduotis ***

tv_kanalai = []

tv_kanalai.append('LTV')
tv_kanalai.append('LNK')
tv_kanalai.append('BTV')
tv_kanalai.append('TV3')
tv_kanalai.append('TV6')
print(tv_kanalai)

pasalinti = input('Kuri kanala norite pasalinti? -> ')
tv_kanalai.remove(pasalinti)
print('Po pasalinimo liko -> ', tv_kanalai)
prideti = input('Koki pridetumete kanala? -> ')
tv_kanalai.insert(0, prideti)
print('Siuo metu yra kanalu -> ', tv_kanalai)
tv_kanalai.reverse()
print(tv_kanalai)
tv_kanalai.sort()
print(tv_kanalai)


# *** Penkta uzduotis ***

studentas ={'Vardas': 'Linas', 'Metai': 37, 'Isilavinimas': 'vidurinis'}
print(studentas)
studentas['DevOPS'] ='Pradedantysis'
print(studentas)
studentas['Metai'] =38
print(studentas)
studentas.clear()

# *** Sesta uzduotis ***

pirmas =('Vienas', 'Du', 'Trys', 'Keturi', 'Penkti')

print(pirmas + pirmas)
print(pirmas[0])
print(pirmas[1])
print(pirmas.index('Du'))
print(pirmas.index('Trys'))