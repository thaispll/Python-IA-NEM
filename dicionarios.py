sensor = {'id': 'T01', 'local': 'Linha 3', 'temp': 25.0}
sensor['local']              # 'Linha 3'
sensor['temp'] = 26.4        # altera
sensor['ativo'] = True       # adiciona nova chave
sensor.get('umid', 'n/d')    # 'n/d' (evita KeyError)
del sensor['ativo']
len(sensor)                  # 3
