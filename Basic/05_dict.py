## DICCIONARIOSS ##

my_dict = dict()

print(type(my_dict))

my_other_dict = {}

print(type(my_other_dict))

my_other_dict = {'Nombre':'Rainier', 'Apellido':'Peña', 'Edad':23, 1:'Python'}
my_dict = {
    'Nombre':'Rainier', 
    'Apellido':'Peña', 
    'Edad':23, 
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1:1.65
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))

print(my_dict['Lenguajes'])

my_dict['Nombre'] = 'Hector'

print(my_dict)

my_dict['Dirección'] = 'Petare'

print(my_dict)

del my_dict['Dirección'] #del es para eliminar

print(my_dict)

print("Hector" in my_dict) #NO COMPRUEBA VALOR
print('Nombre' in my_dict) #ASI SI 
print("Hector" in my_dict['Nombre'])

print(my_dict.items())

print(my_dict.fromkeys(("Nombre", 1))) #CREA OTRO DICCIONARIO VACIO

my_list = ['Nombre', 23, "Techno"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

