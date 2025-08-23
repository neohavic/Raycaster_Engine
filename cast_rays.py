import pygame
import settings
import map1
import math

def cast_rays(screen, px, py, angle):
    start_angle = angle - settings.FOV / 2
    ray_width = settings.SCREEN_WIDTH // settings.NUM_RAYS

    for ray in range(settings.NUM_RAYS):
        ray_angle = start_angle + ray * (settings.FOV / settings.NUM_RAYS)
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        for depth in range(1, settings.MAX_DEPTH):
            x = px + depth * cos_a
            y = py + depth * sin_a

            i = int(x // settings.TILE_SIZE)
            j = int(y // settings.TILE_SIZE)

            if 0 <= i < settings.MAP_WIDTH and 0 <= j < settings.MAP_HEIGHT:
                if map1.game_map[j][i] == 1:
                    # Correct fish-eye distortion
                    corrected_depth = depth * math.cos(ray_angle - angle)

                    # Calculate wall height using projection formula
                    proj_plane_dist = (settings.SCREEN_WIDTH / 2) / math.tan(settings.FOV / 2)
                    wall_height = (settings.TILE_SIZE / corrected_depth) * proj_plane_dist

                    # Clamp wall height to screen bounds
                    wall_height = min(settings.SCREEN_HEIGHT, wall_height)

                    # Depth-based shading
                    shade = 255 / (1 + corrected_depth * corrected_depth * 0.0001)
                    color = (shade, shade, shade)

                    # Draw vertical slice
                    pygame.draw.rect(
                        screen,
                        color,
                        (
                            ray * ray_width,
                            settings.SCREEN_HEIGHT // 2 - wall_height // 2,
                            ray_width,
                            wall_height
                        )
                    )
                    break