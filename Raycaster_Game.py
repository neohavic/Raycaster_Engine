# raycaster_game.py
import pygame
import math
from minimap import draw_minimap
from cast_rays import *
#from cast_rays_textured import *
import settings
import map1
from machine_gun import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    pygame.mouse.get_rel()  # Reset relative motion

    px, py = settings.TILE_SIZE * 1.5, settings.TILE_SIZE * 1.5
    angle = 0

    running = True
    while running:
        
        mx, my = pygame.mouse.get_rel()
        angle += mx * 0.002  # Sensitivity factor

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: angle -= 0.03
        if keys[pygame.K_RIGHT]: angle += 0.03
        dx, dy = 0, 0
        if keys[pygame.K_w]:
            dx += math.cos(angle) * 3
            dy += math.sin(angle) * 3
        if keys[pygame.K_s]:
            dx -= math.cos(angle) * 3
            dy -= math.sin(angle) * 3
        if keys[pygame.K_a]:
            dx += math.sin(angle) * 3
            dy -= math.cos(angle) * 3
        if keys[pygame.K_d]:
            dx -= math.sin(angle) * 3
            dy += math.cos(angle) * 3
        if keys[pygame.K_ESCAPE]:
            running = False

        new_px = px + dx
        new_py = py + dy

        # Horizontal collision
        i, j = int(new_px / settings.TILE_SIZE), int(py / settings.TILE_SIZE)
        if map1.game_map[j][i] == 0:
            px = new_px

        # Vertical collision
        i, j = int(px / settings.TILE_SIZE), int(new_py / settings.TILE_SIZE)
        if map1.game_map[j][i] == 0:
            py = new_py
            
        screen.fill((30, 30, 30))
        cast_rays(screen, px, py, angle)
        draw_minimap(screen, map1.game_map, settings.TILE_SIZE, px, py, angle)
        
        draw_gun(screen)
        if pygame.mouse.get_pressed()[0]:
            fire_gun()
        update_bullets(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()