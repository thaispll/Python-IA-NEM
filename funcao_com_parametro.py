def celsius_para_f(temp_c):
    return temp_c * 9 / 5 + 32

f = celsius_para_f(25)                  # 77.0
print(f'{celsius_para_f(30):.1f} °F')   # 86.0 °F

def extremos(valores):
    return min(valores), max(valores)   # tupla
menor, maior = extremos([25, 27, 24])
