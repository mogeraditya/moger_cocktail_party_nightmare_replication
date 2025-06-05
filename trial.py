#define classes of bats and for sound propagation

import numpy as np

class Bat:
    def __init__(self, x, y, speed, direction, sound_intensity):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.sound_intensity = sound_intensity