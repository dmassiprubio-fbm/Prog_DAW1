###1###
edat = int(input('itrodueix la teva edat: '))
estudiant = input('ets estudiant(S/N): ').ipper()
dia =input('quin dia es avui ? ')

preu = 8
dia2 = dia.lower()

lista =['dilluns','dimarts','dimecres','dillous','divendres','dissabte','diumenge']

if edat >= 0:
    if dia2 in lista:
        if edat < 12:
            preu_final = 8 * 0.5
            preu_final_r = round(preu_final, 2)
            print(f' el preu fianl es de {preu_final_r} € per que ets menor de 12 anys')
        elif dia2 == 'dimecres' :
            preu_final = 8 *0.70
            preu_final_r = round(preu_final, 2)
            print(f' el preu fianl es de {preu_final_r} € per que es dimecres')
        elif estudiant == 'S':
            preu_final = 8 *0.75
            preu_final_r = round(preu_final, 2)
            print(f' el preu fianl es de {preu_final_r} € per que ets estudiant')
    else:
        print('no existeix aquest dia de la setmana')
else:
    print('no pots tenir edat negativa')

###2###

contrasenya = ('Contrasenya33')
contador = 1

while contador <= 3:
    contrasenya2 = input('itrodueix la contrasenya(tens 3 intents): ')
    if contrasenya2 == contrasenya:
        print('Accés concedit')
        break
    else:
        print('contrasenya incorrecta')
        contador = contador +1

##3##

dia = int(input('introdueix el dia: '))
mes = int(input('introdueix el  (en numeros): '))
any = input('introdueix el any: ')



if mes == 1 or mes ==3 or mes ==5 or mes ==7 or mes ==8 or mes ==10 or mes ==12:
    if dia <= 31:
        print(f'{dia}/{mes}/{any} dat correcta')
    else:
        print(f'{dia}/{mes}/{any} dat incorrecta')
elif mes == 4 or mes ==6 or mes ==9 or mes ==11:
    if dia <= 30:
        print(f'{dia}/{mes}/{any} dat correcta')
    else:
        print(f'{dia}/{mes}/{any} dat incorrecta')
elif mes == 2:
    if dia <= 28:
        print(f'{dia}/{mes}/{any} dat correcta')
    else:
        print(f'{dia}/{mes}/{any} dat incorrecta')
