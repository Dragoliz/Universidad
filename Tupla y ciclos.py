
print("2da actividad de programación 1 - Tuplas, listas y ciclos.\n")
print("4.1 Implemente una tupla de un solo elemento. Tiene una particularidad, investigue. (2pts.)\n")

tupla1=(101,)
print(tupla1[0], "- La particularidad es la existencia de una ',' en la declaración de la variable.\n")

vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]
print("4.2 Dada una lista de las edades de una población que ha ido a vacunarse, Elimine de la lista, todas las ocurrencias del entero 10 (3pts)")

print("Las edades:")
print(vEdades)
print("\n")

for x in vEdades:
    if x == 10:
        vEdades.remove(x)
    
print("Las edades depuradas:")
print(vEdades)

print("\nMuchas gracias por usar mi programa \nDiego Estrada CI:28.055.122")
