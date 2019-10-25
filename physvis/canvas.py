import matplotlib.cm
import numpy as np
import pyglet

from . import space




color_map = matplotlib.cm.get_cmap('viridis_r')


class Canvas:
    def __init__(self):
        pass

    def draw_point(self, x, colour=(255, 255, 255)):
        pyglet.graphics.draw(
            1,
            pyglet.gl.GL_POINTS,
            ('v2i', (x[0], x[1])),
            ('c3B', colour,),
        )

    def draw_map(self, array, alpha=1.0, mask=None):
        data = color_map(array)*255
        data[..., 3] *= alpha

        if mask is not None:
            data[~mask, 3] = 0

        data = np.swapaxes(data, 0, 1)

        tex_data = (pyglet.gl.GLubyte*data.size)(*data.flatten().astype('uint8'))
        image = pyglet.image.ImageData(
            data.shape[0],
            data.shape[1],
            'RGBA',
            tex_data,
            pitch=data.shape[1]*data.shape[-1]*1,
        )

        image.blit(0, 0, width=480, height=480)
