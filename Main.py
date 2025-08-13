#Menú

#Se importan las funciones de D1 a utilizar 
from D1 import tabla_verdad, tautologia

n = 0
while n != 5:
    print("""
    1. Tabla de verdad
    2. Verificar tautología
    3. Verificar equivalencias
    4. Realizar inferencia
    5. Finalizar
    """)
    
    #El except para que se ingrese un número válido 
    try:
        n = int(input("Seleccione una opción del menú: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue  # vuelve a mostrar el menú

    if n == 1:
        inst = input("Escriba una expresión: ")
        tabla = tabla_verdad(inst)
        for fila in tabla:
            print(fila)

    elif n == 2:
        expr = input("Ingrese una expresion para ver si es una tautología: ")
            if tautologia(expr):
                print("SI es una tautología. :)")
            else:
                print("NO es una tautología")

    elif n == 3:
        print("Función para verificar equivalencias")

    elif n == 4:
        print("Función para realizar inferencia")

    elif n == 5:
        print("Saliendo del programa...")

    else:
        print("Opción no válida, intente nuevamente.")


