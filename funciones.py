import random as rd
import csv
from statistics import geometric_mean

def generar_liquidaciones(trabajadores):
    lista_trabajadores = []
    solo_liquidaciones = {}

    for trabajador in trabajadores:
        sueldo_bruto = rd.randint(450000,950000)
        salud = round(sueldo_bruto * 0.07)
        AFP = round(sueldo_bruto * 0.12)
        sueldo_liquido = sueldo_bruto - AFP - salud
        solo_liquidaciones[trabajador] = sueldo_liquido

        info_trabajador = {
            "nombre" : trabajador,
            "sueldo bruto" : sueldo_bruto,
            "salud" : salud,
            "AFP" : AFP,
            "sueldo liquido" : sueldo_liquido
        }
        lista_trabajadores.append(info_trabajador)
    
    print("Sueldos asignados correctamente!!")
    print(lista_trabajadores)
    print("---")
    print(solo_liquidaciones)
    return lista_trabajadores,solo_liquidaciones

def buscar_liquidacion(lista_trabajadores,nombre):
    encontrado = False
    for trabajador in lista_trabajadores:
        if trabajador["nombre"].lower() == nombre.lower():
            print("El trabajador ya a sido remunerado")
            print(f"Sueldo Bruto: ${trabajador["sueldo bruto"]} Desc. Salud: ${trabajador["salud"]} Desc. AFP: ${trabajador["AFP"]} Liquido a Pagar: ${trabajador["sueldo liquido"]}")
            encontrado = True
        if not encontrado:
            print("Trabajador aun no remunerado / o registrado")

def clasificar_liquidaciones(solo_liquidaciones):
    mayor_700 = {}
    entre_700_450 = {}
    menor_450 = {}
    for trabajador,sueldo in solo_liquidaciones.items():
        if sueldo < 450000:
            menor_450[trabajador] = sueldo
        elif sueldo <= 700000:
            entre_700_450[trabajador] = sueldo
        else:
            mayor_700[trabajador] = sueldo

    print("------------------------------------")
    print("Sueldos menores a $450k Total:",len(menor_450))
    for trabajador,sueldo in menor_450.items():
        print(f"{trabajador}: ${sueldo}")
    print("------------------------------------")
    print("Sueldos entre $450k y $700k Total:",len(entre_700_450))
    for trabajador,sueldo in entre_700_450.items():
        print(f"{trabajador}: ${sueldo}")
    print("------------------------------------")
    print("Sueldos mayores a $700k Total:",len(mayor_700))
    for trabajador,sueldo in mayor_700.items():
        print(f"{trabajador}: ${sueldo}")

def estadisticas_liquidaciones(solo_liquidaciones):
    sueldos = list(solo_liquidaciones.values())

    sueldo_alto = max(sueldos)
    sueldo_bajo = min(sueldos)
    promedio_sueldos = round(sum(sueldos) / len(sueldos))
    media_geometrica = round(geometric_mean(sueldos))

    return sueldo_alto,sueldo_bajo,promedio_sueldos,media_geometrica

def reporte_liquidaciones(lista_trabajadores):
    print("Trabajador\t|Sueldo Bruto\t|Desc. Salud\t  |Desc. AFP\t|Liquidacion a Pagar")
    print("------------------------------------------------------------------------------------------")
    for trabajador in lista_trabajadores:
        print(f"{trabajador["nombre"]}\t|${trabajador["sueldo bruto"]}\t|${trabajador["salud"]}\t\t  |${trabajador["AFP"]}\t|${trabajador["sueldo liquido"]}")

def imprimir_plantilla(lista_trabajadores):
    with open("plantilla_trabajadores2.csv","w",newline="") as archivo:
        escritor = csv.writer(archivo,delimiter=",")
        
        escritor.writerow(["Trabajadores","Sueldo Bruto","Desc. Salud","Desc. AFP","Liquido a Pagar"])

        for trabajador in lista_trabajadores:
            nombre = trabajador["nombre"]
            sueldo_bruto = trabajador["sueldo bruto"]
            desc_salud = trabajador["salud"]
            desc_AFP = trabajador["AFP"]
            sueldo_liquido = trabajador["sueldo liquido"]
            escritor.writerow([nombre,sueldo_bruto,desc_salud,desc_AFP,sueldo_liquido])
    print("Plantilla generada con exito!!")


