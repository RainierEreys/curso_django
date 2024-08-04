## SETS ##

## NOOO ADMITE REPETIDOS ##

my_set = set()
my_other_set = {}

print(type(my_other_set)) #es un diccionario

my_other_set = {"Rainier", "Peña", 23}
print(type(my_other_set))

print(len(my_other_set))

#print(my_other_set[2])  TypeError: 'set' object is not subscriptable

my_other_set.add("Technorai")

print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add("Technorai")

print(my_other_set)  #Un set no admite repetidos

print("Technorai" in my_other_set)

my_other_set.remove("Technorai")

print(my_other_set)

my_other_set.clear()

print(my_other_set)

print(len(my_other_set))

my_list = list(my_other_set)