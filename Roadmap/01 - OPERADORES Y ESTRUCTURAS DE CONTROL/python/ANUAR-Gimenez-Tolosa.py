'''
Operadores
'''
#Operadores aritméticos
sum = 10+3
print(f"Suma: 10 + 3 = {10+3}")
"""
La letra f en Python se utiliza para crear f-strings (formatted string literals)-interpolación-,forma concisa y eficiente de formatear cadenas de texto
"""
print(f"Resta: 10 - 3 = {10-3}")
print(f"Multiplicación: 10 * 3 = {10*3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")
#para las RAÍCES, observar bien la notación -con ** pero fraccionario (el denominador indica el índice de la raíz)- que la fracción vaya entre paréntesis
print(f"Raíz cuadrada: 9 ** 1/2 = {9 ** (1/2)}")
print(f"Raíz cúbica: 27 ** 1/3 = {27 ** (1/3)}")
print(f"Raíz cuarta: 231 ** 1/4 = {231 ** (1/4)}")


#operaores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}" )
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

#Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")#aquí tienen que cumplirse ambas condiciones para que resulte "True"
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")#si una de las condiciones es verdadera, resulta "True"
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")#invierte el valor.Niega una condición

#Operadores de asignación (los resultados son según la línea de código) -optimizan el código en una sola línea
my_number = 11
print(my_number)
my_number += 5
print(my_number)
my_number -= 5
print(my_number)
my_number *= 5
print(my_number)
my_number /= 2
print(my_number)
my_number %= 1
print(my_number)
my_number **= 5
my_number *= 5
my_number //= 5

#Operadores de identidad
#Los operadores de identidad se utilizan para verificar si dos variables se refieren al mismo objeto en la memoria. "is": Devuelve "True" si dos variables apuntan al mismo objeto... "is not": Devuelve "True" si dos variables no apuntan al mismo objeto
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is my_new_number es {my_number is not my_new_number}")

#Operadores de pertenencia -verifican si un valor está presente en una secuencia (como una lista, cadena, tupla o conjunto)."in": Devuelve "True" si el valor está en la secuencia."not in": Devuelve "True" si el valor no está en la secuencia
print(f"'u' in 'moure' = {"u" in "moure"}")#para mejorar el código: comillas simples
print(f"'b' not in 'moure' = {"b" not in "moure"}")

"""
Los operadores de bit se utilizan para realizar operaciones a nivel de bits en números enteros. Los operadores son:

AND (&): Realiza una operación AND bit a bit.
OR (|): Realiza una operación OR bit a bit.
XOR (^): Realiza una operación XOR bit a bit.
NOT (~): Invierte todos los bits.
Desplazamiento a la izquierda (<<): Desplaza los bits a la izquierda.
Desplazamiento a la derecha (>>): Desplaza los bits a la derecha
"""
a = 10 # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 2 <=> 0010 en binario
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") #101000

"""
Estructura de control
"""
#Condicionales
"""
Los condicionales if, elif y else se utilizan para tomar decisiones en el código:
if: Ejecuta un bloque de código si una condición es verdadera.
elif: (abreviatura de “else if”) permite verificar múltiples condiciones si la condición anterior es falsa.
else: Ejecuta un bloque de código si todas las condiciones anteriores son falsas.
"""

my_string = "Brais"

if my_string == "MoureDev":
    print("my_string es 'MoureDev")#las comilla interiores: simples
elif my_string == "Brais":
    print("my_string es 'Brais'")
else:
    print("my_string no es 'MoureDev' ni 'Brais'")

#Iterativas
"""
se utilizan para repetir bloques de código:

for: Repite un bloque de código un número definido de veces, iterando sobre una secuencia.
while: Repite un bloque de código mientras una condición sea verdadera
"""

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
"""
permiten controlar errores durante la ejecución del programa:

try: Bloque donde se coloca el código que puede generar una excepción.
except: Bloque que maneja la excepción si ocurre un error en el bloque "try".
finally: Bloque que se ejecuta siempre, ocurra o no una excepción
"""
try:
    print(10/0) #tira "error"
except:
    print("Se ha producido un error")

finally:
    print("Ha finalizado el manejo de excepciones")

"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
"""
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)