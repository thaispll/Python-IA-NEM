while True:
    cmd = input('Comando: ').strip().lower()
    if cmd == 'sair':
        break           # encerra o laço
    if cmd == '':
        continue        # volta ao início
    print(f'Executando {cmd}')
