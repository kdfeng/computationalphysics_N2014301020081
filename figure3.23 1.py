# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:56:57 2016

@author: john
"""

import matplotlib.pyplot as plt 
import numpy as np 
class circularstadium_trajectory(): 
    def __init__(self,x0,y0,vx0,vy0,N,dt): 
        self.x = x0 
        self.y = y0 
        self.vx = vx0 
        self.vy = vy0 
        self.N = N 
        self.dt = dt
        self.t=0
        self.tra_x = [x0] 
        self.tra_y = [y0] 
        self.tra_vx = [vx0] 
        self.tra_vy = [vy0] 
        self.tra_t = [0]
    def calculate(self):
        for i in range(1,self.N): 
            self.x=self.x + self.vx*self.dt
            self.y=self.y + self.vy*self.dt
            self.tra_x.append(self.x) 
            self.tra_y.append(self.y) 
            self.tra_vx.append(self.tra_vx[-1]) 
            self.tra_vy.append(self.tra_vy[-1])            
            if (np.sqrt(self.x**2+self.y**2)>1.0): 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2]) 
                self.tra_vx[-1],self.tra_vy[-1] = self.reflect(self.tra_x[-1],\
                self.tra_y[-1],self.tra_vx[-2], self.tra_vy[-2])
            self.x=self.tra_x[-1]
            self.y=self.tra_y[-1]
            self.vx=self.tra_vx[-1]
            self.vy=self.tra_vy[-1]
            self.t=self.t + self.dt
            self.tra_t.append(self.t)
        self.space_vx=[]
        self.space_x=[]
        for i in range(len(self.tra_x)): 
            if (abs(self.tra_y[i]-0)<0.001): 
                self.space_vx.append(self.tra_vx[i]) 
                self.space_x.append(self.tra_x[i]) 

        
    
    def previous_position(self,x,y,vx,vy):
        self.ddt=self.dt/100.0
        if(np.sqrt(x**2+y**2) < 1.0):
            x = x + vx*self.ddt 
            y = y + vy*self.ddt
        return x,y
    def reflect(self,x,y,vx,vy): 
        m=(vx*x+vy*y)/np.sqrt(x**2+y**2)  
        vx_r=vx-2.0*m*x/np.sqrt(x**2+y**2)
        vy_r=vy-2.0*m*y/np.sqrt(x**2+y**2)
        return vx_r,vy_r
        
    def plot(self): 
        plt.figure(figsize = (8,8)) 
        plt.xlabel('x') 
        plt.ylabel(r'$v_x$') 
        plt.title('Circular stadium -phase space plot') 
        plt.plot(self.space_x,self.space_vx,'r.') 
        plt.show() 
a=circularstadium_trajectory(0.2,0.2,1,2,100000,0.01) 
a.calculate() 
a.plot() 
