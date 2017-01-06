# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 10:27:08 2017

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
                if self.r<2.0/18:
                    if self.r>=1.0/18:
                        self.x=self.x+1
                    else:
                        self.x=self.x-1
                    
                elif 4.0/18>self.r>=2.0/18:
                    if self.r>=3.0/18:
                        self.y=self.y+1
                    else:
                        self.y=self.y-1
                    
                elif 6.0/18>self.r>=4.0/18: 
                    if self.r>=5.0/18:
                        self.z=self.z+1
                    else:
                        self.z=self.z-1
                    
                elif 10.0/18>self.r>=6.0/18:
                    if self>=9.0/18:
                       self.x=self.x+0.5
                       self.y=self.y+0.5
                    elif self>=8.0/18:
                       self.x=self.x+0.5
                       self.y=self.y-0.5
                    elif self>=7.0/18:
                       self.x=self.x+0.5
                       self.z=self.z+0.5
                    else: 
                       self.x=self.x+0.5
                       self.z=self.z-0.5
                elif 14.0/18>self.r>=10.0/18:
                    if self>=13.0/18:
                       self.x=self.x-0.5
                       self.y=self.y+0.5
                    elif self>=12.0/18:
                       self.x=self.x-0.5
                       self.y=self.y-0.5
                    elif self>=11.0/18:
                       self.x=self.x-0.5
                       self.z=self.z+0.5
                    else: 
                       self.x=self.x-0.5
                       self.z=self.z-0.5
                else:
                    if self>=17.0/18:
                       self.y=self.y+0.5
                       self.z=self.z+0.5
                    elif self>=16.0/18:
                       self.y=self.y+0.5
                       self.z=self.z-0.5
                    elif self>=15.0/18:
                       self.y=self.y-0.5
                       self.z=self.z+0.5
                    else: 
                       self.y=self.y-0.5
                       self.z=self.z-0.5
                self.xone[i+1]=self.xone[i+1]+self.x
                self.yone[i+1]=self.yone[i+1]+self.y
                self.zone[i+1]=self.zone[i+1]+self.z
        
         
         
            
    def show(self):
        #plt.scatter(self.t,self.x2ave,s=4) 
        
        
        #self.a=np.polyfit(self.t,self.x2ave,1)
        #self.z=np.polyval(self.a,self.t);
        fig = plt.figure()
        ax = Axes3D(fig)
        
        ax.scatter(self.xone,self.yone,self.zone,c='b')
        ax.legend()
        #plt.xlim(0,100)
        #plt.ylim(0,100)
        
        #plt.xlabel(r'step number(=time)') 
        #plt.ylabel(r'x') 
       
        #plt.text(20,80,'<x2> versus time')
        ax.set_title('Random walk(for one walker) in there-dimensional face-centered cubic lattice')
        ax.set_zlabel('Z')
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        
A=random_walks()
A.calculate()
A.show()
