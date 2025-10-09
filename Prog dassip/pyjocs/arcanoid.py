import pygame
import random

pygame.init()

HEIGHT = 800
WIDTH = 1000
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60
ENEMY_SPAWN = 500
FONT = pygame.font.SysFont("Comic Sans", 40)
SCROLL_SPEED = 3

pygame.display.set_caption("Marcianitos")
# Carga la imagen de fondo
imagen_path = "pyjocs/media/estrellas.jpg"

class FondoDeslizanteOptimizado:
    def __init__(self, imagen_path=None):
        if imagen_path:
            try:
                # Cargar y optimizar la imagen
                imagen_original = pygame.image.load(imagen_path)
                self.imagen = pygame.transform.scale(imagen_original, (WIDTH, HEIGHT)).convert()
                print(f"✓ Imagen cargada exitosamente: {imagen_path}")
            except (pygame.error, FileNotFoundError) as e:
                print(f"✗ Error al cargar {imagen_path}: {e}")
                print("Usando fondo generado como respaldo")
                self._crear_fondo_generado()
        else:
            print("No se especificó imagen, usando fondo generado")
            self._crear_fondo_generado()
        
          # Usar punto flotante para posición más suave
        self.offset_y = 0.0
        
        # Pre-calcular el rectángulo de destino para evitar crearlo cada frame
        self.rect1 = pygame.Rect(0, 0, WIDTH, HEIGHT)
        self.rect2 = pygame.Rect(0, -HEIGHT, WIDTH, HEIGHT)

    def _crear_fondo_generado(self):
        """Crear fondo generado de forma más eficiente"""
        self.imagen = pygame.Surface((WIDTH, HEIGHT))
        
        # Usar draw.rect en lugar de líneas individuales para mejor rendimiento
        colores = [
            ((70, 130, 255), 0, HEIGHT//4),
            ((50, 150, 255), HEIGHT//4, HEIGHT//2),
            ((30, 170, 255), HEIGHT//2, 3*HEIGHT//4),
            ((10, 190, 255), 3*HEIGHT//4, HEIGHT)
        ]
        
        for color, y_inicio, y_fin in colores:
            pygame.draw.rect(self.imagen, color, (0, y_inicio, WIDTH, y_fin - y_inicio))
        
        # Añadir algunas "nubes" para hacer más interesante el fondo
        for i in range(8):
            x = (i * WIDTH // 8) + 50
            y = (i % 3) * (HEIGHT // 3) + 50
            tamaño = 40 + (i % 3) * 20
            
            # Crear superficie temporal para la transparencia
            nube = pygame.Surface((tamaño * 2, tamaño))
            nube.set_alpha(80)
            nube.fill((255, 255, 255))
            
            # Dibujar círculos para formar la nube
            pygame.draw.circle(nube, (255, 255, 255), (tamaño//2, tamaño//2), tamaño//2)
            pygame.draw.circle(nube, (255, 255, 255), (tamaño, tamaño//2), tamaño//3)
            pygame.draw.circle(nube, (255, 255, 255), (tamaño + tamaño//2, tamaño//2), tamaño//4)
            
            self.imagen.blit(nube, (x, y))
        
        # Convertir para mejor rendimiento
        self.imagen = self.imagen.convert()
        # Usar punto flotante para posición más suave
        self.offset_y = 0.0
        
        # Pre-calcular el rectángulo de destino para evitar crearlo cada frame
        self.rect1 = pygame.Rect(0, 0, WIDTH, HEIGHT)
        self.rect2 = pygame.Rect(0, -HEIGHT, WIDTH, HEIGHT)
    
    def actualizar(self, velocidad, delta_time):
        """Usar delta time para movimiento independiente del framerate"""
        # Movimiento basado en tiempo real, no en frames
        self.offset_y += velocidad * delta_time * 60  # 60 para normalizar
        
        # Reiniciar cuando el offset llegue a la altura de la pantalla
        if self.offset_y >= HEIGHT:
            self.offset_y = 0.0
    
    def dibujar(self, superficie):
        """Dibujo optimizado usando offset en lugar de mover rectángulos"""
        y_pos = int(self.offset_y)
        
        # Dibujar el fondo principal
        superficie.blit(self.imagen, (0, y_pos))
        
        # Dibujar el fondo que viene desde arriba (solo si es necesario)
        if y_pos > 0:
            superficie.blit(self.imagen, (0, y_pos - HEIGHT))

class Main_Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 50
        self.color = "red"
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load("pyjocs/media/nave.svg")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 90)

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(window, self.color, self.rect)
        WINDOW.blit(self.image, (self.x, self.y))

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 75
        self.width = 75
        self.color = "purple"
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load("pyjocs/media/marciano.svg")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(window, self.color, self.rect)
        WINDOW.blit(self.image, (self.x, self.y))

    def movement(self):
        self.y += self.speed

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 10
        self.color = "green"
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.rect)

    def movement(self):
        self.y -= self.speed

class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 75
        self.width = 75
        self.color = "green"
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load("pyjocs/media/explosion.svg")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(window, self.color, self.rect)
        WINDOW.blit(self.image, (self.x, self.y))

def create_bullets(x, y):
    global last_bullet
    if pygame.time.get_ticks() - last_bullet > cooldown:
        bullets.append(Bullet(x, y))
        last_bullet = pygame.time.get_ticks()

def manage_keys(keys):
    global velocidad_actual
    if keys[pygame.K_w]:
        velocidad_actual += 0.5
        ENEMY_SPAWN -= 10
        #main_character.y -= main_character.speed       
    if keys[pygame.K_s]:
        ENEMY_SPAWN += 10
        velocidad_actual -= 0.5
        #main_character.y += main_character.speed
    if keys[pygame.K_a]:
        main_character.x -= main_character.speed
    if keys[pygame.K_d]:
        main_character.x += main_character.speed
    if keys[pygame.K_SPACE]:
        create_bullets(main_character.x, main_character.y)

play = True

clock = pygame.time.Clock()
time_passed = 0

fondo = FondoDeslizanteOptimizado(imagen_path)

life = 5
points = 0
bullets = []
last_bullet = 0
cooldown = 500
backgroud_y = 0
velocidad_actual = 2.2
main_character = Main_Character((WIDTH/2)-25, HEIGHT-55)
main_character.draw(WINDOW)

enemies: list[Enemy] = []
explosions: list[Explosion] = []

enemies.append(Enemy(500, 100))
tiempo_anterior = 0
while play:

    tiempo_actual = pygame.time.get_ticks()
    delta_time = (tiempo_actual - tiempo_anterior) / 1000.0
    tiempo_anterior = tiempo_actual

    time_passed += clock.tick(FPS)
    if time_passed >= ENEMY_SPAWN:
        enemies.append(Enemy(random.randint(0, WIDTH), -100))
        time_passed = 0

    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    manage_keys(keys)

   
    for e in events:
        if e.type == pygame.QUIT:
            play = False
    

    backgroud_y += SCROLL_SPEED
    if backgroud_y >= HEIGHT:
        backgroud_y = 0

    # Actualizar fondo
    fondo.actualizar(velocidad_actual, delta_time)
    
    # Dibujar
    fondo.dibujar(WINDOW)

    main_character.draw(WINDOW)

    for enemy in enemies:
        enemy.movement()
        enemy.draw(WINDOW)
        if pygame.Rect.colliderect(enemy.rect, (0,800), (1000, 800)):
            enemies.remove(enemy)
            #points += 1
            print("colision")
        if pygame.Rect.colliderect(main_character.rect, enemy.rect):
            life -= 1
            enemies.remove(enemy)
            

        for b in bullets:
            if pygame.Rect.colliderect(b.rect, enemy.rect):
                enemies.remove(enemy)
                bullets.remove(b)
                points += 1
                explosions.append(Explosion(enemy.x,enemy.y))

    for b in bullets:
        b.movement()
        b.draw(WINDOW)

        
    life_text = FONT.render(f"Vida: {life}", True, "white")
    WINDOW.blit(life_text, (20,20))
    life_text = FONT.render(f"Punts: {points}", True, "white")
    WINDOW.blit(life_text, (20,70))

    pygame.display.update()

