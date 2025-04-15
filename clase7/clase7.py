

class Persona:
    def __init__(self,nombre:str,apellido:str,dni,telefono,direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"Nombre:{self.nombre} Apellido:{self.apellido} Dni:{self.dni} Telefono:{self.telefono}"    

    def saludar(self):
        print(f"{self.nombre}: Hola")



class Alumno(Persona):
    
    def __init__(self,nombre,apellido,dni,telefono,direccion,legajo,materias=None):
        super().__init__(nombre,apellido,dni,telefono,direccion)
        self.legajo = legajo
        if materias is None:
            self.materias = []
        else:
            self.materias = materias        


    def __str__(self):
        return f"Nombre:{self.nombre} Apellido:{self.apellido} Dni:{self.dni} Legajo:{self.legajo} Materias:{self.materias}"      

    def saludar(self):
        print(f"Soy el alumno {self.nombre}")


    def add_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)
            print(f"Materia agregada {materia}")
        else:
            print(f"El alumno ya se encuentra cursando la materia {materia}")


persona_uno = Persona("Pepe","Rojas",31231313,1125432123,"Calle Falsa 123")

print(persona_uno)

persona_uno.saludar()


alumno_uno = Alumno("Juan","Lopez",123123123,1522334455,"San Martin 321","L2025")

print( alumno_uno)

alumno_uno.add_materia("Programacion")
alumno_uno.add_materia("Programacion")
alumno_uno.add_materia("Programacion")
alumno_uno.add_materia("Programacion")
alumno_uno.add_materia("Fisica")

print( alumno_uno)