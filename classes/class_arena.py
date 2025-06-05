import numpy as np
import random as rd
from class_bat import Bat

class Arean:
    def __init___(self, xdims, ydims):
        self.xdims= xdims
        self.ydims= ydims
        
        self.xvals = np.arange(self.xdims[0],self.xdims[1]+self.xdims[2],self.xdims[2])
        self.yvals = np.arange(self.ydims[0],self.ydims[1]+self.ydims[2],self.ydims[2])

    def assign_locations(self,obj):
        #generate a random location
        
        # accept_values = False
        # while not accept_values:
        rand_x = rd.uniform(self.xdims[0], self.xdims[1])
        rand_y = rd.uniform(self.ydims[0], self.ydims[1])
            # accept_values = self.within_bush(rand_x,rand_y)
        
        if obj is not None:
            obj.x = rand_x
            obj.y = rand_y
        else:
            return rand_x,rand_y
        #can also be used model random walk in the space

    