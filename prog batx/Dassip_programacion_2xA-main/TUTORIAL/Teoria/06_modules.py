### Mòduls ###

import math

print(math.pi)

print(math.cos(15))

print(math.sqrt(64))

math.degrees(90)

import random

my_random_value = random.randint(10, 20)
print(my_random_value)

import datetime

now = datetime.datetime.now()
print(now.hour, now.minute)
print(now.minute)
print(now.year)
print(now.day)
print(now.weekday())

### POSIX time. Segundos que han pasado desde 1 Enero 1970 ###
print(now.timestamp()) 

import datetime
year_1000 = datetime.datetime(1000,1,1)
diff = now-year_1000
print(diff.days/365)

dia= int(input("Introdueix el dia:"))
mes= int(input("Introdueix el mes:"))
any= int(input("Introdueix el any:"))
fecha_ini = datetime.datetime(any,mes,dia)
fecha_fini =datetime.datetime(2023,8,17)
diff=fecha_fini-fecha_ini
print(diff)
print(diff.days/365)