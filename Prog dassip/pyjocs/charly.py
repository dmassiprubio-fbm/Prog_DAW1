import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 120
ENEMY_SPAWN = 200
SHOOT_SPAWN = 1000
FONT = pygame.font.SysFont(name ="", size = 40)
SCROLL_SPEED = 3

pygame.display.set_caption("SUPER JUEGO DE MURCIANOS")

fondo_path ="/home/ptdii/Documents/pygame/media/estrellas.jpg"

class FondoDeslizante:
    def __init__(self):
        original_image = pygame.image.load(fondo_path)
        self.image = pygame.transform.scale(original_image, (WIDTH, HEIGHT)).convert()
        self.offset_y = 0.0
        self.rect1 = pygame.Rect(0,0, WIDTH, HEIGHT)
        self.rect2 = pygame.Rect(0,-HEIGHT, WIDTH, HEIGHT)

    def actualizar(self, velocidad, delta_time):
        self.offset_y += velocidad * delta_time * FPS   
        if self.offset_y >= HEIGHT:
            self.offset_y = 0.0

    def draw(self, window):
        window.blit(self.image, (0, self.offset_y))

        if self.offset_y > 0:
            window.blit(self.image, (0, self.offset_y - HEIGHT))


class MainCharacter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        #self.color = (0, 128, 0)
        self.speed = 7.5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.life = 3
        self.image = pygame.image.load("/home/ptdii/Documents/pygame/media/nave.jpg")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 90) 


    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.x, self.y))

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        #self.color = ("red")
        self.speed = 6
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load("/home/ptdii/Documents/pygame/media/marciano.jpg")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # self.image = pygame.transform.rotate(self.image, 90) 
    
    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.x, self.y))
    
    def movement(self):
        self.y += self.speed    

class Bullet:
    def __init__(self, x, y):
        self.x = x + 20 - 5
        self.y = y
        self.height = 25
        self.width = 10
        #self.color = "green"
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load("/home/ptdii/Documents/pygame/media/flexipolla.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.x, self.y))

    def movement(self):
        self.y -= self.speed
        
def create_bullet(x, y):
    bullets.append(Bullet(x, y))

def create_explosion(x, y):
    explosions.append(Explosion(x, y))

 
class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.image = pygame.image.load("/home/ptdii/Documents/pygame/media/explosion.jpg")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        window.blit(self.image, (self.x, self.y))


play = True 
DAVID_LEPROSO = MainCharacter(WIDTH/2, HEIGHT -40)
enemies = []
bullets = []
explosions = []
clock = pygame.time.Clock()
time_passed = 0
last_bullet = 0
cooldown = 400
puntuacion = 0

fondo = FondoDeslizante()
background_y = 0
velocidad = 3
last_time = 0

while play:
    
    time_passed += clock.tick(FPS)
    actual_time = pygame.time.get_ticks()
    delta_time = (actual_time - last_time) /1000
    last_time = actual_time


    if time_passed >= ENEMY_SPAWN:
        enemies.append(Enemy(random.randint(0,WIDTH), -175))
        enemies.append(Enemy(random.randint(0,WIDTH), -175))
        time_passed = 0
    
    time_passed += clock.tick(FPS)
    if time_passed >= SHOOT_SPAWN:
        create_bullet(DAVID_LEPROSO.x, DAVID_LEPROSO.y)
        time_passed = 0

    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            play = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if DAVID_LEPROSO.rect.top > 0:
            velocidad += 0.5
    
    if keys[pygame.K_s]:
        # if DAVID_LEPROSO.rect.bottom < HEIGHT:
        if velocidad >= 0:
            velocidad -= 0.5

    if keys[pygame.K_a]:
        if DAVID_LEPROSO.rect.left > 0:
            DAVID_LEPROSO.x -= DAVID_LEPROSO.speed
    
    if keys[pygame.K_d]:
        if DAVID_LEPROSO.rect.right < WIDTH:
            DAVID_LEPROSO.x += DAVID_LEPROSO.speed

    if keys[pygame.K_SPACE]:
        if pygame.time.get_ticks() - last_bullet > cooldown:
            create_bullet(DAVID_LEPROSO.x, DAVID_LEPROSO.y)
            last_bullet = pygame.time.get_ticks()
    

    if keys[pygame.K_r]:
        DAVID_LEPROSO = MainCharacter(WIDTH/2, HEIGHT -40)
        bullets.clear()
        puntuacion = 0

    if keys[pygame.K_ESCAPE]:
        play = False
        
    background_y += SCROLL_SPEED 
    if background_y >= HEIGHT:  
        background_y = 0
    fondo.actualizar(velocidad, delta_time)
    fondo.draw(WINDOW)


    if DAVID_LEPROSO.life == 0:
        restart = FONT.render("[R] para reiniciar", True, "white")
        WINDOW.blit(restart, (175, 400))
        salir = FONT.render("[ESC] para salir", True, "white")
        WINDOW.blit(salir, (400, 400))


    
        lost_text = FONT.render("GAME OVER", True, "red")
        WINDOW.blit(lost_text, (400, 250))
        lost_text = FONT.render(f"Puntuación: {puntuacion}", True, "white")
        WINDOW.blit(lost_text, (400, 300))

    else:
        life_text = FONT.render(f"VIDA: {DAVID_LEPROSO.life}", True,"white")
        WINDOW.blit(life_text, (10, 10))
        life_text = FONT.render(f"Puntuación: {puntuacion}", True,"white")
        WINDOW.blit(life_text, (10, 35))


        DAVID_LEPROSO.draw(WINDOW)

        for enemy in enemies:
            enemy.movement()
            enemy.draw(WINDOW)
            for bullet in bullets:
                if pygame.Rect.colliderect(enemy.rect, bullet.rect):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    create_explosion(enemy.x, enemy.y)
                    puntuacion += 10

        for enemy in enemies:
            enemy.movement()
            enemy.draw(WINDOW)
            if pygame.Rect.colliderect(DAVID_LEPROSO.rect, enemy.rect):
                DAVID_LEPROSO.life -= 1
                enemies.remove(enemy)
                
        
        for bullet in bullets:
            bullet.movement()
            bullet.draw(WINDOW)

            
        for explosion in explosions:
            explosion.draw(WINDOW)
            explosions.remove(explosion)
            

    pygame.display.update()