def exibir(sensor, temp, unidade='°C'):
    print(f'{sensor}: {temp:.1f} {unidade}')

exibir('T01', 25.0)             # T01: 25.0 °C
exibir('T02', 77.0, '°F')       # T02: 77.0 °F
exibir(temp=26, sensor='T03')   # argumentos nomeados

r = exibir('T04', 24.0)
print(r)                        # None
