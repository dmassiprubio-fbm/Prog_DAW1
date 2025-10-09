sentence = input()
sentence = (sentence.lower())


sentence = sentence.replace("à" , "a")
sentence = sentence.replace("á" , "a")
sentence = sentence.replace("é" , "e")
sentence = sentence.replace("è" , "e")
sentence = sentence.replace("ó" , "o")
sentence = sentence.replace("ò" , "o")
sentence = sentence.replace("ï" , "i")
sentence = sentence.replace("í" , "i")
sentence = sentence.replace("ú" , "u")
sentence = sentence.replace("ü" , "u")

a= sentence.count('a')
e= sentence.count('e')
i= sentence.count('i')
o= sentence.count('o')
u= sentence.count('u')

if a != 0:
    print('a',sentence.count('a'))

if e != 0:
    print('e',sentence.count('e'))

if i != 0:
    print('i',sentence.count('i'))

if o != 0:
    print('o',sentence.count('o'))

if u != 0:
    print('u',sentence.count('u'))