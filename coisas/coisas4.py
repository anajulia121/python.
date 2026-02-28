nume  = [8.9, 9.2, 8.6, 9.6, 9.3]
tempo = [12, 13, 13, 14, 14]

menor_tempo = min(tempo)
indice = tempo.index(menor_tempo)

print(nume[indice], "km em", tempo[indice], "min")
