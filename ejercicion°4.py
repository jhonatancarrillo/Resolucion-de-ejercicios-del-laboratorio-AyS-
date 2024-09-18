
#Hallando la radio y area de un circulo

PI = 3.14
radio = 30

# Calcular el área del círculo
area_of_circle = PI * (radio ** 2)

# Calcular la circunferencia del círculo
circum_of_circle = 2 * PI * radio

# Mostrar los resultados
print("El área del círculo es:", area_of_circle, "metros cuadrados")
print("La circunferencia del círculo es:", circum_of_circle, "metros")

# Calculando el area tomando radio como entrada del usuario
PI = 3.14
radio = float(input("Ingrese la radio para calcular el area: "))

# hallamos el resultado
area_of_circle = PI * (radio ** 2)
print(f"El area del circulo con radio {radio} es:", area_of_circle, "metros cuadrados" )

# utilizamos la función de entrada incorporada
# Usar la función de entrada para obtener los detalles del usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
edad = input("Ingrese su edad: ")

# Mostrar los valores capturados
print("Nombre:", nombre)
print("Apellido:", apellido)
print("País:", pais)
print("Edad:", edad)

