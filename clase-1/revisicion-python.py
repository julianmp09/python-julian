# Estaremos practicando python nuevamente, ¡Mucho exito Julian Daniel

# Como declarar una variable
# Una variable es una ubicación en la memoria de una computadora donde un programa almacena un valor. Una variable tiene un nombre, un tipo de datos y un valor. En Python, asignamos un valor a una variable usando el operador de asignación, que es el símbolo igual (=). Una computadora puede cambiar el valor y el tipo de datos de una variable mientras ejecuta un programa.

longitud = 5
nombre = "Julian"
valor_booleano = True

# Tipo de datos
# Python tiene muchos tipos de datos , incluidos str, bool, int, float, listy dict. La mayoría de los tipos de datos que utilizará en sus programas en CSE 111 se muestran en la siguiente lista.
# Un string  es cualquier texto entre comillas simples o dobles, cualquier texto que ingresa un usuario y cualquier texto en un archivo de texto. Por ejemplo:
saludo = "Hola" 
texto = "23"

# Un bool (variable booleana) es una variable que almacena Trueo False. Una variable booleana no puede almacenar ningún otro valor además de True o False. Por ejemplo:
encontrado = True

# Un int (entero) es un número entero como 14. intNo puede tener una parte fraccionaria ni dígitos después del punto decimal. Por ejemplo:
x = 14

# Un flotante (número de punto flotante) es un número que puede tener una parte fraccionaria o dígitos después del punto decimal como 7,51. Por ejemplo:
muestra = 7,51

# Una lista es una colección de valores. Cada valor de una lista se denomina elemento y se almacena en un índice único. El propósito principal de una lista es almacenar muchos elementos de manera eficiente. En un programa Python, podemos crear una lista usando corchetes ([ y ]) y separando los elementos con comas (,). Por ejemplo, aquí hay dos listas nombradas colors y samples:
colors = [ "amarillo" , "rojo" , "verde" , "amarillo" , "azul" ]
samples = [ 6,5 , 7,2 , 7,0 , 8,1 , 7,2 , 6,8 , 6,8 ]

# Un dict (diccionario) es una colección de elementos. Cada elemento es un par clave-valor. El objetivo principal de un diccionario es permitir que una computadora encuentre elementos muy rápidamente. En un programa Python, podemos crear un diccionario usando llaves ({ y }) y separando los elementos con comas (,). Por ejemplo:
estudiantes = {
     "42-039-4736" : "Clint Huish" ,
     "61-315-0160" : "Amelia Davis" ,
     "10-450-1203" : "Ana Soares" ,
     "75-421-2310" : "Abdul Ali" ,
     "07-103-5621" : "Amelia Davis"
}

# nombre_1 = "Julian"
# Apellido = "Martinez"

# print(f"Hola {nombre_1} {Apellido} Bienvenido otra vez")

# Crearemos un ejercicio simple en donde le pediremos al ususario que ingrese su fecha de nacimiento y el año actual para tener cuantos años tiene

año_de_nacimiento = float(input("Ingrese el año en que nacio: "))
año_actual = float(input("Ingrese el año actual: "))

def cacular_el_año_actual (fecha, año):
    """Esta funcion toma como parametros fecha y año la cual despues, nos retronara la edad aproximada de la persona"""
    edad_actual = año - fecha
    return edad_actual

#llamamos la funcion 
print(f"Usted tiene o tendra {cacular_el_año_actual(año_de_nacimiento,año_actual):.0f} años")

# Aritmetica
# Python tiene muchos operadores aritméticos , incluidos potencia (**), negación (-), multiplicación (*), división (/), división de piso (//), módulo (%), suma (+) y resta (-).
# El operador de potencia (**) a veces se llama exponenciación y hace que una computadora eleve un número base a un exponente. Por ejemplo, el siguiente código Python hace que la computadora calcule y almacene 125 en la variable resultado porque el valor en x es 5 y el valor en y es 3 y 5 ** 3 o 5 3 o 5 elevado al exponente 3 es 125 .

x = 5 
y = 3 
resultado = x ** y
print(f"{resultado}")

# if Statements

# En Python, usamos ifdeclaraciones para hacer que la computadora tome decisiones; ifLas declaraciones también se denominan declaraciones de selección porque la computadora selecciona un grupo de declaraciones para ejecutar y omite el otro grupo de declaraciones.

# Hay seis operadores de comparación que podemos usar en una ifdeclaración:

# <	menos que
# <=	menor o igual
# >	mas grande que
# >=	mayor que o igual
# ==	igual a
# !=	no igual a

# Example 6

# Get an account balance as a number from the user.
balance = float(input("Enter the account balance: "))

# If the balance is greater than 500, then
# compute and add interest to the balance.
if balance > 500:
    interest = balance * 0.03
    balance += interest

# Print the balance.
print(f"balance: {balance:.2f}")

# Example 7

# Get the cost of an item from the user.
cost = float(input("Please enter the cost: "))

# Determine a discount rate based on the cost.
if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

# Compute the discount amount
# and the discounted cost.
discount = cost * rate
cost -= discount

# Print the discounted cost for the user to see.
print(f"After the discount, you will pay {cost:.2f}")