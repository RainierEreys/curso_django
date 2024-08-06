## EXPRESIONES REGULARESS ##
# SIRVEN PARA COMPROBAR SI UNA CADENA DE TEXTO CONTIENE COSAS
# PARA NO COMPLICARNOS LA VIDA RECORRIENDO STRINGS Y HACIENDO VALIDACIONES LOCAS
# "HAY QUE LLAMAR UN MODULO"

import re 

my_string = "Esta es la lección número 7: Lección de Expresiones regulares"
my_other_string = "Esta no es la lección número 7: Expresiones regulares"

#intenta encontrar cosas y arroja true o false (Al principio de la cadena de texto)
#match
result = re.match("Esta es la lección", my_string, re.I)
print(result)
start, end = result.span()
print(my_string[start:end])


result_2 = re.match("Esta no es la lección", my_other_string)
if not(result_2 == None):
    print(result_2)
    start, end = result_2.span()
    print(my_other_string[start:end])
    

#search()
# encuentra cosas en la cadena en cualquier sitio (encuentra la primera ocurrencia)
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


#findall
#arroja lista con las veces que ha encontrado la coincidencia
findall = re.findall("lección", my_string, re.I)
print(findall)

#split
#forma lista dividiendo en el caracter que se le de como parametro
split = re.split(":", my_string, re.I)
print(split)

#sub
#Es para sustituir (e.g. expresiones en minusculas por expresion en mayuscula)
sub = re.sub("[l|L]ección", "LECCIÓN", my_string, re.I)
print(sub)

# Patterns

pattern = r'[lL]ección'
print(re.findall(pattern, my_string, re.I))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[a-z]'
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r'\D' #TOMA EN CUENTA SOLO LAS LETRAS
print(re.findall(pattern, my_string))

pattern = r'\d' #TOMA EN CUENTA SOLO LOS NÚMEROS
print(re.findall(pattern, my_string))

pattern = r'[l].'  #BUSCA LA L pero como periodo (con lo que viene despues de ella)
print(re.findall(pattern, my_string))

pattern = r'[l].*'  #SE EXTRAE DESDE LA L HACIA ADELANTE
print(re.findall(pattern, my_string))


#email validation regular expresions (REGEX)

email = 'rai@technorai.com'
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$' #EXPRESION PARA ENCONTRAR EMAIL
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = 'rai@technorai.com'
print(re.findall(pattern, email)) #RETORNA VACIO PORQUE NO ENCONTRÓ EL EMAIL

    
