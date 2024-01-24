#tuplas no se pueden modificar pero si crear otrsas en base la existente
numeros =(1,2,3)+(4,5,6)
print(numeros)

punto = tuple([1,2])  # la fx tuple recibe iterable
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)
# lo mas importante es que las tuplas no se modifican,
# se crean listas en base a las tuplas y se modifican esas listas
# por ejemplo

listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"   
print(listaNumeros) 