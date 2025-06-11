from class_bat import Bat
import random as rd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

threshold_SPL= 10
duration= 10
mean_vel= 10
std_vel= 10
SPL= 10
SPL_std= 10


class Model:
    def ___init__(self, N, arena, threshold_SPL=threshold_SPL):
        self.N = int(N)
        self.bat_list = []
        self.arena= arena
        self.threshold_SPL= threshold_SPL
        self.duration= duration

        vels= np.random.lognormal(mean_vel, std_vel, size= int(N))
        vels /= np.sqrt(2)

        self.vel_list= vels

    def gen_bats(self):
        bat_list=[]
        for i in range(0, int(self.N)):
            bat= Bat(0,0,np.random.normal(loc=SPL, scale=SPL_std))
            self.arena.assign_locations(bat)
            bat_list.append(bat)
        rd.shuffle(bat_list)
        self.bat_list= bat_list
        del bat_list

    def movement(self):
        for bat in self.bat_list:
            

    def run(self, timesteps, side, store_images=False, directory=""):
        time =0
        while time<timesteps:
            rd.shuffle(self.bat_list)

            