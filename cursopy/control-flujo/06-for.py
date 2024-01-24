buscar = 10
for numero in range(5): # range(5) es un iterable
    print(numero)
    if numero== buscar:
        print("encontrado", buscar)
        break
else: 
    print("No encontre el numero buscado")

for char in "ultimate python":
    print(char)

    # print(numero)
    # print(numero, numero * 'Hola mundo')