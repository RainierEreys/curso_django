## DATES ---> FECHAS ##


## CAPAZ DE AGRUPAR FECHA Y TIEMPO (HORA)
from datetime import datetime
## HAY QUE INICIALIZAR LOS OBJETOS
now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

## para trabajar la fecha en un formato tratable (hace referencia al momento actual)
timestamp = now.timestamp()

print(timestamp)

## SE DEFINE LA FECHA QUE QUIERA
year_2025 = datetime(2025, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(year_2025)

## CAPAZ DE AGRUPAR SOLO TIEMPO (HORA)
from datetime import time

## NO HAY FORMA DE INICIALIZAR UN TIME DIRECTAMENTE (E.G. EN DATE ESTA LA FUNCION TODAY())
current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


## CAPAZ DE AGRUPAR SOLO FECHA
from datetime import date

current_date = date(2023, 5, 27)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date_function = date.today()

print(current_date_function.year)
print(current_date_function.month)
print(current_date_function.day)


# current_date.year += 1  NO SE PUEDE XD

# asi si se puede modificar
current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date)



print(year_2025 - now)
print(year_2025.date() - current_date)


from datetime import timedelta

start_time_delta = timedelta(200, 100, 100, weeks=10)
end_time_delta = timedelta(300, 100, 100, weeks=13)

print(start_time_delta - end_time_delta)