tabela = [
    ['T01', 25.0, 63],
    ['T02', 26.5, 58],
]
tabela[1][0]       # 'T02'
tabela[1][1]       # 26.5
for sensor, temp, umid in tabela:
    print(sensor, temp, umid)
