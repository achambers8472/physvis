import matplotlib.cm
import numpy as np
import pyglet

from . import space


def array_to_image(array, format='RGBA'):
    data = np.swapaxes(array, 0, 1)
    tex_data = (pyglet.gl.GLubyte*data.size)(*data.flatten().astype('uint8'))
    image = pyglet.image.ImageData(
        data.shape[0],
        data.shape[1],
        format,
        tex_data,
        pitch=data.shape[1]*data.shape[-1]*1,
    )
    return image


class Canvas:
    def __init__(self, size):
        self.size = size


    def draw_point(self, x, r, colour=(255, 255, 255, 255)):
        colour = np.asanyarray(colour)
        image = array_to_image(np.ones((2*r, 2*r, 4))*colour)
        ll = x - r
        image.blit(ll[0], ll[1])

    def draw_line(self, xi, xf, colour=(255, 255, 255, 255)):
        pyglet.graphics.draw(
            2,
            pyglet.gl.GL_LINES,
            ('v2i', (xi[0], xi[1], xf[0], xf[1])),
            ('c4B', colour + colour,),
        )


    def draw_array(
            self,
            pos,
            array,
            alpha=1.0,
            mask=None,
            color_map='viridis_r',
    ):
        color_map = matplotlib.cm.get_cmap(color_map)

        data = color_map(1 - array)*255
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

        image.blit(
            pos[0], pos[1],
            width=self.size[0]/2,
            height=self.size[1])
