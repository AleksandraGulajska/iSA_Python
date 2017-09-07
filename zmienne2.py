print("Hello World!")

zdanie = "cos tam costam"
zdanie.capitalize()
print(3 * zdanie)
imie = "ala"

print(zdanie + " " + imie.capitalize())

print("{} {}".format(zdanie, imie.capitalize()))
print("{1} {0}".format(zdanie, imie.capitalize()) )

imie2 = imie.capitalize()
print(imie2)

a=2
b=6
print(a+b)
print( "jola".capitalize().replace('o', "O"))
cytat = 'Ania powiedziala "bla bla"'
cytat2 = "Ania powiedziala \"bla bla\""
print(cytat + "\n" + cytat2)

dlugosc_wyrazu = len("abrakadabra")
print(dlugosc_wyrazu)

slowo = "abrakadabra"
print("Slowo {} ma {} liter".format(slowo, dlugosc_wyrazu))
print(f"Slowo {slowo} ma {dlugosc_wyrazu} liter".format(slowo, dlugosc_wyrazu))

#indeksowanie
print(slowo[0])
print(slowo[9])
print(slowo[-3]) #liczac od konca wyrazu

print(slowo[len(slowo)-1])

slowo2 = "czarymary"
print(slowo2[2:5])
print(slowo2[:5])
print(slowo2[2:7:2])

#numer porzadkowy kodu ASCI
kod = ord("D")
print(kod)
#zamienia numer na listere ASCI
# kod = 68 + 4
print(chr(kod+4))

