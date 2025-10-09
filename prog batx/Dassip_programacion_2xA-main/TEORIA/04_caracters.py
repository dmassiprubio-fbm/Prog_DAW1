'''
1️⃣Mostra exemples de totes les operacions que pots realitzar amb cadenes de caràcters a Python. Algunes d'aquestes operacions podrien ser:

    Accés a caràcters específics, subcadenes, longitud, concatenació, repetició, recorregut, conversió a majúscules i minúscules, reemplaçament, divisió, unió, interpolació, verificació...

DIFICULTAT EXTRA (Puntua si el resols totsol):

2️⃣Crea un programa que analitzi dues paraules diferents i realitzi comprovacions per a descobrir si són:

    Palíndroms: és una paraula, frase o grup de paraules les lletres de les quals es repeteixen en el mateix ordre quan són llegides en la direcció inversa. Ex: Radar -> radaR
    Anagrames: és una paraula o una frase formada per la transposició de les lletres d'una altra paraula o una altra frase. Ex: Roma -> amoR
    Isogrames: és una paraula o frase en la qual cada lletra apareix el mateix nombre de vegades. Ex: Paperera -> P*2, a*2, e*2, r*2
'''

#operacions

s1 = 'hola'
s2 = 'phyton'

#concatenacio
print(s1 + ' ' + s2)

#repetició
print(s1 * 4)

#Accès
print(s1[0], s2[0])

#longitud
print(len(s1))

#subcadena
print(s1[0:3])
print(s1[1:])
print(s1[:3])

#cerca
print('o' in s1)
print('i' in s1)
print('ola' in s1)

#substitució
print(s1.replace('o', 'a'))

#split
print(s2.split('t'))
print('Pum Pum, Pum Pum, Carmaaaanyooolaaaa'.split(' '))

#majúsculas, minúsculas, capitalize
print(s1.upper())
print(s2.lower())
print('guillem mas'.title())
print('guillem mas'.capitalize())

#Eliminar espais blancs al principi i al final
print('                             guillem mas                                       '.strip())

#cerca al principi i al final
print(s1.startswith('ho'))
print(s2.startswith('py'))
print(s1.endswith('a'))
print(s2.endswith('thon'))

s3 = 'Guillem Mas @guillemmas'
#cerca per posició
print(s3.find('Mas'))
print(s3.find('maas')) #-1 significarà que no ha trobat la cadena

#cerca d'aparicions
print(s3.count('m'))
print(s3.lower().count('m'))

#Interpolacio
name = input('Introdueix el teu nom  ')
age = input('Introdueix la teva edat  ')
print(f'Salutacioó {name}, tens {age} anys ')

#formateig
print('Salutacions {}, tens {} anys'.format(name,age))

#coverti a llista
print(list(s3))

#convertir llista a string
my_list = ['Carlos','Damia','Alba']
print(my_list)
my_string = ', '.join(my_list)
print(my_string)

#transformsions numèiques
s4 = '1234'
s5 = '123.345'
print(int(s4)) #conversiò a nombre entre
print(float(s5)) #conversió a nombre real

#comprovacio de cadenes de text
s6= 'mdvgjskebhiwug'
s7= '5265716876525'
s8 =  '7yj8b6875tj746r3'
s9 = 'jhfgikdol5496h5ep45klgiodc'

print(s6.isalnum())  #alphanumrico
print(s6.isalpha())  #letras
print(s6.isnumeric())   #numeros
print(s6.isdecimal())   #digitos del 0 al 9
print(s7.isalnum())
print(s7.isalpha())
print(s7.isnumeric())
print(s7.isdecimal())
print(s8.isalnum())
print(s8.isalpha())
print(s8.isnumeric())
print(s8.isdecimal())
print(s9.isalnum())
print(s9.isalpha())
print(s9.isnumeric())
print(s9.isdecimal())


'''
    Crea un programa que analitzi dues paraules diferents i realitzi comprovacions per a descobrir si són:
    Palíndroms: és una paraula, frase o grup de paraules les lletres de les quals es repeteixen en el mateix ordre quan són llegides en la direcció inversa. Ex: Radar -> radaR
    Anagrames: és una paraula o una frase formada per la transposició de les lletres d'una altra paraula o una altra frase. Ex: Roma -> amoR
    Isogrames: és una paraula o frase en la qual cada lletra apareix el mateix nombre de vegades. Ex: Paperera -> P*2, a*2, e*2, r*2
'''


def chek(word1, word2):
    def isograma(word):
        word_dict = {}
        for character in word1: #ficam totes les lletres dins un diccionari
            word_dict[character] = word_dict.get(character, 0) + 1 #utilitzam el get per definir el valor com 0
        is_isograma = True #suposem que es isograma i hem de trobar un cas contrari
        v_0 = list(word_dict.values())[0] # agafam el nº de vegades que apareix el primer valor de la llisa
        for k, v in word_dict.items(): #recore tot el diccionari
            if (v != v_0):#comparam si son diferents
                is_isograma = False
                break #si es fals atura de comprobar
        return is_isograma

    print(f'{word1} és un palindrom? {word1 == '' .join(reversed(word1))}')
    print(f'{word2} és un palindrom? {word2 == '' .join(reversed(word2))}')

    '''
    word1_reversed = ''.join(reversed(word1))
    
    # reversd torna una llista,
    # i feim el join per pasar a str
    
    if (word1 == word1_reversed):
        print(f'{word1} és palindrom')
    word2_reversed = word2 [::-1] #invertir la cadena
    if (word2 == word2_reversed):
        print(f'{word2} és palindrom ')
    '''
    
    print(f'{word1} és anagrama de {word2}? {sorted(word1)==sorted(word2)}')
    '''
    if (sorted(word1)) == (sorted(word2)):
        print(f'{word1} és anagrama de {word2}.')
    '''
    
    print(f'{word1} és isograma ? {isograma(word1)}')
    print(f'{word2} és isograma ? {isograma(word2)}')

word1 = input('Introdueix la paraula 1')
word2 = input('introdueix la paraula 2')

chek(word1, word2)