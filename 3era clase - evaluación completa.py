from math import pi
print("Clase 3 - Actividad evaluada.")

def CalcularAreaCircular(): 
    print("\n5.1 Defina una función en python que acepte el radio y devuelva el valor del area de un círculo de esas dimensiones. (4pts)")
    print("\nCalculo de area circular según su radio")
    radio = float (input ("Por favor, ingrese el radio del circulo:"))

    AreaCircular = pi * radio ** 2
    print("El area del circulo es: ", AreaCircular)

def CalcularNumeroMayor():
    print("\n5.2 Defina una función en python que acepte 3 valores y devuelva solo el máximo de los tres. (7pts)")
    Numeros=[1,2,3]
    i=0
    NumeroMayor = 0
    print("Ingrese el valor de los 3 numeros<>:")

    while i<3:          
        Numeros[i] = input ()
        i=i+1

    if Numeros[1]>=Numeros[2]:
        NumeroMayor=Numeros[1]
        if Numeros[0]>=Numeros[1]:
            NumeroMayor=Numeros[0]
    
    if Numeros[0]>=Numeros[1]:
        NumeroMayor=Numeros[0]
        if Numeros[2]>=Numeros[0]:
            NumeroMayor=Numeros[2]
    
    if Numeros[2]>=Numeros[1]:
        NumeroMayor=Numeros[2]
        if Numeros[0]>= Numeros[2]:
            NumeroMayor=Numeros[0]
    print("El número mayor es: ", NumeroMayor)


def CalcularSumaDeImpares():
    print("\n5.3 Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista. (7pts)")
    CantidadDeNumeros=float(input("\n¿Cuántos numeros desea agregar?"))
    CantidadDeNumeros -= 1
    Numero= 0
    ListaDeNumeros =[]
    SumaDeImpares=0
    Residuo=0

    while CantidadDeNumeros >= 0 :
        Numero=input("Añada un número: ")
        ListaDeNumeros.append(float (Numero))
        CantidadDeNumeros-=1

    Numero=len(ListaDeNumeros)-1
    while Numero >=0:
        Residuo=ListaDeNumeros[Numero]%2

        if Residuo == 1 :
            SumaDeImpares+=ListaDeNumeros[Numero]

        Numero-=1
    print("\nLos numeros en la lista son:",ListaDeNumeros)
    print("La suma de los impares es:",SumaDeImpares)

def CentradoDeTexto():
    print("\n5.4 Desarrolle una función en python que acepte una variable string como primer parámetro y la cantidad de caracteres de como segundo parámetro. La función debe retornar un nuevo string que consista en el string original y el número correcto de caracteres necesarios para que el string se salga centrado. No agregue caracteres al final del string. (10pts)")
    Texto=input("\nEscriba el texto a centrar:")
    Espacios=int (input("Cuánto espacios desea que ocupe todo el texto:"))
    print("Texto centrado a continuación:\n")
    len(Texto)
    print (len(Texto))
    print (Texto.center(Espacios,"-"))
    print (Texto.center(Espacios,))
opcion=1
ProbarPrograma=1
while ProbarPrograma==1:
    print("\n1-Calcular área de un circulo.")
    print("2.-Determinar el número mayor entre 3 entradas.")
    print("3.-Calcular la suma de numeros impares.")
    print("4.-Centrado de texto.\n")
    opcion=int(input("¿Qué opción desea probar?... "))

    if opcion==1:
        CalcularAreaCircular()
        print("\n¿Desea continuar probando el programa?")
        print("1.-Sí")
        print("2.-No")
        opcion=int(input("opcion:"))
        if opcion==1:
            ProbarPrograma=1
        elif opcion==2:
            ProbarPrograma=0
        else :
            print("Entrada invalida, se cerrará el programa.")
            ProbarPrograma=0
            input()
 
    elif opcion==2:
        CalcularNumeroMayor()
        print("\n¿Desea continuar probando el programa?")
        print("1.-Sí")
        print("2.-No")
        opcion=int(input("opcion:"))
        if opcion==1:
            ProbarPrograma=1
        elif opcion==2:
            ProbarPrograma=0
        else :
            print("Entrada invalida, se cerrará el programa.")
            ProbarPrograma=0
            input()
    elif opcion==3:
        CalcularSumaDeImpares()
        print("\n¿Desea continuar probando el programa?")
        print("1.-Sí")
        print("2.-No")
        opcion=int(input("opcion:"))
        if opcion==1:
            ProbarPrograma=1
        elif opcion==2:
            ProbarPrograma=0
        else :
            print("Entrada invalida, se cerrará el programa.")
            ProbarPrograma=0
            input()
    elif opcion==4:
        CentradoDeTexto()
        print("\n¿Desea continuar probando el programa?")
        print("1.-Sí")
        print("2.-No")
        opcion=int(input("opcion:"))
        if opcion==1:
            ProbarPrograma=1
        elif opcion==2:
            ProbarPrograma=0
        else :
            print("Entrada invalida, se cerrará el programa.")
            ProbarPrograma=0
            input()
    else:
        print("Entrada invalida, por favor vuelva a intentar...")
        input()
print("\nMuchas gracias por usar mi programa \nDiego Estrada CI:28.055.122")
