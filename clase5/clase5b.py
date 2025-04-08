#SCOPE GLOBAL
nombre_global = "Pedro"

def saludar():
    #SCOPE LOCAL
    nombre = "PEPE"
    print(nombre)
    print(f"NOMBRE GLOBAL: {nombre_global}")



saludar()
#print(f"EL NOMBRE DEL USUARIO ES: {nombre}")