#como crear un dicc ... son muy usados
punto = {"x": 25, "y": 50} # solo acepta string y siempre "" y :
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["lala"])# dara error ´por que lala no esxiste como llave de punto
if "lala" in punto: # solucion para buscar "lala"
    print("encontre lala", punto ["lala"])

print(punto.get("lala", 97)) # agrega valor 97 por defecto
del punto["x"]
del punto["y"]
print(punto)
punto["x"] = 25
print(punto)

for valor in punto:
    print(valor, punto [valor])

#como acceder a diicionario
    
    for valor in punto.items():
        print(valor)  # nos devuelve duplas

for llave, valor in punto.items():
        print(llave, valor) #otra manera de acceder a diicionarios

#uso mas real de diccionarios
        
usuarios = [
     {"id": 1, "nombre": "Chanchito"},
     {"id": 2, "nombre": "juan"},
     {"id": 3, "nombre": "caball"},
     {"id": 4, "nombre": "Julie"},
]
for usuario in usuarios:
     print(usuario["nombre"])
