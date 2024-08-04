## tuplas ##

## LA TUPLA ES CONSTANTE, LOS VALORES SON INMUTABLES ##
## NO COMO LA LISTA ##
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (9, 1.65, "Rainier", "Peña")

print(type(my_tuple))

print(my_tuple[0])

print(my_tuple.count("Rainier"))
print(my_tuple.index("Rainier"))

#my_tuple[1] = 1.90 TypeError: 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple[2:4])

my_tuple_liust = list(my_tuple)
print(type(my_tuple_liust))

my_tuple_liust.insert(2, "verde")
print(my_tuple_liust)

my_tuple = tuple(my_tuple_liust)
print(type(my_tuple))