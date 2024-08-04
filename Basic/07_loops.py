## LOOPS ##

# While """ES COMO UN IF INFINITO"""

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
if my_condition == 10:
    print("Mi condicion es igual a 10")
else: #ES OPCIONAL
    print("Mi condicion es mayor o igual que 10")
    
print("La ejecucion continua")


while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
#        print("Mi condicion es igual a 15")
        print(my_condition)
        break
    print("Mi condicion es menor que 20")
    
    
my_list = [35, 65, 76, 43, 34]

for element in my_list:
    print(element)


my_tuple = (9, 1.65, "Rainier", "Peña")

for element in my_tuple:
    print(element)
    
my_other_set = {"Rainier", "Peña", 23}

for element in my_other_set:
    print(element)
    
my_dict = {
    'Nombre':'Rainier', 
    'Apellido':'Peña', 
    'Edad':23, 
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1:1.65
}

for element in my_dict.values():
    print(element)
    
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    else:
        print("Se ejecuta")
else:
        print("El bucle for ha finalizado")






        