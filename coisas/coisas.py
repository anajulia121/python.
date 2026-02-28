nume=[4,5,1,2,8,9,7,6,3]
def organizar(cont,voltas):
    if voltas>=len(nume):
        return
    if cont>=len(nume)-1:
        return organizar(0,voltas+1)
    if nume[cont]>nume[cont+1]:
        aux=nume[cont]
        nume[cont]=nume[cont+1]
        nume[cont+1]=aux
        print(nume)
    organizar(cont+1,voltas)
organizar(0,0)
print(nume)




