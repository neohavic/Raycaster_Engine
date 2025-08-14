import pygame
import settings
import map1
import math

def cast_rays(screen, px, py, angle, wall_texture):
    start_angle = angle - settings.FOV / 2
    texture_width, texture_height = wall_texture.get_size()

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
                    # Fish-eye correction
                    corrected_depth = depth * math.cos(ray_angle - angle)
                    wall_height = 30000 / (corrected_depth + 0.0001)

                    # Texture sampling
                    hit_x = x % settings.TILE_SIZE if map1.game_map[j][i] else y % settings.TILE_SIZE
                    tex_x = int(hit_x / settings.TILE_SIZE * texture_width)

                    # Scale texture slice
                    column = wall_texture.subsurface(tex_x, 0, 1, texture_height)
                    column = pygame.transform.scale(column, (
                        settings.SCREEN_WIDTH // settings.NUM_RAYS,
                        int(wall_height)
                    ))

                    screen.blit(column, (
                        ray * (settings.SCREEN_WIDTH // settings.NUM_RAYS),
                        settings.SCREEN_HEIGHT // 2 - wall_height // 2
                    ))
                    break