import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Plataformas con Scroll")

# Carrega el sprite sheet
sprite_sheet = pygame.image.load("pyjocs/media/knight.png").convert_alpha()

# Dades del sprite sheet
frame_width = 30     # ← adapta-ho a la mida real del teu sprite
frame_height = 30
num_frames = 4       # ← quants fotogrames hi ha?

# Talla els fotogrames del sprite sheet
walk_frames = []
escala = 2  # Escala de mida (2 = doble, 3 = triple...)

for i in range(num_frames):
    frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
    frame_escalat = pygame.transform.scale(frame, (frame_width * escala, frame_height * escala))
    walk_frames.append(frame_escalat)

# Configuración del mundo (más ancho que la pantalla)
ANCHO_MUNDO = 2000
ALTO_MUNDO = ALTO_PANTALLA

# Crear una superficie para el mundo
mundo = pygame.Surface((ANCHO_MUNDO, ALTO_MUNDO))

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
MORADO = (128, 0, 128)
CIELO = (135, 206, 235)

# Reloj para controlar la velocidad de fotogramas
reloj = pygame.time.Clock()
FPS = 60

# Gravedad
GRAVEDAD = 0.75

# Clase del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, walk_frames):
        super().__init__()
        self.walk_frames = walk_frames
        self.index_anim = 0
        self.image = self.walk_frames[self.index_anim]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.saltando = False
        self.vidas = 3
        self.contador_anim = 0  # Per controlar la velocitat de l’animació
        self.mirant_esquerra = False  # nova variable

    def update(self, plataformas):
        # Aplicar gravedad
        self.velocidad_y += GRAVEDAD
        
        # Mover el jugador horizontalmente
        self.rect.x += self.velocidad_x
        
        # Detectar colisiones horizontales
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.velocidad_x > 0:  # Moviéndose a la derecha
                    self.rect.right = plataforma.rect.left
                elif self.velocidad_x < 0:  # Moviéndose a la izquierda
                    self.rect.left = plataforma.rect.right
        
        # Mover el jugador verticalmente
        self.rect.y += self.velocidad_y
        
        # Detectar colisiones verticales
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.velocidad_y > 0:  # Cayendo
                    self.rect.bottom = plataforma.rect.top
                    self.velocidad_y = 0
                    self.saltando = False
                elif self.velocidad_y < 0:  # Saltando
                    self.rect.top = plataforma.rect.bottom
                    self.velocidad_y = 0
        
        # Limitar al jugador dentro del mundo
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO_MUNDO:
            self.rect.right = ANCHO_MUNDO
        if self.rect.bottom > ALTO_MUNDO:
            self.rect.bottom = ALTO_MUNDO
            self.velocidad_y = 0
            self.saltando = False

        # ANIMACIÓ si es mou
        if self.velocidad_x != 0:
            self.contador_anim += 1
            if self.contador_anim >= 6:  # control de velocitat de canvi de fotograma
                self.index_anim = (self.index_anim + 1) % len(self.walk_frames)
                self.contador_anim = 0
        else:
            self.index_anim = 0  # torna a l’estat de repòs

        if self.velocidad_x < 0:
            self.mirant_esquerra = True
        elif self.velocidad_x > 0:
            self.mirant_esquerra = False

        self.image = self.walk_frames[self.index_anim]

        frame_actual = self.walk_frames[self.index_anim]
        if self.mirant_esquerra:
            self.image = pygame.transform.flip(frame_actual, True, False)
        else:
            self.image = frame_actual
    
    def saltar(self):
        if not self.saltando:
            self.velocidad_y = -15
            self.saltando = True
    
    def mover_izquierda(self):
        self.velocidad_x = -5
    
    def mover_derecha(self):
        self.velocidad_x = 5
    
    def detener(self):
        self.velocidad_x = 0

# Clase de plataforma
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Clase de enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, plataforma=None):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = random.choice([-2, -1, 1, 2])
        self.plataforma = plataforma
        self.rango_movimiento = 100
        self.pos_inicial_x = x
    
    def update(self):
        self.rect.x += self.velocidad_x
        
        # Cambiar dirección si alcanza los límites del rango
        if abs(self.rect.x - self.pos_inicial_x) > self.rango_movimiento:
            self.velocidad_x *= -1
        
        # Si el enemigo tiene una plataforma asignada
        if self.plataforma:
            if self.rect.left < self.plataforma.rect.left:
                self.rect.left = self.plataforma.rect.left
                self.velocidad_x *= -1
            if self.rect.right > self.plataforma.rect.right:
                self.rect.right = self.plataforma.rect.right
                self.velocidad_x *= -1

