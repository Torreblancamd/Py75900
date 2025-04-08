

#LISTA

lista_usuarios = []
#lista_alumnos = list()

lista_usuarios = ["Lu", "Romeo","Marcos","Marta","Julia"]

print(lista_usuarios)

#ORDENADAS----->INDEX
#ACCESO
print( lista_usuarios[0])
print( lista_usuarios[2])
print( lista_usuarios[1] + lista_usuarios[4])



lista_random = [10 ,20 , "Pedro", True, 22.2, ["Azul", "Rojo","Verde"] , 8.3]

print(lista_random[2])
print(lista_random[6])
print(lista_random[5][1])



#MUTABLES 

lista_usuarios[0] = "Romina"
print(lista_usuarios)

#lista_usuario = "Pedro"


#METODOS

#APPEND
# . OPERADOR DOT--->

lista_usuarios.append("Laura")
print("Lista despues del append: ", lista_usuarios)


#INSERT 

lista_usuarios.insert(3, "Mauro")
print("Lista depsues del insert: ", lista_usuarios)



#POP
lista_usuarios.pop()
print("Lista despues del POP: ", lista_usuarios)

#POP + INDEX
lista_usuarios.pop(1)
print("Lista despues del POP+INDEX: ", lista_usuarios)


#POP + INDEX
usuario_eliminado = lista_usuarios.pop(1)
print("Lista despues del POP+INDEX: ", lista_usuarios)
print("Se elimino al usuario: ", usuario_eliminado)


#REMOVE 

lista_usuarios.remove("Mauro")
print("Lista despues del REMOVE: ", lista_usuarios)


#OJO
#lista_usuarios.remove("Lautaro")
#print("Lista despues del REMOVE: ", lista_usuarios)


#INDEX

print( lista_usuarios.index("Marta"))


print( len(lista_usuarios))