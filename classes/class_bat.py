#define classes of bats and for sound propagation

import numpy as np

#remember to put these in fixed parameters
ref_dist=20 #cm
right_boundary= 10 #define arena
upper_boundary= 10 
threshold_SPL=10

class Bat:
    def __init__(self, x, y,SPL):
        self.x = x
        self.y = y

        self.SPL = SPL

        self.xvel= 0
        self.yvel= 0

        self.calling= False #variable that decides if the bat is calling or not
        self.call_times= [] #times at which the bat will call
        # self.call_effort= call_effort #likelihood of the bat calling
        
        self.SPL= SPL

        #movement variables
        self.total_steps=0
        self.total_distance=0

        self.call_instances=0

    def __key(self):
        return (self.x, self.y, self.SPL)

    def __eq__(self, other):
        if not isinstance(other, Bat):
            return NotImplemented
        return self.__key()==other.__key()

    def dist(self,caller):
        xdist= self.x-caller.x
        ydist= self.y-caller.y
        return (np.sqrt(xdist**2+ydist**2)) 
    
    def decay(self,dist):
        if not self.calling:
            return 0
        else:
            if dist>0:
                TL = 20*np.log10(dist/ref_dist)
                return self.SPL - TL

            else:
                return self.SPL
        
    def move(self, location):
        dist= np.sqrt((self.x- location[0])**2+((self.y- location[1])**2))

        if dist>0:
            x,y= (location[0] -self.x)/dist, (location[1]-self.y)/dist #vector from self to location

        else:
            x,y =0,0

        #use velocity to move
        if dist> np.sqrt((x*self.velx)**2+(y*self.vely)**2):
            self.x= x*self.velx
            self.y= y*self.vely

        else:
            self.x = location[0]
            self.y = location[1]

        right_boundary= right_boundary
        upper_boundary= upper_boundary
        left_boundary= 0
        lower_boundary= 0

        if self.x > right_boundary:
            self.x= right_boundary-(self.x-right_boundary)
            if self.velx >0 :
                self.velx*=-1
        
        if self.x < left_boundary:
           self.x = left_boundary + (left_boundary - self.x)
           if self.velx<0:
               self.velx *= -1
        
        if self.y > upper_boundary:
           self.y = upper_boundary - (self.y-upper_boundary)
           if self.vely>0:
               self.vely *= -1
        
        if self.y < lower_boundary:
           self.y = lower_boundary + (lower_boundary-self.y)
           if self.vely<0:
               self.vely *= -1

    #active space?????
    def find_active_space(self): #For visualization purposes
        SPL = self.SPL
        return (20*10**((SPL-threshold_SPL)/ref_dist))
    #creates a ball arund the bat,  for visualization

