# Ejercicio 10: Calculadora de Promedio
numeros = input("Introduce una serie de números separados por comas: ").split(',')
suma = 0
for numero in numeros:
    suma += float(numero)
promedio = suma / len(numeros)
print(f"El promedio de los números es: {promedio}")
