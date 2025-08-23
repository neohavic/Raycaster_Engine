import pygame
import math
import settings
import map1

textures = {}

def load_textures(texture_paths):
    for tile_id, path in texture_paths.items():
        image = pygame.image.load(path).convert()
        texture = pygame.transform.scale(image, (256, 256))
        textures[tile_id] = texture

def cast_rays(screen, px, py, angle):
    start_angle = angle - settings.FOV / 2
    ray_width = settings.SCREEN_WIDTH // settings.NUM_RAYS
    proj_plane_dist = (settings.SCREEN_WIDTH / 2) / math.tan(settings.FOV / 2)

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
                tile_id = map1.game_map[j][i]
                if tile_id in textures:
                    # Correct fish-eye distortion
                    corrected_depth = depth * math.cos(ray_angle - angle)

                    # Compute wall height from corrected depth
                    wall_height = (settings.TILE_SIZE / corrected_depth) * proj_plane_dist
                    wall_height = min(settings.SCREEN_HEIGHT, wall_height)

                    # Determine wall orientation
                    dx = x - px
                    dy = y - py
                    if abs(dx) > abs(dy):
                        offset = y % settings.TILE_SIZE  # Vertical wall
                    else:
                        offset = x % settings.TILE_SIZE  # Horizontal wall

                    # Sample texture slice
                    texture = textures[tile_id]
                    tex_x = int(offset / settings.TILE_SIZE * texture.get_width())
                    tex_x = max(0, min(texture.get_width() - 1, tex_x))

                    column = texture.subsurface(tex_x, 0, 1, texture.get_height())
                    scaled_column = pygame.transform.scale(column, (ray_width, int(wall_height)))

                    # Blit to screen
                    screen.blit(scaled_column, (
                        ray * ray_width,
                        settings.SCREEN_HEIGHT // 2 - int(wall_height) // 2
                    ))
                    break