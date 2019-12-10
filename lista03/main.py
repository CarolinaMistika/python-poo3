from canal import Canal
from iterator import Iterator

canais = []
canais.append(Canal("Globo"))
canais.append(Canal("Record"))
canais.append(Canal("TV união"))
canais.append(Canal("MTV"))
canais.append(Canal("Netflix"))
canais.append(Canal("Disney+"))
canais.append(Canal("History"))

iterator = Iterator(canais)
print("PROXIMOS CANAIS")
print(iterator.next().nome)
print(iterator.next().nome)
print(iterator.next().nome)
print(iterator.next().nome)
print(iterator.next().nome)
print(iterator.next().nome)
print(iterator.next().nome)
print("CANAIS ANTERIORES")
print(iterator.after().nome)
print(iterator.after().nome)
print(iterator.after().nome)
print(iterator.after().nome)
print(iterator.after().nome)
print(iterator.after().nome)
print(iterator.after().nome)
print("PRIMEIRO CANAL")
print(iterator.first().nome)
print("ULTIMO CANAL")
print(iterator.last().nome)

