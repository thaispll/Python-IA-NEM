sensores = ['T01', 'T02']
sensores.append('T03')       # ao final
sensores.insert(0, 'T00')    # na posição 0
sensores.remove('T02')       # pelo valor
ultimo = sensores.pop()      # remove e devolve o último
del sensores[0]              # pelo índice
'T01' in sensores            # True
sensores.index('T01')        # 0
