import pygame
import random

pygame.init()

HEIGHT = 800
WIDTH = 1000
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60
ENEMY_SPAWN = 1000
ULTI_SPAWN = 3000

class MainCharacter:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 20
        #self.height = 50
        #self.width = 50
        self.color = "purple"
        self.speed = 10
        self.rect = pygame.Rect(self.x - self.size //2, self.y, self.size, self.size + 35)

        self.invulnerable = False
        self.invulnerable_time = 0

    
    def draw(self, window):
        if not self.invulnerable or (pygame.time.get_ticks()//200) % 2 == 0:
            points = [ 
                (self.x, self.y),
                (self.x - self.size //2, self.y + self.size + 35),
                (self.x + self.size //2, self.y + self.size + 35),
            ]
            pygame.draw.polygon(window, self.color, points)
            
            self.rect = pygame.Rect(self.x - self.size //2, self.y, self.size, self.size + 35)
        

class alien:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 50
        self.color = "green"
        self.speed = 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.rect)
    
    def movement(self):
        self.y += self.speed

class shoot: #
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 20
        self.color = 'red'
        self.speed = 20
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)
        pygame.draw.rect(window, self.color, self.rect) 

    def movement(self):
        self.y -= self.speed

def create_bullets(x, y):
    global last_bullet
    if pygame.time.get_ticks() - last_bullet > cooldown:
        shoots.append(shoot(x, y))
        last_bullet = pygame.time.get_ticks()      

class ulti:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 15
        self.width = 15
        self.color = "pink"
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.color, self.rect)
    
    def movement(self):
        self.y += self.speed


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
    
    #Limites arriba y abajo
    if main_character.y <0:
        main_character.y = 0
    if main_character.y > HEIGHT - 70:
        main_character.y = HEIGHT - 70

    #Pasar de derecha a izquierda i viceversa
    if main_character.x < 10:
        main_character.x = 10
    elif main_character.x > WIDTH - 10:
        main_character.x = WIDTH - 10

play = True 

clock = pygame.time.Clock()
time_passed = 0
cooldown = 200
last_bullet = 0
backgroud_y = 0
contador_vidas = 3
game_over = False
pantalla_go = 0
main_character = MainCharacter(475,700)

shoots: list[shoot] = []

enemies: list[alien] = []
enemies.append(alien(500, 100))

ultimate: list[ulti] = []
ultimate.append(ulti(0,999))


while play:
    time_passed += clock.tick(FPS)
    if time_passed >= ENEMY_SPAWN:
        enemies.append(alien(random.randint(0, WIDTH), - 100))
        time_passed = 100

    if time_passed >= ULTI_SPAWN:
        enemies.append(ulti(random.randint(0, WIDTH), - 100))
        time_passed = 50
    
    if time_passed >= ENEMY_SPAWN:
        enemies.append(shoot(main_character.x, main_character.y))
        time_passed = 50
        

    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            play = False

    if not game_over:
        keys = pygame.key.get_pressed()
        manage_keys(keys)

    
        

        WINDOW.fill((0, 0, 0))  # Limpia la pantalla con negro
        main_character.draw(WINDOW)

        for enemy in enemies:
            enemy.movement()
            enemy.draw(WINDOW)


            for b in shoots:
                if pygame.Rect.colliderect(b.rect, enemy.rect):
                    enemies.remove(enemy)
                    shoots.remove(b)
            
            if enemy.y == 750:
                enemies.remove(enemy)
        
        for ultimates in ultimate:
            ultimates.movement()
            ultimates.draw(WINDOW)
            if main_character.rect.colliderect(ultimates.rect):
                ultimate.remove(ultimates)

            
        
        for b in shoots:
            b.movement()
            b.draw(WINDOW)
        
        # if main_character.invulnerable > 0:
        #     main_character.invulnerable -= clock.get_time()

        for enemy in enemies:
            if main_character.rect.colliderect(enemy.rect) and not main_character.invulnerable:
                    contador_vidas = contador_vidas - 1
                    main_character.invulnerable = True
                    main_character.invulnerable_time = 1500
                    if contador_vidas == 0:
                        game_over = True
                        pantalla_go = pygame.time.get_ticks()

        if main_character.invulnerable:
            main_character.invulnerable_time -= clock.get_time()
            if main_character.invulnerable_time <= 0:
                main_character.invulnerable = False
                main_character.invulnerable_time = 0
    
    else:
        WINDOW.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 80)
        text = font.render("GAME OVER", True, (255, 0, 0))
        WINDOW.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

        # comprobar si ya pasaron 5 segundos
        if pygame.time.get_ticks() - pantalla_go >= 5000:
            play = False


    
    pygame.display.update()  # Actualiza la pantalla

    


pygame.quit()

