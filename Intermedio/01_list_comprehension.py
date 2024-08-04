## LIST COMPREHENSION ##
## SIRVE PARA CREAR LISTAS


my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(7)

print(list(my_range))

## SIRVE PARA CREAR LISTAS

## SIRVE PARA CREAR LISTAS QUE NOSOSTROS VAYAMOS OPERANDO (TRATANDO) EN EL MOMENTO EN QUE SE ESTE CREANDO 
my_list = [i + 1 for i in my_range]
print(my_list)

my_list = [i * 2 for i in my_range]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in my_range]
print(my_list)

