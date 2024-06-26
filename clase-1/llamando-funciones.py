# ¿Qué es una función? §
# Una función es un grupo de declaraciones (comandos de computadora) que juntas realizan una tarea. A grandes rasgos, existen cuatro tipos de funciones en Python que son:

# Funciones integradas
# Funciones de biblioteca estándar
# Funciones de terceros
# Funciones definidas por el usuario

# Un programador (usted) puede ahorrar mucho tiempo utilizando funciones existentes. En esta lección, aprenderá a utilizar (llamar) los dos primeros tipos de funciones. En la lección 5 , aprenderá cómo instalar módulos de terceros y llamar a funciones de terceros. En la siguiente lección , aprenderá a escribir y llamar a funciones definidas por el usuario.

# Funciones integradas:
# Python incluye muchas funciones integradas como: input, int, float, str, len, range, abs, round, list, dict, openy print. Estas se denominan funciones integradas porque no es necesario importar ningún módulo para usarlas. Son simplemente una parte integrada del lenguaje Python. Puede leer sobre las funciones integradas en la sección Funciones integradas de la referencia oficial en línea de Python.

# Un parámetro es un dato que una función necesita para completar su tarea.
# Un argumento es el valor que se pasa a través de un parámetro a una función. En otras palabras, los parámetros se enumeran en la documentación de una función y los argumentos se enumeran en una llamada a una función.

# Argumentos nombrados
# Observe en el extracto que la printfunción puede aceptar muchos objetos que se imprimirán. Opcionalmente, puede tomar parámetros llamados sep , end , file y flush que deben nombrarse cuando se usan. Por ejemplo, este código llama a la printfunción para imprimir tres palabras, todas separadas por una barra vertical (|). Observe los argumentos nombrados sep y rubor .

x = "sol" 
y = "luna" 
z = "estrellas" 
print (x, y, z, sep= "|" , flush= True )

# Cómo llamar a una función que está dentro de un módulo 
# Un módulo de Python es una colección de funciones relacionadas. La biblioteca estándar de Python incluye muchos módulos que tienen más funciones, como el math módulo, que incluye las funciones floor, ceily sqrtel randommódulo, que incluye las funciones randint, choicey shuffle .

import math

r = math.sqrt(71)
print(f"{r:.2f}")

# Cómo llamar a un método 
# Python es un lenguaje orientado a objetos e incluye muchas clases y objetos. Un método es una función que pertenece a una clase u objeto

# Example 6

# Get a string of text from the user.
text1 = input("Enter a motivational quote: ")

# Call the built-in len function to get
# the number of characters in the text.
length = len(text1)

# Call the string upper method to convert
# the quote to upper case characters.
text2 = text1.upper()

# Call the built-in print function to print
# the length of the text and the text in all
# upper case for the user to see.
print(length, text2)