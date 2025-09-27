from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# --- Settings ---
CHUNK_SIZE = 10
RENDER_DISTANCE = 3   # how many chunks around player will load
GROUND_Y = 0          # the flat ground level

player = FirstPersonController()
Sky()

chunks = {}

def generate_chunk(cx, cz):
    """Generate a flat chunk at chunk coords (cx, cz)."""
    if (cx, cz) in chunks:
        return  # already made

    blocks = []
    for x in range(CHUNK_SIZE):
        for z in range(CHUNK_SIZE):
            world_x = cx * CHUNK_SIZE + x
            world_z = cz * CHUNK_SIZE + z

            block = Entity(
                model='cube',
                color=color.white,
                texture='grass.png',
                position=(world_x, GROUND_Y, world_z),
                parent=scene,
                collider='box'
            )
            blocks.append(block)

    chunks[(cx, cz)] = blocks

def update():
    # Find which chunk player is in
    cx = floor(player.x / CHUNK_SIZE)
    cz = floor(player.z / CHUNK_SIZE)

    # Generate chunks around player
    for x in range(cx - RENDER_DISTANCE, cx + RENDER_DISTANCE + 1):
        for z in range(cz - RENDER_DISTANCE, cz + RENDER_DISTANCE + 1):
            generate_chunk(x, z)

def input(key):
    if key == 'escape':
        application.quit()

app.run()
