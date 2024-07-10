import funciones as fn

trabajadores = ["123456789012345","Kevin Fuenza","Franco Millar","Anto Fuentes","Constanza Jerez",
"Dixon Tapia","Jose Ignacio","Bicho Rodriguez","Benja Perez"]

lista_trabajadores = {}
solo_liquidaciones = {}

opcion = None
while opcion != 7:
    try:
        print("""    ~~~~~~MENU TRABAJADORES~~~~~~
1.- Generar liquidaciones a los trabajadores
2.- Buscar liquidacion de un trabajador
3.- Clasificar las liquidaciones
4.- Ver estadisticas de las liquidaciones
5.- Reporte de las liquidaciones
6.- Imprimir plantilla de liquidaciones
7.- Apagar sistema""")
        opcion = int(input("--> "))
        if opcion == 1:
            lista_trabajadores,solo_liquidaciones = fn.generar_liquidaciones(trabajadores)

        elif opcion == 2:
                nombre = input("Ingrese el nombre del trabajador: ").lower()
                fn.buscar_liquidacion(lista_trabajadores,nombre)

        elif opcion == 3:
            if lista_trabajadores:
                fn.clasificar_liquidaciones(solo_liquidaciones)
            else:
                print("Primero debe de asignar los sueldos")
        elif opcion == 4:
            if lista_trabajadores:
                sueldo_alto,sueldo_bajo,promedio_sueldos,media_geometrica = fn.estadisticas_liquidaciones(solo_liquidaciones)
                if sueldo_alto is not None:
                    print(f"Sueldo mas alto: ${sueldo_alto}")
                    print(f"Sueldo mas bajo: ${sueldo_bajo}")
                    print(f"Promedio de sueldos: ${promedio_sueldos}")
                    print(f"Media geometrica: ${media_geometrica}")
            else:
                print("Primero debe de asignar los sueldos")
        
        elif opcion == 5:
            if lista_trabajadores:
                fn.reporte_liquidaciones(lista_trabajadores)
            else:
                print("Primero debe de asignar los sueldos")    

        elif opcion == 6:
            if lista_trabajadores:
                fn.imprimir_plantilla(lista_trabajadores)
            else:
                print("Primero debe de asignar los sueldos")  

        else:
            print("Opcion erronea, elegir del 1 al 7")
    except ValueError:
        print("Opcion erronea")
