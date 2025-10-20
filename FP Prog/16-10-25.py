import numpy as np

lisata = []
nota = ()

while nota != -1:
    nota = float(input('introduce una nota del alumno: '))
    if nota in np.arange(0,11,0.1):
        lisata.append(nota)
    else:
        print('introduce otra, esta no esta entre el 0 y el 10')

print(lisata)
lisata.sort()
print(f'la nota mas alta es: {lisata[-1]}')
print(f'la nota mas baja es: {lisata[0]}')

total = 0
suspensos = 0
aprovados = 0
#listaA = []
#listaS=[]
notasA = 0

for i in lisata:
    total = total +1
    notasA = notasA + i
    if i < 5:
        suspensos = suspensos + 1
        #listaS.append(i)
    elif i >= 5:
        aprovados = aprovados + 1
        #listaA.append(i)
        

print(f'has aprovado {aprovados} examenes')
print(f'has suspendido {suspensos} examenes')
media = (notasA / total) * 10
print(f'tus examenes tiene una media de {media}')
percent = (aprovados / total ) * 100
print(f'has aprovado un {percent}% de los examenes')

