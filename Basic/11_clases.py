## CLASES ##

class MyEmptyPerson:
    pass

print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = "Sin alias"): ##ESTO ES UN CONSTRUCTOR DE CLASE (LUGAR DONDE SE PUEDEN ESTABLECER CIERTOS VALORES ASOCIADOS A L ACLASE)
        self.__nameeeeeeee = name ##ASI DEFINIMOS UN DATO PRIVADO CON LOS PISOS AL INICIO DEL NOMBRE DE VARIABLE
        self.surnameeeeee = surname
        self.full_name = f'{name} {surname} ({alias})'
        
##funcion para leer el dato privado (no se puede modificar porque es privado)
    def get_name(self):
        return self.__nameeeeeeee
    
##ESTO ES UNA FUNCION (SE PUEDEN DEFINIR EN LAS CLASES)
    def caminar(self): #SI LE ANADIMOS EL SELF PUEDE ACCEDER A LO QUE SELF TIENE GUARDADO
        print(f"{self.full_name} Esta caminando")

my_person = Person("Rainier", "Pena")

#print(my_person.__nameeeeeeee) QUEDARON INSERVIBLES AL VOLVER LA VARIABLE NAME PRIVADA
#print(f'{my_person.__nameeeeeeee} {my_person.surnameeeeee}')
print(f'{my_person.full_name}')
my_person.caminar()

print(my_person.get_name())

class OtherPerson: # PODEMOS DEFINIR COSAS DENTRO Y FUERA DE LA CLASE (LOS DE AFUERA SE LES PASA POR PARAMETRO)
    def __init__(self):
        self.name = "Rainier"
        self.surname = "Pena"
        
my_other_person = OtherPerson()
print(f'{my_other_person.name} {my_other_person.surname}')

my_other_other_person = Person("Rainier", "Pena", "Modafoka")
print(my_other_other_person.full_name)
my_other_other_person.caminar()
my_other_other_person.full_name = "Rainier Ereys (EL Criminal)"
print(my_other_other_person.full_name)

##PUEDO CAMBIAR EL TIPO DE DATO COMO QUIERO
my_other_other_person.full_name = 666
print(my_other_other_person.full_name)