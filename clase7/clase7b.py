

def division(num_uno , num_dos):

    num_uno = int(num_uno)
    num_dos = int(num_dos)

    return num_uno / num_dos



try:
    resultado = division(10,0)
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("No se puede dividir por 0")
    resultado = division(10, 2)
except:
    print("No se puede dividir por 0")
else:
    print(f"{resultado}")

