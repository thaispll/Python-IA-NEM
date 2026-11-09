ponto = (-22.9, -43.2)        # latitude, longitude
ponto[0]                      # -22.9
ponto[0] = 0                  # TypeError: imutável
lat, lon = ponto              # desempacotamento
LIMITES = (70, 90)            # dados que não devem mudar
