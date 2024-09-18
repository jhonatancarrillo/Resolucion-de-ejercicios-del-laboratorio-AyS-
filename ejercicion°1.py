# Ejercicio parte 01:

# Ejercicio 1: Longitud del texto 'python', convertir a float y luego a string
texto = "python"
longitud = len(texto)
longitud_float = float(longitud)
longitud_str = str(longitud_float)

print(longitud)
print(longitud_float)
print(longitud_str)
# Ejercicio 2: Comprobar si un número es par
numero = int(input("Ejercicio 2  Introduce un número: "))
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")

# Ejercicio 3 Comprobar si la división entera de 7 entre 3 es igual a 2.7 convertido a entero
division_entera = 7 // 3
valor = int(2.7)
print("Ejercicio 3  División entera es igual a 2.7 convertido a entero:", division_entera == valor)

# Ejercicio 4: Comprobar si el tipo de '10' es igual al tipo de 10
print("Ejercicio 4  ¿El tipo de '10' es igual al tipo de 10?", type('10') == type(10))

# Ejercicio 5: Comprobar si int('9.8') es igual a 10
if int('9.8')==10:
    print("true")
else:
    print("false")

# Ejercicio 6: Calcular el pago de una persona basado en horas trabajadas y tarifa por hora
horas = float(input("Ejercicio 6  Introduce las horas: "))
tarifa = float(input("Introduce la tarifa por hora: "))
salario_semanal = horas * tarifa
print(f"Tu salario semanal es {salario_semanal}")

# Ejercicio 7: Calcular el número de segundos que una persona puede vivir, asumiendo 100 años
anios = int(input("Ejercicio 7  Introduce el número de años que has vivido: "))
segundos_por_anio = 365 * 24 * 60 * 60  # 1 año = 365 días * 24 horas * 60 minutos * 60 segundos
segundos_totales = anios * segundos_por_anio
print(f"Has vivido durante {segundos_totales} segundos.")

# Ejercicio 8: Mostrar la tabla solicitada
print("Ejercicio 8  Tabla:")
for i in range(1, 6):
    print(f"{i} {1} {i} {i**2} {i**3}")

# Ejercicio 9: Invertir una cadena dada por el usuario
cadena = input("Ejercicio 9  Introduce una cadena: ")
cadena_invertida = cadena[::-1]
print(f"Cadena invertida: {cadena_invertida}")

# Ejercicio 10: Contar vocales en una cadena dada por el usuario
cadena = input("Ejercicio 10  Introduce una cadena: ").lower()
vocales = "aeiou"
contador_vocales = sum(1 for letra in cadena if letra in vocales)
print(f"Número de vocales: {contador_vocales}")

# Ejercicio 11: Verificar si una cadena es un palíndromo
cadena = input("Ejercicio 11  Introduce una cadena: ").replace(" ", "").lower()
es_palindromo = cadena == cadena[::-1]
print(f"Es palíndromo: {es_palindromo}")

# Ejercicio 12: Reemplazar espacios con guiones bajos
cadena = input("Ejercicio 12  Introduce una cadena: ")
cadena_reemplazada = cadena.replace(" ", "_")
print(f"Cadena con guiones bajos: {cadena_reemplazada}")

# Ejercicio 13: Contar el número de palabras en una cadena dada
cadena = input("Ejercicio 13  Introduce una cadena: ")
numero_palabras = len(cadena.split())
print(f"Número de palabras: {numero_palabras}")

# Ejercicio 14: Convertir una cadena a mayúsculas y minúsculas
cadena = input("Ejercicio 14  Introduce una cadena: ")
print("Mayúsculas:", cadena.upper())
print("Minúsculas:", cadena.lower())

# Ejercicio 15: Eliminar espacios en blanco al principio y al final de una cadena
cadena = input("Ejercicio 15  Introduce una cadena: ")
cadena_sin_espacios = cadena.strip()
print(f"Cadena sin espacios: '{cadena_sin_espacios}'")

# Ejercicio 16: Extraer una subcadena especificando los índices
cadena = input("Ejercicio 16  Introduce una cadena: ")
inicio = int(input("Introduce el índice de inicio: "))
fin = int(input("Introduce el índice de fin: "))
subcadena = cadena[inicio:fin]
print(f"Subcadena: {subcadena}")

# Ejercicio 17: Verificar prefijo y sufijo en una cadena
cadena = input("Ejercicio 17  Introduce una cadena: ")
prefijo = input("Introduce el prefijo: ")
sufijo = input("Introduce el sufijo: ")
tiene_prefijo = cadena.startswith(prefijo)
tiene_sufijo = cadena.endswith(sufijo)
print(f"Comienza con el prefijo: {tiene_prefijo}")
print(f"Termina con el sufijo: {tiene_sufijo}")
