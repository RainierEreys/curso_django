## FUNCIONES DE ORDEN SUPERIOR ###

## SON FUNCIONES QUE HACEN COSAS CON FUCNIONES DENTRO

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

## SE PUEDE PASAR UNA FUNCION COMO PARAMETRO
def sum_two_values_and_add_value(first_value, second_value, function):
    return function(first_value + second_value)

print(sum_two_values_and_add_value(5, 7, sum_one))

print(sum_two_values_and_add_value(5, 2, sum_five))


## CLOUSURES ##
## FUNCION QUE DEFINE UNA FUNCION Y RETORNA UNA FUNCION
##RETORNAR FUNCIONES ##
def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_clousure = sum_ten()
print(add_clousure(5))

