
#comparamos la longitud de mi nombre con la longitud de mi apellido

nombre = (input("Introduzca su nombre: "))

apellido1 = (input("introduzca su primer apellido: "))
apellido2 = (input("Introduzca su segundo apellido: "))

print("Longitud de tu nombre es ", len(nombre))
print("Longitud de tu apellido es", len(apellido1 + apellido2))

if len(nombre) < len(apellido1 + apellido2):
    print("La longitud de tus apellidos es mayor que la de tu nombre")
elif len(nombre) > len(apellido1 + apellido2):
    print("La longitud de tu nombre es mayor que la de tus apellidos ")
else: 
    print("La longitud de tu nombre es igual a la longitud de tus apellidos")






