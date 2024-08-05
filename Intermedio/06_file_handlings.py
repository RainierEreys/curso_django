## MANEJAR FICHEROS ##

import os
# .txt file

#SE PASA EL ARCHIVO DESDE LA CARPETA RAÍ, EL SEGUNDO PARAMETRO ES MODO: LECTURA, ESCRITURA , ETC ETC
txt_file = open("Intermedio/my_file.txt", "r+")
#print(txt_file.read())
#print(txt_file.read(10)) #SIRVE PARA LEER UNA SECCION DE 10 ESPACIOS
#print(txt_file.readline()) #LEE LA PRIMERA LINEA (SI COLOCO MAS LEE LAS LINEAS SIGUIENTES)
# print(txt_file.readlines()) #HACE UN ARREGLO CON LAS LINEAS

for line in txt_file.readlines():
    print(line)

#txt_file.write("Hola como estas")

print(txt_file.read())


#.JSON FILE

import json #PARA TRABAJAR CON JSON 

json_file = open("Intermedio/my_file.json", "w+")

json_text = {
    'name':'Rainier', 
    'surname':'Peña', 
    'age':23, 
    'languages':['Python', 'Swift', 'Kotlin'],
    'website':'https://www.moure.dev',
    }

## se debe pasar el texto y el archivo al que se le va a meter el texto e identacion
json.dump(json_text, json_file, indent=4) ## PARA METER CONTENIDO AL JSON


json_file.close()  ## HAY QUE CERRARLO PARA PODER LEER LOS ARCHIVOS

with open("Intermedio/my_file.json") as my_other_file:
    
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermedio/my_file.json")) ##PARA CARGAR EL CONTENIDO DEL JSON A UN DICCIONARIO
print(json_dict)
print(type(json_dict))

    
