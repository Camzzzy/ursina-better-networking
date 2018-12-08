from ursina import *


class Cylinder(Prismatoid):
    def __init__(self, resolution=4, radius=.5, height=1, **kwargs):
        super().__init__(
            base_shape=Circle(resolution=resolution, radius=.5),
            origin=(0,0),
            path=((0,0,0),(0,height,0)),
            thicknesses=((radius*2, radius*2),),
            mode='triangle',
            **kwargs
            )


if __name__ == '__main__':
    app = Ursina()
    Entity(model=Cylinder(6), color=color.color(60,1,1,.3))
    origin = Entity(model='quad', color=color.orange, scale=(.05, .05))
    ed = EditorCamera(rotation_speed = 200, panning_speed=200)
    app.run()