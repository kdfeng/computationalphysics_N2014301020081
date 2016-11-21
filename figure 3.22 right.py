# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:19:36 2016

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
            
            if (np.sqrt( self.x**2+(self.y-0.01)**2 ) > 1.0) and self.y>0.01: 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position1\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2]) 
                self.tra_vx[-1],self.tra_vy[-1] = self.reflect1(self.tra_x[-1],\
                self.tra_y[-1],self.tra_vx[-2], self.tra_vy[-2]) 
            elif (np.sqrt( self.x**2+(self.y+0.01)**2 ) > 1.0) and self.y<-0.01: 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position2\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2]) 
                self.tra_vx[-1],self.tra_vy[-1] = self.reflect2(self.tra_x[-1],\
                self.tra_y[-1],self.tra_vx[-2], self.tra_vy[-2])
            elif (self.x < -1.0) and self.y>-0.01 and self.y<0.01: 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position3\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2]) 
                self.tra_vx[-1] = - self.tra_vx[-1]
            elif (self.x > 1.0) and self.y>-0.01 and self.y<0.01: 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position4\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2])
                self.tra_vx[-1] = - self.tra_vx[-1]
            self.x=self.tra_x[-1]
            self.y=self.tra_y[-1]
            self.vx=self.tra_vx[-1]
            self.vy=self.tra_vy[-1]
            self.t=self.t + self.dt
            self.tra_t.append(self.t) 
        
    
    def previous_position1(self,x,y,vx,vy):
        self.ddt=self.dt/100.0
        if(np.sqrt(x**2+(y-0.01)**2) < 1.0):
            x = x + vx*self.ddt 
            y = y + vy*self.ddt
        return x,y
    def previous_position2(self,x,y,vx,vy):
        self.ddt=self.dt/100.0
        if(np.sqrt(x**2+(y+0.01)**2) < 1.0):
            x = x + vx*self.ddt 
            y = y + vy*self.ddt
        return x,y
    def previous_position3(self,x,y,vx,vy):
        self.ddt=self.dt/100.0
        if(x>-1.0):
            x = x + vx*self.ddt 
            y = y + vy*self.ddt
        return x,y
    def previous_position4(self,x,y,vx,vy):
        self.ddt=self.dt/100.0
        if(x<1.0):
            x = x + vx*self.ddt 
            y = y + vy*self.ddt
        return x,y
    def reflect1(self,x,y,vx,vy): 
        m=(vx*x+vy*(y-0.01))/np.sqrt(x**2+(y-0.01)**2)  
        vx_r=vx-2.0*m*x/np.sqrt(x**2+(y-0.01)**2)
        vy_r=vy-2.0*m*(y-0.01)/np.sqrt(x**2+(y-0.01)**2)
        return vx_r,vy_r
    def reflect2(self,x,y,vx,vy): 
        m=(vx*x+vy*(y+0.01))/np.sqrt(x**2+(y+0.01)**2)  
        vx_r=vx-2.0*m*x/np.sqrt(x**2+(y+0.01)**2)
        vy_r=vy-2.0*m*(y+0.01)/np.sqrt(x**2+(y+0.01)**2)
        return vx_r,vy_r
        
    def plot(self): 
        plt.figure(figsize = (8,8)) 
        plt.xlim(-1,1) 
        plt.ylim(-1,1) 
        plt.xlabel('x') 
        plt.ylabel('y') 
        plt.title('Stadium billiard $\\alpha$=0.01') 
         
        plt.plot(self.tra_x,self.tra_y) 
        plt.show() 
a=circularstadium_trajectory(0,0,1,0.6,8000,0.01) 
a.calculate() 
a.plot() 
