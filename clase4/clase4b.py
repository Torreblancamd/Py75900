"""
nombre = ""

while nombre != "FIN":
    nombre = input("Ingrese su nombre")
    print(f"Bienvenido/a: {nombre}")


"""


#PIDO UN NUMERO POR TECLADO Y MUESTRO EL SIGUIENTE POR CONSOLA
#SE FINALIZA CUANDO SE INGRESE UN NUMERO NEGATIVO
"""
total = 0

while total >= 0:
    num = int(input("Ingrese un numero positivo y le muestro siguiente"))
    if num >= 0:
        print(f"Ingreso el num: {num}")
        print(f"El siguiente es: {num+1}")
    else:
        print(f"Ingreso el numero negativo {num}, chau")


"""

"""
Establezca el total en 0 para empezar. Mientras el total sea 50 o menos, pedir al usuario que ingrese un número. 
Sumar ese número al total e imprime el mensaje “El total es… [total]”. Detener el ciclo cuando el total es más de 50.
"""

total = 0

while total <= 50:
    print(f"Total: {total}")
    num = int(input("Ingrese un numero"))
    total = total + num