import pygame
import math

# Configurable constants
MINIMAP_SCALE = .25
MAP_COLOR = (80, 80, 80)
WALL_COLOR = (200, 200, 200)
PLAYER_COLOR = (255, 0, 0)
RAY_COLOR = (255, 255, 0)

def draw_minimap(surface, game_map, tile_size, px, py, angle, offset=(10, 10)):
    map_width = len(game_map[0])
    map_height = len(game_map)
    map_width_px = map_width * tile_size
    map_height_px = map_height * tile_size

    minimap = pygame.Surface((int(map_width_px * MINIMAP_SCALE), int(map_height_px * MINIMAP_SCALE)))
    minimap.fill(MAP_COLOR)

    # Draw walls
    for j in range(map_height):
        for i in range(map_width):
            if game_map[j][i] == 1:
                rect = pygame.Rect(
                    int(i * tile_size * MINIMAP_SCALE),
                    int(j * tile_size * MINIMAP_SCALE),
                    int(tile_size * MINIMAP_SCALE),
                    int(tile_size * MINIMAP_SCALE)
                )
                pygame.draw.rect(minimap, WALL_COLOR, rect)

    # Draw player
    player_x = int(px * MINIMAP_SCALE)
    player_y = int(py * MINIMAP_SCALE)
    pygame.draw.circle(minimap, PLAYER_COLOR, (player_x, player_y), 4)

    # Draw facing direction
    line_end_x = int(player_x + math.cos(angle) * 20)
    line_end_y = int(player_y + math.sin(angle) * 20)
    pygame.draw.line(minimap, RAY_COLOR, (player_x, player_y), (line_end_x, line_end_y), 2)

    surface.blit(minimap, offset)