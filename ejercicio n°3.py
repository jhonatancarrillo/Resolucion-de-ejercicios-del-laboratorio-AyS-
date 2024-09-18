# Ejercicio 3: Operaciones con tres listas de números enteros
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

# a. Convierte las listas en conjuntos
set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

# b. Conjunto de todos los números presentes en las tres listas
comunes_tres_listas = set1 & set2 & set3
print(f"Presentes en las tres listas: {comunes_tres_listas}")

# c. Conjunto de todos los números presentes en al menos una de las listas
presentes_una_lista = set1 | set2 | set3
print(f"Presentes en al menos una lista: {presentes_una_lista}")

# d. Conjunto de todos los números presentes en la primera lista pero no en la última
presentes_primera_no_ultima = set1 - set3
print(f"Presentes en la primera lista pero no en la última: {presentes_primera_no_ultima}")

# e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla
tupla_comunes = tuple(comunes_tres_listas)
tupla_presentes = tuple(presentes_una_lista)
tupla_primera_no_ultima = tuple(presentes_primera_no_ultima)

if tupla_comunes:
    suma_comunes = tupla_comunes[0] + tupla_comunes[-1]
else:
    suma_comunes = 0
if tupla_presentes:
    suma_presentes = tupla_presentes[0] + tupla_presentes[-1]
else:
    suma_presentes = 0
if tupla_primera_no_ultima:
    suma_primera_no_ultima = tupla_primera_no_ultima[0] + tupla_primera_no_ultima[-1]
else:
    suma_primera_no_ultima = 0

print(f"Suma de primer y último elemento en comunes: {suma_comunes}")
print(f"Suma de primer y último elemento en presentes: {suma_presentes}")
print(f"Suma de primer y último elemento en primera no última: {suma_primera_no_ultima}")