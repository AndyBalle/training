# def suma(a, b, c):  # funcion suma simple
    #print(a + b + c)

def suma(*numeros): # el asterisco me indica que es iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
   
    print(resultado)
 
suma(2, 7, 7, 78)   

#suma(2, 7, 7)