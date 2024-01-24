lista1=[1, 2, 3, 4]
print(1,2,3,4)
print(*lista1) #si le ponemos asterisco osea iterable devuelve lo mismo

lista2=[5, 6]

combinada =["hola ", *lista1, "hola mundo", "Chanchito"] 
print(combinada)
#otra manera desempaquetar dicionarios 
punto1= {"x":19, "y":"hola "}
punto2= {"y":20}
    #desempaquetamos dicionario
nuevoPunto={**punto1, "lala":"hola mundo", **punto2, "Hola cabezon":"hello"}    
print(nuevoPunto)

