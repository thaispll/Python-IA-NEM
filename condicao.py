#Entrada de dados
nota = float(input("Digite a sua nota (0 a 10) \n"));


if nota >= 6.0:
    print("Parabéns, você foi aprovado!")
elif (nota >= 5.0 and nota <6.0):
    print("Você ficou de recuperação, tente novamente")
else:
    print("Você está reprovado!")