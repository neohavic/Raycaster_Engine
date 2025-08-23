# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Map settings
MAP_WIDTH = 10        # number of tiles horizontally
MAP_HEIGHT = 10       # number of tiles vertically
TILE_SIZE = 64        # pixels per tile

'''
# Raycasting settings - High Quality
FOV = 60 * (3.14159 / 180)  # convert degrees to radians
NUM_RAYS = SCREEN_WIDTH     # one ray per horizontal pixel
MAX_DEPTH = MAP_WIDTH * TILE_SIZE
'''

# Raycasting settings - Low Quality
FOV = 60 * (3.14159 / 180)  # convert degrees to radians
NUM_RAYS = 320
MAX_DEPTH = 240 * TILE_SIZE


# Player settings (optional defaults)
PLAYER_SPEED = 2.5
PLAYER_ROT_SPEED = 0.03
