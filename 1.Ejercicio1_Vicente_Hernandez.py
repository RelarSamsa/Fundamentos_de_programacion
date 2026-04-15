print("Inscripcion del Taller", "\n")
edad_usuario = int(input("Ingrese su edad actual "))
estado_inscripcion = str(input("Esta usted inscrito(SI o NO):"))
if edad_usuario >= 18:
    if estado_inscripcion == "NO":
     print("Inscripcion aceptada")
    elif estado_inscripcion == "SI":
     print("Inscripción rechazada")
    else:
        print("Inscripción rechazada")
else:
    print("Debe ser mayor de edad para poder inscribirse")
print("Fin del proceso")