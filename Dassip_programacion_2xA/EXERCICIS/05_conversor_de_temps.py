dies=int(input())
hores=int(input())
minuts=int(input())
segons=int(input())

dies_c= dies * 86400000
hores_c=hores * 3600000
minuts_c=minuts * 60000
segons_c=segons * 1000

mili=segons_c + dies_c + hores_c + minuts_c

print(mili)