## FUNCIONES ##

def my_function():
    print("Esto es una funcion")
    
my_function()

## :int ---> hace referencia a que le pasen un entero ##

def sum_two_values(first_number:int, second_number):
    result = first_number + second_number
    print(result)
    
sum_two_values(5, 7)
sum_two_values("5", "7")

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

result = sum_two_values_with_return(5, 7)
print(result)
print(sum_two_values_with_return(5, 7))

def print_name(name, surname):
    print(f"{name} {surname}") #LA f es para acceder a los valores (de lo contrario imprime una cadena de texto)
    
print_name(surname = "Pena", name = "Rainier")

def print_name_with_default(name, surname, alias = "Sin alias"): ##ESA CADENA ES EL VALOR POR DEFAULT
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Rainier", "Pena", "Modafoka")
print_name_with_default("Rainier", "Pena")

def print_texts(*text): ## EL ASTERISCO ES PARA DECIRLE QUE PUEDE RECIBIR LOS PARAMETROS QUE QUIERA
    for element in text:
        print(element)
    
print_texts("Hola")
print_texts("Hola", "COMO", "ESTAS")
    
def print_upper_texts(*text):
    for element in text:
        print(element.upper())
        
print_upper_texts("rainier", "erey", "pena", "bolivar")