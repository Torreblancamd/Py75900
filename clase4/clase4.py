

#IF---->SI
edad =  22

if edad >= 18:
    print("Bienvenido/a")
    print("Muestro el menu")




num_a = input("Ingrese un numero")
num_b = input("Ingrese un numero")
operacion = input("Ingrese Suma(+) o Resta(-)")


if operacion == "+":
    suma = int(num_a) + int(num_b)
    print(f"Suma: {suma}")
elif operacion == "-":
    resta = int(num_a) - int(num_b)
    print(f"Resta: {resta}")
elif operacion == "*":
    multi = int(num_a) * int(num_b)
    print(f"Multiplicacion: {multi}")
else:    
    print(f"Operacion no encontrada: {operacion}")






usuario = input("Ingrese su nombre de usuario")
password = input("Ingrese su password")


if usuario == "Pepe" and password == "123abc":
    print(f"Bienvenido al sistema {usuario}")
else:
    print(f"Usuario incorrecto: {usuario}")
