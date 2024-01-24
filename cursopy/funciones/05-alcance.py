saludo = "Hola Global"

def saludar():
    global saludo
    saludo = "hola Mundo"

def saludachanchito():
    saludo ="Hola Chanchito"
    print(saludo)


print(saludo)
saludar()
print(saludo)
