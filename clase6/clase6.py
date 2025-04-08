#Crear un metodo que muestre el estado del alumno/a: get_estado-->RECURSA(1,2,3),RECUPERA(4,5,6),APROBADO(7,8,9,10)

#MODIFICAR sacar las propiedades nota_uno y nota_dos
# Ahora la propiedad es materias y cada materia tiene sus 2 notas + promedio final
#Crear 


class Alumno:

    #METODOS
    def __init__(self, nombre:str , dni:int):
        #PROPIEDADES
        self.nombre_alumno = nombre
        self.dni_alumno = dni
        self.nota_uno = 0
        self.nota_dos = 0
        self.promedio = 0

    def get_datos(self):
        print("<----- DATOS DEL ALUMNO ----->")
        print(f"Nombre:{self.nombre_alumno}")
        print(f"DNI:{self.dni_alumno}")


    def set_nota_uno(self,nota):
        if type(nota == float):
            if nota >= 1 and nota <= 10:
                self.nota_uno = nota
            else:
                print(f"Error nota no fue cargada")
        else:
            print(f"Tipo de datos incorrecto {type(nota)}")
    


alumno_uno = Alumno("Pepe",3827183)
alumno_dos = Alumno("Marta",6251523)
print(alumno_uno)

#OPERADOR DOT/PUNTO 
print(alumno_uno.nombre_alumno)
print(alumno_uno.dni_alumno)
#DATOS ALUMNA 2
print(alumno_dos.nombre_alumno)
print(alumno_dos.dni_alumno)


#PRIMER LLAMADO A UN METODO
alumno_uno.get_datos()
alumno_dos.get_datos()



#PROPIEDADES 
print(alumno_uno.nota_uno)

alumno_uno.set_nota_uno(10)

print(alumno_uno.nota_uno)
