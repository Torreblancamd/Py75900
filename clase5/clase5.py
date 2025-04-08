

#la funcion mayor de 
"""
def mayor_de_edad( edad:int ):
    if type(edad) == int:    
        if edad >= 18:
            print("El usuario es mayor de edad")
            print(type(edad))
        else:
            print("El usuario no es mayor")
    else:
        print(f"Tipo de datos incorrecto: {type(edad)}")



mayor_de_edad(18)
mayor_de_edad(10)
mayor_de_edad(39)
mayor_de_edad(6)
mayor_de_edad("Pedro")"
""
"""

#1:10%  3:40% 6:60% 12:90%

def calcular_interes(monto:int , cuotas:int):
    interes = 0
    if cuotas == 1:
        interes = monto * 0.10
        return interes        
    elif cuotas == 3:
        interes = monto * 0.40
        return interes
    elif cuotas == 6:
        interes = monto * 0.60
        return interes
    elif cuotas == 12:
        interes = monto * 0.90
        return interes
    
    


def datos_prestamo(monto,cuotas,interes):
    print("<-----DATOS DEL PRESTAMO------->")
    print(f"Monto: {monto}")
    print(f"Monto: {cuotas}")
    print(f"Monto total: {monto+interes}")
    print(f"Pagas por cuota: {(monto+interes)/cuotas}")




print("Bienvenidos/as a Prestamo Ya")
monto = int(input("Ingrese el monto que quiere solicitar"))
cuotas = int(input("Cuotas: 1,3,6 y 12"))
interes = calcular_interes(monto,cuotas)
datos_prestamo(monto,cuotas,interes)
