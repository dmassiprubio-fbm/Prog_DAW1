'''
1️⃣ Implementa els mecanismes d'introducció i recuperació d'elements propis de les piles (stacks - LIFO) i les cues (queue - FIFO) utilitzant una estructura de llista.

DIFICULTAT EXTRA (Puntua si el resols totsol):
2️⃣ Utilitzant la implementació de pila i cadenes de text, simula el mecanisme d'avançar i tornar enrere d'un navegador web. Crea un programa en el qual puguis navegar a una pàgina o indicar-li que et vols desplaçar endavant o enrere, mostrant en cada cas el nom de la web.

    Les paraules "endavant", "enrere" desencadenen aquesta acció, la resta s'interpreta com el nom d'una nova web.

3️⃣ Utilitzant la implementació de cua i cadenes de text, simula el mecanisme d'una impressora compartida que rep documents i els imprimeix quan així se li indica.

    La paraula "imprimir" imprimeix un element de la cua, la resta de paraules s'interpreten com a noms de documents.
'''

#LIFO (pila) -> last in, first out
#FIFO (cues) -> first in, first out

# Pila / Stack (LIFO)

stack = []

# Afegir / push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# Treure / pop
pop_item = stack[-1]
del stack[-1]
print(pop_item)
print(stack)

# Cua / Queue (FIFO)
queue = []

# afegir / enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# eliminar / dequeue
dequeue_item = queue[0]
del queue[0]
print(queue)
print(dequeue_item)


'''
web
'''

stack_navegation  = []
stack_del_navegation = []
while True:
    action=input('Afegeix una URL o interactua amb les paraueles: endavant/enderrera/sortir:')
    if action == 'sortir':
        print('sortint del navegador')
        break
    elif action == 'enderrera':
        stack_del_navegation.append(stack_navegation[-1])
        del stack_navegation[-1]
    elif action == 'endavant':
        stack_navegation.append(stack_del_navegation[-1])
        del stack_del_navegation[-1]
    else:
        stack_navegation.append(action)

    print(stack_navegation)
    print(stack_del_navegation)


'''
impresora
'''
print_queue = []
while True:
    action = input(' afegeix un document o selecciona imprimir/sortim')
    if action == 'sortir':
        break
    elif action == 'imprimir':
        if len (print_queue) > 0:
            print(f'imprimint document: {print_queue[0]}')
            del print_queue[0]
        else:
            print('no hi ha documents per imprimir.')
    else:
        print_queue.append(action)

    
    print(print_queue)