# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 00:17:55 2017

@author: john
"""

import matplotlib.pyplot as plt 
import numpy as np 
import random as rd 
from mpl_toolkits.mplot3d import Axes3D  
class random_walks(): 
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        self.r=0
        self.b=0
        
        self.xone = [0]*1000
        self.yone = [0]*1000
        self.zone = [0]*1000
    def calculate(self):
        for i in range(999):
            self.r=rd.random()
            if self.r<2.0/6:
                if self.r>=1.0/6:
                    self.x=self.x+1
                else:
                    self.x=self.x-1
                
            elif 4.0/6>self.r>=2.0/6:
                if 4.0/6>self.r>=3.0/6:
                    self.y=self.y+1
                else:
                    self.y=self.y-1
                
                
            else: 
                if self.r>=5.0/6:
                    self.z=self.z+1
                else:
                    self.z=self.z-1
            self.xone[i+1]=self.xone[i+1]+self.x
            self.yone[i+1]=self.yone[i+1]+self.y
            self.zone[i+1]=self.zone[i+1]+self.z
         
         
            
    def show(self):
        #plt.scatter(self.t,self.x2ave,s=4) 
        
        
        #self.a=np.polyfit(self.t,self.x2ave,1)
        #self.z=np.polyval(self.a,self.t);
        fig = plt.figure()
        ax = Axes3D(fig)
        
        ax.scatter(self.xone,self.yone,self.zone,c='r')
        ax.legend()
        #plt.xlim(0,100)
        #plt.ylim(0,100)
        
        #plt.xlabel(r'step number(=time)') 
        #plt.ylabel(r'x') 
       
        #plt.text(20,80,'<x2> versus time')
        ax.set_title('Random walk(one walker 1000 steps) in there dimensional simple-cubic lattice')
        ax.set_zlabel('Z')
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        ax.show()
A=random_walks()
A.calculate()
A.show()
