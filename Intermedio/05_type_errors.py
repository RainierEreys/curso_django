## TIPOS DE ERRORES ##

# SyntaxError
#print "Hola comunidad" ERROR
print("Hola Comunidad")

# NameError CUANDO INTENTAS TRABAJAR CON ALGUNA VARIABLE NO DECLARADA
#print(name)
language = "Spanish"
print(language)

#IndexError CUANDO LLAMO UN INDICE QUE NO EXISTE EN UN ARREGLO
# my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
# print(my_list[6])
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[4])
print(my_list[False])
# print(my_list['Apellido']) DESCOMENTAR PARA ERROR


#ModuleNotFoundError CUANDO HACEMOS REFERENCIA A UN MODULO QUE NO EXISTE
#import maths
import math

#AttributeError #CUANDO HAGO REFERENCIA A UN ATRIBUTO DE UN MODULO QUE NO EXISTE
#print(math.PI)
print(math.pi)

#KeyError CUANDO HAGO REFERENCIA A UNA CLAVE DE UN DICCIONARIO QUE NO EXISTE
# my_dict = {
#     'Nombre':'Rainier', 
#     'Apellido':'Peña', 
#     'Edad':23, 
#     'Lenguajes':{'Python', 'Swift', 'Kotlin'},
#     1:1.65
# }
# print(my_dict['Apellidos'])
my_dict = {
    'Nombre':'Rainier', 
    'Apellido':'Peña', 
    'Edad':23, 
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1:1.65
}
print(my_dict['Apellido'])


#ImportError CUANDO IMPORTO ALGO QUE NO EXISTE
#from math import PI
from math import pi
print(pi)

#ValueError CUANDO INTENTO TRANSFORMAR UNA CADENA DE TEXTO A ENTERO
# my_int = int("10 Años")
# print(type(my_int))

# ZeroDivisionError CUANDO INTENTO DIVIDIR ALGO ENTRE CERO
print(4/2)
# print(4/0)