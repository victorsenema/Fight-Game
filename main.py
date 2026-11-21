import glfw
from OpenGL.GL import *
import numpy as np

import tools.archives_manipulation.sprites.sprites_data as sprites_data

#CANVAS
HEIGHT, WIDTH = 600, 500
CANVAS = np.full((HEIGHT, WIDTH, 3), 255, dtype=np.uint8)


def create_window(width, height):
    if not glfw.init():
       return None
    window = glfw.create_window( width, height, "Mini Paint", None, None )

    if not window:
        glfw.terminate()
        return None
    
    glfw.make_context_current(window)
    return window

    return window

def update(window):
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glRasterPos2f(-1, -1)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":

    sprites_data.print_info()

    window = create_window(WIDTH, HEIGHT)
    update(window)