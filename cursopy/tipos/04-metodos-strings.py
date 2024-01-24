animal = "  chanchito feliz  "
print(animal.upper())  #mayusculas
print(animal.lower())
print(animal.capitalize())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.strip())  # espacios a la derecha del string
print(animal.find("cha"))
print(animal.replace("an", "T"))
print("nCH" in animal)   # si encuentra el caracter devuelve bollean
print("nCH" not in animal)