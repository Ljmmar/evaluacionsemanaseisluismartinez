def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio


numeros = []
for i in range(10):
    numero = float(input("Ingrese el número {}: ".format(i + 1)))
    numeros.append(numero)


promedio = calcular_promedio(numeros)


print("El promedio de los números ingresados es:", promedio)
 
