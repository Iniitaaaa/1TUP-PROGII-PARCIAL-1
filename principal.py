empleados=  []
#registro de empleado. no lo puse en otro modulo ya que el ejercicio solo pedia que el que este en modulo separado sea cursos.py
def registrar():
    nombre = input("Ingrese el nombre: ")
    legajo = input("Ingrese el legajo: ")
    antiguedad = int(input("Ingrese la antigüedad en meses: "))
    
    if antiguedad <= 6:
        print("Debe ser mayor a 6 meses.")
        return
    
    empleado = {
        "nombre": nombre,
        "legajo": legajo,
        "cursos_realizados": [], #porque pueden ser varios
        "antiguedad": antiguedad
    }
    
    empleados.append(empleado)
    print("Resgistro exitoso")

#nuevo curso
def agregar(legajo):
    for empleado in empleados:
        if empleado["legajo"] == legajo:  #se confirma que el legajo es correcto y le pertenece a un empleado
            while True:
                from cursos import seleccionar #importa la funcion desde cursos.py
                seleccionar()
                curso=seleccionar() #se le da el valor de la funcion anterior a curso
                empleado["cursos_realizados"].append(curso) #se agrega el nuevo curso al str empleado
                continuar = input("¿Desea agregar otro curso? (S/N): ")
                if continuar.lower() != 's':
                    break
            return
    print("Legajo incorrecto o no registrado.")


while True:
    print("\nMenu Principal:")
    print("A) Registrar un empleado")
    print("B) Agregar nuevo curso")
    print("C) Salir")
    
    opcion = input("Elija una opcion entre A-B-C: ").upper()
    
    if opcion == "A":
        registrar()
    elif opcion == "B":
        legajo = input("Ingrese el legajo del empleado: ") #se corrobora el legsjo del empleador
        agregar(legajo)
    elif opcion == "C":
        break
    else:
        print("Opcion incorrecta. Elija entre A-B-C")


empleados.sort(key=lambda x: len(x["cursos_realizados"]), reverse=True) #ordena los empleados por la cantidad de cursos. Reverse=true para que sea de mayor a menor 

print(f"Cantidad de empleados: {len(empleados)}")
#Se muestra el nombre., legajo y cursos del empleado.
for empleado in empleados:
    print(f"Nombre: {empleado['nombre']}, Legajo: {empleado['legajo']}, Cursos: {len(empleado['cursos_realizados'])}")



    #NOTA PARA LA O EL PROFE#

    #Las primeras dos semanas falté a clases por un tema medico y una hospitalizacion. Realmente no vi como dieron python en clase. Esto lo hice con mi conocimiento ya que hice un curso de python en MasterIT. Por ahora estoy tratando de ponerme al dia y sé que no puedo faltar mas. Muchas Gracias :)