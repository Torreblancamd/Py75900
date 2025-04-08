#TUPLAS

tupla_usuario = ("Jose","Laura", "Mauro","Laura")

print(type(tupla_usuario))

#ACCESO
print( tupla_usuario)
print( tupla_usuario[1])

#MODIFICAR
#tupla_usuario[1] = "Pedro"




#SET 

set_alumnos = {"Marcos","Pedro","Julia","Matias","Julia","Marcos"}

print(set_alumnos)




lista_alumnos = ["Marcos","Pedro","Julia","Matias","Julia","Marcos"]

print(set_alumnos)


copia_set_alumnos = set(lista_alumnos)
print(copia_set_alumnos)



#DICCIONARIOS {}
#LLAVE: NUMERICO, STRING
#VALOR: CUALQUIER TIPO DE DATO


usuarios = { "u1":"Pepe", "u2":"Juan", "u3":"Marta", 6:"Pedro", "u3":"Mauro"}

print(usuarios)

print( usuarios["u2"])
print( usuarios[6])


lista_alumnos = [   {"nombre":"Juan", "edad":30 , "materias":["Lengua","Fisica","Ingles"]},
                    {"nombre":"Marta", "edad":23 , "materias":["Lengua","Fisica","Ingles"]},
                    {"nombre":"Pedro", "edad":22 , "materias":["Programacion","Quimica","Ingles"]},
                    {"nombre":"Marcos", "edad":18 , "materias":["Francesa","Fisica","Natacion"]},
                 ]


print(lista_alumnos)
print(lista_alumnos[1])
print(lista_alumnos[1]["materias"])
print(lista_alumnos[1]["materias"][0])