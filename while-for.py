frutas = ["maçã", "banana", "uva", "morango"] #lista
"""print(frutas[0])

for i in range(5):
    print(i)

for fruta in frutas:
    print(fruta)*/"""

for indice, fruta in enumerate(frutas):
    print(f"Na posição {indice} está a {fruta}")