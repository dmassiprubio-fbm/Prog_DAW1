def biblioteca():

    biblio = {}

    while True:
        print('')
        print('1 Afegir Llibre')
        print('2 Llistar Llibres')
        print('3 Cercar Llibre')
        print('4 Eliminar Llibre')
        print('5 Sortir')
        option = input('Selecciona una opcio ')

        if (option == '1'):
            titol = input('Introdueix el titol del llibre: ')
            autor = input('Introdueix l\'autor del llibre: ')
            biblio[titol] = {'autor': autor,}
            print(f'El llibre {titol} ha estat afegit a la biblioteca.')
        elif (option == '2'):
            if biblio:
                print('Llibres a la biblioteca:')
                for titol, info in biblio.items():
                    print(f'Títol: {titol}, Autor: {info["autor"]}')
            else:
                print('No hi ha llibres a la biblioteca.')
        elif (option == '3'):
            titol = input('Introdueix el titol del llibre a cercar: ')
            if titol in biblio:
                info = biblio[titol]
                print(f'Títol: {titol}, Autor: {info["autor"]}')
            else:
                print(f'El llibre {titol} no es troba a la biblioteca.')
        elif (option == '4'):
            titol = input('Introdueix el titol del llibre a eliminar: ')
            if titol in biblio:
                del biblio[titol]
                print(f'El llibre {titol} ha estat eliminat de la biblioteca.')
            else:
                print(f'El llibre {titol} no es troba a la biblioteca.')
        elif (option == '5'):
            print('Sortint de la biblioteca.')
            break
        else:
            print('Selecciona una opcio correcta.')
biblioteca()
    