# Función para mostrar texto
def mostrar_texto(surface, texto, tamaño, x, y, color=BLANCO):
    fuente = pygame.font.SysFont("Arial", tamaño)
    texto_surface = fuente.render(texto, True, color)
    texto_rect = texto_surface.get_rect()
    texto_rect.midtop = (x, y)
    surface.blit(texto_surface, texto_rect)

# Crear sprites
todos_los_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

# Crear jugador (posición inicial centrada en el mundo)
jugador = Jugador(ANCHO_MUNDO // 2 - 15, ALTO_MUNDO - 100, walk_frames)
todos_los_sprites.add(jugador)

# Crear plataformas
plataforma_suelo = Plataforma(0, ALTO_MUNDO - 50, ANCHO_MUNDO, 50)
plataformas.add(plataforma_suelo)
todos_los_sprites.add(plataforma_suelo)

# Plataformas adicionales (distribuidas por el mundo)
posiciones_plataformas = [
    (100, 400, 200, 20),
    (400, 300, 200, 20),
    (200, 200, 150, 20),
    (600, 450, 150, 20),
    (800, 350, 200, 20),
    (1200, 250, 200, 20),
    (1500, 400, 150, 20),
    (1700, 300, 200, 20)
]

for x, y, ancho, alto in posiciones_plataformas:
    plataforma = Plataforma(x, y, ancho, alto)
    plataformas.add(plataforma)
    todos_los_sprites.add(plataforma)

# Crear enemigos en algunas plataformas
for plataforma in plataformas:
    # Solo poner enemigos en plataformas que no sean el suelo
    if plataforma.rect.y < ALTO_MUNDO - 100:
        # 50% de probabilidad de poner un enemigo
        if random.random() > 0.5:
            enemigo = Enemigo(
                plataforma.rect.x + plataforma.rect.width // 2,
                plataforma.rect.y - 30,
                plataforma
            )
            enemigos.add(enemigo)
            todos_los_sprites.add(enemigo)

# Función para reiniciar el juego
def reiniciar_juego():
    jugador.rect.x = ANCHO_MUNDO // 2 - 15
    jugador.rect.y = ALTO_MUNDO - 100
    jugador.velocidad_x = 0
    jugador.velocidad_y = 0
    jugador.vidas = 3

# Bucle principal del juego
ejecutando = True
game_over = False

# Posición de la cámara
camara_x = 0

while ejecutando:
    # Mantener el bucle funcionando a la velocidad correcta
    reloj.tick(FPS)
    
    # Procesar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not game_over:
                jugador.saltar()
            if evento.key == pygame.K_LEFT and not game_over:
                jugador.mover_izquierda()
            if evento.key == pygame.K_RIGHT and not game_over:
                jugador.mover_derecha()
            if evento.key == pygame.K_r and game_over:
                reiniciar_juego()
                game_over = False
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT and jugador.velocidad_x < 0:
                jugador.detener()
            if evento.key == pygame.K_RIGHT and jugador.velocidad_x > 0:
                jugador.detener()
    
    if not game_over:
        # Actualizar jugador y colisiones
        jugador.update(plataformas)
        enemigos.update()
        
        # Actualizar posición de la cámara (scroll)
        # La cámara sigue al jugador, pero no se sale del mundo
        camara_x = jugador.rect.x - ANCHO_PANTALLA // 2
        camara_x = max(0, min(camara_x, ANCHO_MUNDO - ANCHO_PANTALLA))
        
        # Detectar colisiones con enemigos
        if pygame.sprite.spritecollide(jugador, enemigos, False):
            jugador.vidas -= 1
            if jugador.vidas <= 0:
                game_over = True
            else:
                # Pequeño efecto de "golpe" - empujar al jugador
                jugador.velocidad_y = -10
                jugador.rect.x -= 50  # Empujar hacia atrás
    
    # Dibujar todo en la superficie del mundo
    mundo.fill(CIELO)  # Color de fondo del cielo
    
    # Dibujar todos los sprites en el mundo
    for sprite in todos_los_sprites:
        mundo.blit(sprite.image, sprite.rect)
    
    # Dibujar la parte visible del mundo en la pantalla
    pantalla.blit(mundo, (0, 0), (camara_x, 0, ANCHO_PANTALLA, ALTO_PANTALLA))
    
    # Mostrar información en pantalla
    mostrar_texto(pantalla, f"Vidas: {jugador.vidas}", 30, 70, 10)
    mostrar_texto(pantalla, f"Posición: {jugador.rect.x}", 30, ANCHO_PANTALLA - 100, 10)
    
    if game_over:
        mostrar_texto(pantalla, "GAME OVER", 50, ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 - 50, ROJO)
        mostrar_texto(pantalla, "Presiona R para reiniciar", 30, ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 + 10)
    
    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
sys.exit()