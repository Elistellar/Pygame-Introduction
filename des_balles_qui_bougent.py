import random
import pygame


# Ouvre une fenêtre Pygame de 640x480 pixels
screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("Fenête pygame !")

# Un objet Clock pour gérer les IPS
clock = pygame.time.Clock()

# Un groupe de sprites pour gérer tous nos objets
camera = pygame.sprite.Group()

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, center, group):
        super().__init__(group)
        
        self.pos = pygame.math.Vector2(center)
        
        self.vel = pygame.math.Vector2(1, 0)
        self.speed = 0.5
        self.vel.rotate_ip(random.randint(0, 360))
        
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        self.radius = 10
        
    def update(self, dt):
        
        # Prévoit la position future de la balle
        future_x = self.pos.x + self.vel.x * dt * self.speed
        future_y = self.pos.y + self.vel.y * dt * self.speed
        
        # Fait rebondir la balle sur les bords de l'écran
        if future_x - self.radius < 0 or future_x + self.radius > screen.get_width():
            self.vel.x *= -1
        if future_y - self.radius < 0 or future_y + self.radius > screen.get_height():
            self.vel.y *= -1
            
        # Bouge la balle
        self.pos += self.vel * dt * self.speed
        
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

# On instancie 10 balles au centre de l'écran
for _ in range(10):
    Ball(
        (screen.get_width() / 2, screen.get_height() / 2), # centre de l'écran
        camera
    )

# Boucle principale
running = True
while running:
    clock.tick(30) # On limite le nombre d'images à 30 par seconde
    
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
            running = False
            
    # Mise à jour des objets
    dt = clock.get_time()# Temps écoulé depuis le dernier tour de boucle (en ms)
    camera.update(dt)
    
    # Rendu à l'écran
    screen.fill((255, 255, 255)) # On remplit l'écran de blanc
    
    for sprite in camera.sprites():
        sprite.render(screen)
    
    pygame.display.flip() # Mise à jour de l'écran
    