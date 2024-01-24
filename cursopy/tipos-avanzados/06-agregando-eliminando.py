mascotas = ["tomy", "pulga", "Euro", "Andy", "chanchito", "pulga", "banana"]

mascotas.insert(1, "melvin")
mascotas.append("chanchito triste")

mascotas.remove("pulga") # elimina el primero que encuentre 
mascotas.pop(1) #borra el elemento 1  
del mascotas[0] #borra el primer elemento
mascotas.clear()# borra todo
print(mascotas) 