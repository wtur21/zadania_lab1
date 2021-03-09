# zad. 1

napis = "Jakiś napis"

calk = 2

flo = 2.5

zesp = 2+5j

t = True

f = False

lista = ["abc", "def"]

slo = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D"
}

tup = ("fed", "cba")

print(f'String: "{napis}"')

print(f"Liczbowe: {calk}, {flo}, {zesp}")

print(f"Bool: {t}, {f}")

print(f"Lista: {lista}")

print(f"Słownik: {slo}")

print(f"Tuple: {tup}")

# zad. 2

a = 20

b = 10

print(a + b)

print(a - b)

print(a * b)

print(a / b)

print(a ** b)

print(a % b)

# zad. 3

import math as m

wyr1 = m.e**10

wyr2 = m.sqrt(m.pow(m.log(5 + m.pow(m.sin(8), 2)), 1/6))

wyr3 = m.floor(3.55)

wyr4 = m.ceil(4.80)

print(f"Wynik wyrażenia pierwszego: {wyr1}")

print(f"Wynik wyrażenia drugiego: {wyr2}")

print(f"Wynik wyrażenia trzeciego: {wyr3}")

print(f"Wynik wyrażenia czwartego: {wyr4}")

# zad. 4

imie = "WIKTOR"

nazwisko = "TURSKI"

print(str.capitalize(imie), str.capitalize(nazwisko))

# zad. 5

tekst = "la la la la la la la la la la la la"

print(tekst.count("la"))

# zad. 6

tekst = "Zmienna łańcuchowa awohcucńał anneimZ"

print(tekst[1], tekst[len(tekst) - 1])

# zad. 7

tekst = "Zmienna łańcuchowa awohcucńał anneimZ"

print(tekst.split(" "))

# zad. 8

napis = "Napis napis napis napis"

flo = 24.55

szes = 0x19

print(f"{napis}, {flo}, {hex(szes)}")

# zad. 9

lista = ["koszykówka", "bobslej", "piłka nożna", "tenis", "siatkówka"]

lista.reverse()

lista.append("golf")

lista.append("curling")

print(lista)

# zad. 10

# nie wiedziałem o jakie skróty chodzi to dałem inne

slownik = {
    "HTML": "Hypertext Markup Language",
    "SQL": "Structured Quary Language",
    "WWW": "World Wide Web",
    "CSS": "Cascading Style Sheets",
    "HTTP": "Hypertext Transfer Protocol",
    "SSH": "Secure Shell"
}