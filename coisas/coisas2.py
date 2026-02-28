a=input("digite um numero:")
print(a)
b=input("digite um numero:")
print(b)
c=input("digite um numero:")
print(c)
d=input("digite um numero:")
print(d)
nume=[a,b,c,d]
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