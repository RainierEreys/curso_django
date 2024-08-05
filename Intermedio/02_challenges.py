## RETOS DE PROGRAMACION ##

"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    print("PRIMER RETO")
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)

fizzbuzz()

"""

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.

"""

def is_anagrama(primerPalabra, segundaPalabra):
    print("SEGUNDO RETO")
    if primerPalabra.lower() == segundaPalabra.lower():
        return False
    return sorted(primerPalabra.lower()) == sorted(segundaPalabra.lower())       
        
result = is_anagrama("rainier", 'rainier')

print(result)

"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""


    

def fibonacci():
    print("TERCER RETO")
    prevOne = 0
    prevTwo = 1
    
    my_range = range(51)
    for i in my_range:
        print(i)
        print(prevOne)
        fib = prevOne + prevTwo
        prevOne = prevTwo
        prevTwo = fib

fibonacci()

"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.

"""

def numero_primo():
    print("CUARTO RETO")
    for i in range(0,101):
        if i < 2:
            #print(f"{i} No es un numero primo")
            pass
        elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            # print(f"{i} No es un numero primo")
            pass
        else:
            print(f"{i} SI es un numero primo")
            
numero_primo()

def num_ent_prim(numero):
    print("CUARTO RETO")
    if numero < 2:
        print(f"{numero} No es un numero primo")
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0:
        print(f"{numero} No es un numero primo")
    else:
        print(f"{numero} SI es un numero primo")
        
num_ent_prim(15)

"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertidor(palabra):
    print("SEXTO RETO")
    palabra_invertida = ""
    longitud = len(palabra)
    
    for i in range(longitud):
        palabra_invertida += palabra[-i-1]
        if i + 1 == longitud:
            print(palabra_invertida)
        
invertidor("Hola mundo")
        