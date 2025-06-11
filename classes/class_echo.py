import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class Echo:
    def __init__(self, x, y, r, SPL, t):
        self.x = x
        self.y = y
        self.r = r
        self.SPL = SPL
        self.initiation_time= t

    def __key(self):
        return (self.x,self.y,self.r)

    def spreading_rule(self, current_time):
        velocity= 340 
        r= 340 * (current_time - self.t)
        self.r= r

    
