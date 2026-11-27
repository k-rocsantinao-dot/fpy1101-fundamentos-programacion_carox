#evaluacion 4 forma D

#funciones para validar_______________--_________________
def validar_nombre(nombre):
    texto= nombre.strip()
    if texto == "": #si el texto esta vacio...
        return False
    #sino
    return True

def validar_edad(texto_edad):
    try:
        edad = int(texto_edad)
        if edad > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_salario(texto_salario):
    try:
        salario = float(texto_salario)
        if salario > 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
#funciones del menu principal

def mostrar_menu():
    print()
    print("-----------MENU PRINCIPAL---------------------")
    print("1. agregar empleado")
    print("2. buscar empleado")
    print("3. eliminar empleado")
    print("4. actualizar estado")
    print("5. mostrar empleados")
    print("6. salir")
    print("-----------------------------------------------")

#leer opcion en una funcion aparte    
def leer_opcion():
    while True:
        opcion_texto = input("ingrese una opcion: ").strip()
        try:
            opcion = int(opcion_texto)
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("de be ingresar un numero entre el 1 y el 6")
        except ValueError:
            print("debe ingresar un numero valido")
        

#funciones para la gestion 


def agregar_empleado(empleados):
    nombre = input("ingrese nombre: ")
    edad_texto = input("ingrese edad: ")
    salario_texto = input("ingrese salario: ")
    
    #validaciones antes de que se pueda agregar all nuevo empleado
    if not validar_nombre(nombre):
        print("error:el nombre no puede estar vacio ni solo espacios ") 
        return
    if not validar_edad(edad_texto):
        print("error:la edad debe ser un num. entero mayor a 0")
        return
    if not validar_salario(salario_tezto):
        print("error: el salario debe ser un numero decimal mayor a cero")  
        return
    
    #agregar empleado nuevo al diccionario
    nuevo_empleado = {
        "nombre": nombre.strip(),
        "edad": int(edad_texto),
        "salario": float(salario_texto),
        "activo": False
    }  
    
    empleados.append(nuevo_empleado)
    print("empleado agregado!")
    
#buscar empleado funcion

def buscar_empleado(empleados, nombre_buscado):
    for i in range(len(empleados)):
        if empleados[i]["nombre"] == nombre_buscado:
            return i
    return - 1

