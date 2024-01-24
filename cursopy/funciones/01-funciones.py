# definimos nuestra propia funcion
def hola(nombre, apellido="sin apellido"): #el segundo parametro lo configuro por si no hay info
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")

hola("ANDY", "ballesteros")
hola("CHANCHITO")


hola(apellido="ballesteros", nombre="Andy")  #se define cual es el apellido y cual el nombre
