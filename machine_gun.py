import pygame
import time

# Constants
BULLET_SPEED = 20
FIRE_RATE = 900  # rounds per minute
FIRE_INTERVAL = 60 / FIRE_RATE
MAX_BULLET_SIZE = 10
MIN_BULLET_SIZE = 2
DEPTH_SCALE = 0.15

# State
last_shot_time = 0
bullets = []

def draw_gun(screen):
    """Draws the gun at bottom center, angled into the screen."""
    w, h = screen.get_size()
    base = (w // 2, h - 30)
    tip = (w // 2, h - 100)
    pygame.draw.line(screen, (160, 160, 160), base, tip, 10)
    pygame.draw.circle(screen, (90, 90, 90), base, 18)

def fire_gun():
    """Spawns a bullet from the gun tip if enough time has passed."""
    global last_shot_time
    now = time.time()
    if now - last_shot_time >= FIRE_INTERVAL:
        last_shot_time = now
        w, h = pygame.display.get_surface().get_size()
        bullets.append({
            'x': w // 2,
            'y': h - 100,
            'depth': 0
        })
        # Sound stub (optional)
        # pygame.mixer.Sound('machine_gun.wav').play()

def update_bullets(screen):
    """Updates bullet positions and renders them with depth-based scaling."""
    for bullet in bullets:
        bullet['y'] -= BULLET_SPEED
        bullet['depth'] += 1

        # Shrinking size based on depth
        size = max(MIN_BULLET_SIZE, MAX_BULLET_SIZE - bullet['depth'] * DEPTH_SCALE)
        pygame.draw.circle(screen, (255, 220, 0), (int(bullet['x']), int(bullet['y'])), int(size))