## EXCEPTION HANDLING ##


numberOne, numberTwo = 5, 1

numberTwo = "1"

## try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")

## try except else FINALLY
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: ## ESTE ELSE SOLO SE EJECUTA SI NO HAY UN ERROR (SINO OCURRE EL EXCEPT)
    print("La ejecucion sigue xd")
finally: ##ESTE SE EJECUTA CON ERROR Y SIN ERROR (SIEMPRE CON EXCEPT O SIN EXCEPT)
    print("Y la ejecucion continua y continua")
    
    
# CAPTURA DE ERRORES POR TIPO
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except TypeError: ##SOLO SE VA A EJECUTAR SI ES UN ERROR DE TIPEO (HAY VARIOS TIOS DE ERRORES)
    print("Se ha producido un TypeError")
except ValueError: ##Se pueden meter varias excepciones
    print("Se ha producido un ValueError")
    
    
#CAPTURA DE LA INFORMACION DE LA EXCEPCION
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error: #SE DEFINE ESA VARIABLE PARA CONTROLAR EL ERROR (OBTENER LA IFNORMACION PRECISA)
    print(error)
except Exception as error: ##Sea lo que sea el error se controlara (Es usado para capturar la informacion del error y establecer la variable)
    print(error)
    



    
