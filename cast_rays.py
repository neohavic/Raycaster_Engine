import pygame
import settings
import map1
import math

def cast_rays(screen, px, py, angle):
    start_angle = angle - settings.FOV / 2
    for ray in range(settings.NUM_RAYS):
        ray_angle = start_angle + ray * settings.DELTA_ANGLE
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        for depth in range(settings.MAX_DEPTH):
            x = px + depth * cos_a
            y = py + depth * sin_a

            i, j = int(x / settings.TILE_SIZE), int(y / settings.TILE_SIZE)
            if 0 <= i < settings.MAP_WIDTH and 0 <= j < settings.MAP_HEIGHT:
                if map1.game_map[j][i] == 1:
                    color = 255 / (1 + depth * depth * 0.0001)
                    wall_height = 30000 / (depth + 0.0001)
                    pygame.draw.rect(screen, (color, color, color),
                                     (ray * (settings.SCREEN_WIDTH //settings.NUM_RAYS),
                                      settings.SCREEN_HEIGHT // 2 - wall_height // 2,
                                      settings.SCREEN_WIDTH // settings.NUM_RAYS,
                                      wall_height))
                    break