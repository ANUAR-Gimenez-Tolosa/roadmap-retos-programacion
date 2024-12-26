# Listas
my_list = ["Brais", "Black", "Wolfy", "Visions"]

print(my_list) 
my_list.append("Castor")# Inserción
my_list.append("Castor")
print(my_list)
my_list.remove("Brais") # Eliminación
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "Cuervillo" # Actualización
print(my_list)
my_list.sort() # Ordenación
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Brais", "Moure", "MoureDev", "36")
print(my_tuple[1])
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))
print(type(my_tuple))

# Sets
my_set = {"Brais", "Moure", "MoureDev", "36"}
print(my_set)
my_set.add("mouredev@gmail.com")
my_set.add("mouredev@gmail.com")
my_set.remove("Moure")# eliminación
print(my_set)
my_set = set(sorted(my_set))
print(my_set)
print(type(my_set))

# Diccionario
my_dict: dict = {
    "name":"Brais",
    "surname":"Moure",
    "alias":"MoureDev", 
    "age":"36"
    }
my_dict["email"] = "mouredev@gmail.com"
print(my_dict)
del my_dict["surname"]
print(my_dict)
print(my_dict["name"])
my_dict["age"] = "37"
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(my_dict)
print(type(my_dict))

"""
Extra
"""

def my_agenda():
    agenda = {}

    while True:
    

    print("")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("2. Actualizar conptacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    option = input("\nSelecciona una opción: ")

    match option:

        case "1":
            name = input("Introduce el nombre del contacto a buscar: ")
            if name in agenda:
                print(f"El número de teléfono de {name} es {agenda[name]}. ")
            else:
                print(f"El contacto {name} no existe.")
        case "2":
            name = input("Introduce el nombre del contacto: ")
            phone = input("Introduce el teléfono del contacto: ")
            if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                agenda[name] = phone
            else:
                print("Debes introducir un número de teléfono con menos de 12 dígitos.")
        case "3":
            name = input("Introduce el nombre del contacto a actualizar: ")
            if name in agenda:
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                agenda[name] = phone
            else:
                print(f"El contacto {name} no existe.")
        case "4":
            name = input("Introduce el nombre del contacto a eliminar: ")
            if name in agenda:
                del agenda[name]
            else:
                print(f"El contacto {name} no existe. ")


        case "5":
            print("Saliendo de la agenda")
            break
        case _:
            print("Opción no válida. Elige una opción del 1 al 5.")
    

my_agenda()