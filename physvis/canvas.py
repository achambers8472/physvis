import matplotlib.cm
import numpy as np
import pyglet


color_map = matplotlib.cm.get_cmap('viridis_r')


class Canvas:
    def __init__(self):
        pass

    def draw_point(self, x, colour=(255, 255, 255)):
        print(f'drawing point at {x}')
        pyglet.graphics.draw(
            1,
            pyglet.gl.GL_POINTS,
            ('v2i', (x[0], x[1])),
            ('c3B', colour,),
        )

    def draw_map(self, xs, ss):
        xs = np.asanyarray(xs)
        ss = np.asanyarray(ss)
        cs = (color_map(ss)[:, :3]*255).astype(int)
        print(xs.shape, ss.shape, cs.shape)
        print(xs.dtype, ss.dtype, cs.dtype)
        print(xs.flatten())
        print(cs.flatten())

        pyglet.graphics.draw(
            len(xs),
            pyglet.gl.GL_POINTS,
            ('v2i', xs.flatten()),
            ('c3B', cs.flatten()),
        )


    # def draw_circle(centre, radius):
