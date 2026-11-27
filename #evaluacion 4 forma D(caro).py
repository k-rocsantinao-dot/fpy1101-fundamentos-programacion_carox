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
            
    