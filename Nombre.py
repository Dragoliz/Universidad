from distutils.command.clean import clean


Continuar=True


while Continuar==True:
        print("\n1ra actividad de programación \nToma e impresión de nombre \n")
        Nombre = input("Por favor, ingrese su nombre completo:")
        print("\nSu nombre completo es: " + Nombre + "\n")
        print("¿Desea volver a probarlo?")
        Respuesta = input("Responda con si o no \n Respuesta: ")
        if Respuesta == "si" : 
            Continuar = True
        if Respuesta == "no" : 
            Continuar = False
        else : 
            print("Entrada invalida, cerrando programa...")
            Continuar = False
    

print("\nMuchas gracias por usar mi programa \nDiego Estrada CI:28.055.122")

