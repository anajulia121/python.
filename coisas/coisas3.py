nume = [8.9, 9.2, 8.6, 9.6, 9.3, ]
print(min(nume))

def organizar(cont, voltas):
    if voltas >= len(nume):
        return 
    
    if cont >= len(nume) -1:
      return organizar(0, voltas + 1)

    if nume[cont] < nume[cont + 1]:
       aux = nume[cont]
       nume[cont] = nume[cont + 1]   
       nume[cont + 1] = aux
    
    organizar (cont + 1, voltas)

organizar(0, 0)
print (nume)
