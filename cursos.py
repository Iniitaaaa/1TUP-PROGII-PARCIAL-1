def seleccionar():
    curso = {
        1: "PHP",
        2: "PYTHON",
        3: "C#",
        4: "HTML y CSS",
        5: "JAVA",
        6: "JS",
        7: "RUBY",
        8: "GIT"
    }
    print("Selecciona un curso:")
    for opc, valor in curso.items():   #muestra las opciones del menu 
        print(f"{opc}- {valor}")
    
    while True:
        try:
            opcion = int(input("Ingrese la opcion del curso: "))
            if opcion in curso:
                return curso[opcion]
            else:
                print("Numero invalido. Opciones validas: 1 al 8")#valida que sea opcion del 1 al 8 
        except ValueError:
            print("Ingrese un numero") #por si no se escribe un numero 
