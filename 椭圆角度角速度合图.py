# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 17:27:00 2016

@author: john
"""

import matplotlib.pyplot as plt 
import numpy as np 
class Hyperion(): 
    def __init__(self,e,a,y0=0,vx0=0,dt=0.0001): 
        self.e=e
        self.a=a
        self.x = e*a+a 
        self.y = y0 
        self.vx =vx0
        self.vy = np.sqrt(4*np.pi**2*(1-self.e)/(self.a*(1+self.e)))
        self.rad=0
        self.w=0
        self.t=0
        self.tra_x = [a+e*a] 
        self.tra_y = [y0]
        self.tra_rad=[0]
        self.tra_w=[0]
        self.tra_t=[0]
        self.dt=dt
    def calculate(self):
        for i in  range(100000):
           self.r=np.sqrt(self.x**2+self.y**2)
           self.vx=self.vx-4*np.pi**2*self.x*self.dt/self.r**3
           self.vy=self.vy-4*np.pi**2*self.y*self.dt/self.r**3
           self.x=self.x+self.vx*self.dt
           self.y=self.y+self.vy*self.dt 
           self.w=self.w-3*4*np.pi**2*(self.x*np.sin(self.rad)-self.y*np.cos(self.rad))*\
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
        return self.tra_rad,self.tra_w,self.tra_t
  
sub1=plt.subplot(221)
A=Hyperion(0.36,1)
x,y,t=A.calculate()
sub1.plot(t,x)
plt.xlabel('time(yr)') 
plt.ylabel('$ \ theta $(radians) ')
plt.text(1,3.5,'Elliptical orbit e=0.36')
sub1.set_title('Hyperion $ \ theta $ versus time  ')
plt.show()

sub2=plt.subplot(222)
A=Hyperion(0.36,1)
x,y,t=A.calculate()
sub2.plot(t,y)
plt.xlabel('time(yr)') 
plt.ylabel('$\omega$(radians/yr)')
plt.text(1,22.5,'Elliptical orbit e=0.36')
sub2.set_title('Hyperion $\omega$ versus time  ')
plt.show()

sub3=plt.subplot(223)
A=Hyperion(0.38,1)
x,y,t=A.calculate()
sub3.plot(t,x)
plt.xlabel('time(yr)') 
plt.ylabel('$ \ theta $(radians) ')
plt.text(1,3.5,'Elliptical orbit e=0.38')
plt.show()

sub4=plt.subplot(224)
A=Hyperion(0.38,1)
x,y,t=A.calculate()
sub4.plot(t,y)
plt.xlabel('time(yr)') 
plt.ylabel('$\omega$(radians/yr)')
plt.text(1,37.5,'Elliptical orbit e=0.38')
plt.show()

