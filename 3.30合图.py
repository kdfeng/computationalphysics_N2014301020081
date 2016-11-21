# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:28:58 2016

@author: john
"""
import matplotlib.pyplot as plt 
import numpy as np 
class circularstadium_trajectory(): 
    def __init__(self,x0,y0,vx0,vy0,N,dt,a): 
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
        self.a=a
    def calculate(self):
        
        for i in range(1,self.N): 
            self.x=self.x + self.vx*self.dt
            self.y=self.y + self.vy*self.dt
            self.tra_x.append(self.x) 
            self.tra_y.append(self.y) 
            self.tra_vx.append(self.tra_vx[-1]) 
            self.tra_vy.append(self.tra_vy[-1])            
            
            if (np.sqrt( self.x**2+(self.y-self.a)**2 ) > 1.0) and self.y>self.a: 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position1\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2]) 
                self.tra_vx[-1],self.tra_vy[-1] = self.reflect1(self.tra_x[-1],\
                self.tra_y[-1],self.tra_vx[-2], self.tra_vy[-2]) 
            elif (np.sqrt( self.x**2+(self.y+self.a)**2 ) > 1.0) and self.y<-self.a: 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position2\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2]) 
                self.tra_vx[-1],self.tra_vy[-1] = self.reflect2(self.tra_x[-1],\
                self.tra_y[-1],self.tra_vx[-2], self.tra_vy[-2])
            elif (self.x < -1.0) and self.y>-self.a and self.y<self.a: 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position3\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2]) 
                self.tra_vx[-1] = - self.tra_vx[-1]
            elif (self.x > 1.0) and self.y>-self.a and self.y<self.a: 
                self.tra_x[-1],self.tra_y[-1] = self.previous_position4\
                (self.tra_x[-2], self.tra_y[-2], self.tra_vx[-2], self.tra_vy[-2])
                self.tra_vx[-1] = - self.tra_vx[-1]
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
        return self.tra_x, self.tra_y, self.tra_t
    def previous_position1(self,x,y,vx,vy):
        self.ddt=self.dt/100.0
        if(np.sqrt(x**2+(y-self.a)**2) < 1.0):
            x = x + vx*self.ddt 
            y = y + vy*self.ddt
        return x,y
    def previous_position2(self,x,y,vx,vy):
        self.ddt=self.dt/100.0
        if(np.sqrt(x**2+(y+self.a)**2) < 1.0):
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
        m=(vx*x+vy*(y-self.a))/np.sqrt(x**2+(y-self.a)**2)  
        vx_r=vx-2.0*m*x/np.sqrt(x**2+(y-0.01)**2)
        vy_r=vy-2.0*m*(y-self.a)/np.sqrt(x**2+(y-self.a)**2)
        return vx_r,vy_r
    def reflect2(self,x,y,vx,vy): 
        m=(vx*x+vy*(y+self.a))/np.sqrt(x**2+(y+self.a)**2)  
        vx_r=vx-2.0*m*x/np.sqrt(x**2+(y+0.01)**2)
        vy_r=vy-2.0*m*(y+self.a)/np.sqrt(x**2+(y+self.a)**2)
        return vx_r,vy_r
    
sub1=plt.subplot(221) 
a=circularstadium_trajectory(0,0,1,0.6,8000,0.01,0.1) 
x1,y1,t1=a.calculate() 
b=circularstadium_trajectory(0.00001,0,1,0.6,8000,0.01,0.1) 
x2,y2,t2=b.calculate()  
for i in range(len(x1)): 
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2) 
sub1.semilogy(t1,x1) 
sub1.title('Stadium with $\\alpha$=0.1 - divergence of two trajectories') 
plt.xlabel('time') 
plt.ylabel('separation')

sub2=plt.subplot(222) 
a=circularstadium_trajectory(0,0,1,0.6,8000,0.01,0.05) 
x1,y1,t1=a.calculate() 
b=circularstadium_trajectory(0.00001,0,1,0.6,8000,0.01,0.05) 
x2,y2,t2=b.calculate()  
for i in range(len(x1)): 
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2) 
sub2.semilogy(t1,x1) 
sub2.title('Stadium with $\\alpha$=0.05 - divergence of two trajectories') 
plt.xlabel('time') 
plt.ylabel('separation')
 
sub3=plt.subplot(223) 
a=circularstadium_trajectory(0,0,1,0.6,8000,0.01,0.01,0.01) 
x1,y1,t1=a.calculate() 
b=circularstadium_trajectory(0.00001,0,1,0.6,8000,0.01,0.01) 
x2,y2,t2=b.calculate()  
for i in range(len(x1)): 
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2) 
sub3.semilogy(t1,x1) 
sub3.title('Stadium with $\\alpha$=0.01 - divergence of two trajectories') 
plt.xlabel('time') 
plt.ylabel('separation')

sub4=plt.subplot(224) 
a=circularstadium_trajectory(0,0,1,0.6,8000,0.01,0.001) 
x1,y1,t1=a.calculate() 
b=circularstadium_trajectory(0.00001,0,1,0.6,8000,0.01,0.001) 
x2,y2,t2=b.calculate()  
for i in range(len(x1)): 
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2) 
sub4.semilogy(t1,x1) 
sub4.title('Stadium with $\\alpha$=0.001 - divergence of two trajectories') 
plt.xlabel('time') 
plt.ylabel('separation')
