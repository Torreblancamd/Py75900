

# ASIGNACION = 
# ARITMETICOS 

# OPERADORES RELACIONES ---->

# MAYOR >  = A ES MAYOR QUE B

print(10 > 5)#T
print( 39 > 40 )#F
print( 10 + 10 > 10 + 5)#T


#MENOR <

print( 22 < 33 )#T
print( "a" < "A")


# == IGUAL

print( 9 == 9 )#T
print( 10 == "10")
print("Juan" == "JUAN")
print("Ramon Lautaro Jimenez" == "RamonLautaroJimenez")



# != DISTINTO 

print( 10 != 10 )#F
print( 5 + 8 != 23 )#V


# >= MAYOR O IGUAL
# <= MENOR O IGUAL
edad = 18
print( edad >= 18 )#T


print( 30 <= 40 )#V





#OPERADORES LOGICOS------> and | or


#AND-----> Y
print( 10 > 5 and 30 == 30 )#T
print( "Juan" == "Juan" and 30 < 20-5 )
print( True == False and 10 > 5  and 30 < 50 )



#OR-----> O
print( 22 < 11 or 55 == 60 )#F


nombre = "Juan"
password = "1234"
print( nombre == "Ramon" or password == "1234" )




#SLICING 

nombre = "Juan Marcos Lopez"

print( nombre[5:10])
print(nombre[5:])
print(nombre[:5])



numeros = [1,2,3,4,5,6,7,8,9,10]

print(numeros[4:7])
#numeros[inicio:fin:paso]
print(numeros[::2])




#F strings

nombre = "Pepe"
edad = 45
nota_uno = 8
nota_dos = 6

print(f"Promedio: {(nota_uno + nota_dos)/2}")