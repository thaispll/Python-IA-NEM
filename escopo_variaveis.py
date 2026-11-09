LIMITE = 70                    # global

def verificar(temp):
    excesso = temp - LIMITE    # local: só existe aqui
    return excesso > 0

verificar(75)                  # True
print(excesso)                 # NameError
