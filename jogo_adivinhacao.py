import random

numero_secreto = random.randint(1,100)
palpite = int(input("Adivinhe o número de 1 a 100 (apenas uma chance) "))


if palpite == numero_secreto:
    print("Você acertou!")
else:
    print(f"Errou! O número era {numero_secreto}")
