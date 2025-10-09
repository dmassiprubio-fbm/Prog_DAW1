'''
Escriu una funció que rebi dues paraules (String) i retorni Vertader o Fals segons siguin
o no anagrames:
'''

word1_ = input().strip()
word2_ = input().strip()

word1 = word1_.lower()
word2 = word2_.lower()

if word1 != word2:
    print(f'{sorted(word1)==sorted(word2)}')
else:
    print(False)