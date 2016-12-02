# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 15:46:50 2016

@author: john
"""

import matplotlib.pyplot as plt 
import numpy as np 
class Hyperion(): 
    def __init__(self,e,a,init_rad,y0=0,vx0=0,dt=0.0001): 
        self.e=e
        self.a=a
        self.x = e*a+a 
        self.y = y0 
        self.vx =vx0
        self.vy = np.sqrt(4*(np.pi**2)*(1-self.e)/(self.a*(1+self.e)))
        self.rad=init_rad
        self.w=0
        self.t=0
        self.tra_x = [a+e*a] 
        self.tra_y = [y0]
        self.tra_rad=[init_rad]
        self.tra_w=[0]
        self.tra_t=[0]
        self.dt=dt
    def calculate(self):
        for i in  range(120000):
           self.r=np.sqrt(self.x**2+self.y**2)
           self.vx=self.vx-4*np.pi**2*self.x*self.dt/self.r**3
           self.vy=self.vy-4*np.pi**2*self.y*self.dt/self.r**3
           self.x=self.x+self.vx*self.dt
           self.y=self.y+self.vy*self.dt 
           self.w=self.w-3*4*(np.pi**2)*(self.x*np.sin(self.rad)-self.y*np.cos(self.rad))*\
           (self.x*np.cos(self.rad)+self.y*np.sin(self.rad))*self.dt/self.r**5
           self.rad=self.rad+self.w*self.dt
           if self.rad>np.pi:
                self.rad=self.rad-2*np.pi
           elif self.rad<-np.pi:
                self.rad=self.rad+2*np.pi
           self.tra_w.append(self.w) 
           self.tra_rad.append(self.rad)
           
           #self.tra_x.append(self.x) 
           #self.tra_y.append(self.y)
           self.t=self.t+self.dt
           self.tra_t.append(self.t)
        return self.tra_rad, self.tra_w, self.tra_t

sub1=plt.subplot(221)
a=Hyperion(0.34,1,0) 
x1,y1,t1=a.calculate() 
b=Hyperion(0.34,1,0.01) 
x2,y2,t2=b.calculate()  
for i in range(len(t1)): 
    x1[i]=np.abs(x2[i]-x1[i])
sub1.semilogy(t1,x1)
sub1.text(0.1,2,'Elliptical orbit: e=0.34')
sub1.set_title('Hyperion $ \Delta\ theta $ versus time  ') 
plt.xlabel('time(yr)') 
plt.ylabel('$\Delta\theta $(radians) ')
plt.show()

sub2=plt.subplot(222)
a=Hyperion(0.36,1,0) 
x1,y1,t1=a.calculate() 
b=Hyperion(0.36,1,0.01) 
x2,y2,t2=b.calculate()  
for i in range(len(t1)): 
    x1[i]=np.abs(x2[i]-x1[i])
sub2.semilogy(t1,x1)
sub2.set_title('Hyperion $ \Delta\ theta $ versus time  ')
sub2.text(0.1,2,'Elliptical orbit: e=0.36') 
plt.xlabel('time(yr)') 

plt.show()

sub3=plt.subplot(223)
a=Hyperion(0.38,1,0) 
x1,y1,t1=a.calculate() 
b=Hyperion(0.38,1,0.01) 
x2,y2,t2=b.calculate()  
for i in range(len(t1)): 
    x1[i]=np.abs(x2[i]-x1[i])
sub3.semilogy(t1,x1)
sub3.text(0.1,2,'Elliptical orbit: e=0.38') 
plt.xlabel('time(yr)')
plt.ylabel('$\Delta\theta $(radians) ') 
plt.show()

sub4=plt.subplot(224)
a=Hyperion(0.4,1,0) 
x1,y1,t1=a.calculate() 
b=Hyperion(0.4,1,0.01) 
x2,y2,t2=b.calculate()  
for i in range(len(t1)): 
    x1[i]=np.abs(x2[i]-x1[i])
sub4.semilogy(t1,x1)
sub4.text(0.1,2,'Elliptical orbit: e=0.4') 
plt.xlabel('time(yr)') 

plt.show()

