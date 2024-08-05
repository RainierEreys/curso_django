from functools import reduce
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
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
    
add_clousure = sum_ten(3)
print(add_clousure(5))
print(sum_ten(5)(2))
sum_ten(5)(2)


## Built-IN HIGHER ORDER FUNCTION

#MAP
def multiply_two(number):
    return number * 2

numbers = [2, 5, 10, 21, 3, 30]
## AL MAP SE LE PASA LA FUNCION Y UN ITERABLE

print(list(map(multiply_two, numbers)))

print(list(map(lambda number: number * 2, numbers)))

#FILTER

#FUNCION QUE MUESTRA VALORES MAYORES A 10
def filter_greater_than_ten(value):
    if value > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


#REDUCE
#OPERA ENTRE LOS VALORES QUE VA RECORRIENDO
#un valor, mas el acumulado
def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))

