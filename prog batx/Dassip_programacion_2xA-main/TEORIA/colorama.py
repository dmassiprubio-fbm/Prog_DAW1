from colorama import init, Fore, Back, Style

# Inicializar colorama
init(autoreset=True)

# Ejemplos de colores de texto
print(Fore.RED + 'Este texto es rojo')
print(Fore.GREEN + 'Este texto es verde')
print(Fore.BLUE + 'Este texto es azul')

# Ejemplos de colores de fondo
print(Back.YELLOW + 'Este texto tiene un fondo amarillo')
print(Back.CYAN + 'Este texto tiene un fondo cian')

# Combinar colores de texto y de fondo
print(Fore.RED + Back.WHITE + 'Texto rojo con fondo blanco')

# Usar estilos como brillante y tenue
print(Style.BRIGHT + 'Este texto es brillante')
print(Style.DIM + 'Este texto es tenue')

# Combinar estilos, colores de texto y de fondo
print(Style.BRIGHT + Fore.YELLOW + Back.BLUE + 'Texto brillante amarillo con fondo azul')

# Ejemplo sin autoreset
init(autoreset=False)
print(Fore.GREEN + 'Texto verde', end='')
print(' Texto normal')
print(Style.RESET_ALL, end='')  # Restablecer manualmente los estilos
print(' Texto después de restablecer')