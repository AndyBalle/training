# set grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}  # remueve los duplicados
segundo =[3, 4, 5]
segundo = set(segundo)  #trasnformamos la lista a un set
#primer.add(5)
#primer.remove(1)

#print(segundo | primer)  # | union 
#print(segundo & primer)   # & interseccion
# print(primer - segundo) #interseccion
print(primer ^ segundo)  # elimina los comunes

#los sets no se encuentran ordenados ojo no se puede acceder por [0]