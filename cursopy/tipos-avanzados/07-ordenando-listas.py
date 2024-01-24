numeros = [2, 4, 1, 45, 75, 22]

#numeros.sort(reverse=True)  #lista numeros en orden descente
numeros2 = sorted(numeros)  #sorted ordena numeros
print(numeros)  
print(numeros2)

usuarios = [
    ["chanchito", 4],
    ["Andy", 1],
    ["Bobi", 5]
]

def ordena(elemento):
    return elemento[1]

# usuarios.sort(key=ordena, reverse=True)
usuarios.sort(key=lambda el:el[1], reverse=True)

print(usuarios)

