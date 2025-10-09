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
fondo = pygame.image.load("pyjocs/media/estrellas.jpg")
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT*2))

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
    if keys[pygame.K_w]:
        main_character.y -= main_character.speed       
    if keys[pygame.K_s]:
        main_character.y += main_character.speed
    if keys[pygame.K_a]:
        main_character.x -= main_character.speed
    if keys[pygame.K_d]:
        main_character.x += main_character.speed
    if keys[pygame.K_SPACE]:
        create_bullets(main_character.x, main_character.y)

play = True

clock = pygame.time.Clock()
time_passed = 0

life = 5
points = 0
bullets = []
last_bullet = 0
cooldown = 500
backgroud_y = 0

main_character = Main_Character(100, 100)
main_character.draw(WINDOW)

enemies: list[Enemy] = []
explosions: list[Explosion] = []

enemies.append(Enemy(500, 100))

while play:

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

    WINDOW.blit(fondo, (0, backgroud_y))
    WINDOW.blit(fondo, (0, backgroud_y - HEIGHT))
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

