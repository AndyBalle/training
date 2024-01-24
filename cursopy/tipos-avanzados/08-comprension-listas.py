#queremos a ese listado 
#de ususariosno devuelvallista nobres
usuarios = [
    ["chanchito", 4],
    ["Andy", 1],
    ["Bobi", 5]
]
# nombres=[]
# for ususario in usuarios:
#     nombres.append(ususario[0])
# print(nombres)
#una forma mas elegante para hacer lo de la lineas anteriores

# nombres=[usuario[0] for usuario in usuarios] #mas alegante

#nombres =[usuario for usuario in usuarios if usuario[1]>2] #filtramayoresde 2
#nombres =[usuario[0] for usuario in usuarios if usuario[1]>2] #filtra y transofrma
#nombres = list(map(lambda usuario: usuario[0], usuarios)) #lomismo de arriba pero con lenguaje universal otros lenguajes
#print(nombres)
menosUsuarios = list(filter(lambda usuario: usuario[1]>2, usuarios))
print(menosUsuarios)

#la misma operacion de las dos formas 

