"""
Funciones definidas por el usuario
"""
#Simple

def greet():
    print("Hola Python")

greet()
greet()

#Con retorno

def return_greet():
    return "¡Hola Python!!"

 
print(return_greet())

#Con un argumento

def arg_greet(name):
    print(f"¡¡¡¡Hola {name}!!!!")

arg_greet("Brais")

#Con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi", "Brais")

#Con un argumento predeterminado

def default_arg_greet(name="Python"):
    print(f"¡¡¡¡Hola {name}!!!!")

default_arg_greet("Brais")
default_arg_greet()

#Con aargumentos y retornos

def return_args_greet(greet, name):
    return "{greet}, {name}"

print(return_args_greet("Hi", "Brais"))

#Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

#Con un número variable de argumentos

def variable_arg_greet(*name):
    for name in name:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Brais", "Mouredev", "comunidad")

#con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, values in names.items():
        print(f"Hola, {values} ({key})!")

variable_key_arg_greet(
Language="Python", 
name="Brais", 
alias= "MoureDev", 
age=36
)

#Funciones dentro de funciones

def outer_function():
    def inner_function():
        print("función interna: Hola Python!")
    inner_function()

outer_function()

#Funciones del lenguaje (built-in)

print(len("MoureDev"))
print(type(36))
print("MoureDev".upper())

#Variable locales y globales

global_var = "Python"


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)


hello_python()

#Extra

def print_numbers(text_1, texto_2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + texto_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(texto_2)
        else:
            print(number)
            count == 1
    return count

print(print_numbers("Fizz", "buzz"))
