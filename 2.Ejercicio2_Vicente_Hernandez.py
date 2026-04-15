tiempo_total = 0
while True:
     print("\n", "Registro de actividades diarias", "\n")
     print("1) Registrar actividades")
     print("2) Mostrar análisis del tiempo")
     print("3) Salir")
     opcion = int(input("Ingrese una opcion: "))
     if opcion == 1:
        actividades = int(input("Ingresa la cantidad de actividades a registrar: "))
        for i in range(actividades):
           if actividades >=3:
             nombre_actividad = str(input("Ingresa el nombre de la actividad: "))
             tiempo_actividad = int(input("Ingresa el tiempo que toma la actividad en minutos: ")) 
             tiempo_total = tiempo_actividad + tiempo_total
        else:
            print("n", "Debe ingresar una cantidad mayor a 3")
     elif opcion == 2:
        print("\n", f"{tiempo_total} minutos")
        if tiempo_total > 180:
            print("Tiempo diario excesivo")
        else:
            print("Tiempo diario adecuado")
     elif opcion == 3:
        print("\n", "Fin del registro", "\n")
        break
     else:
        print("\n", "Opcion invalida vuelve a intentarlo ")