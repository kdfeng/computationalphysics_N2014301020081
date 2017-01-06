# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 12:13:46 2017

@author: john
"""

import matplotlib.pyplot as plt 
import numpy as np 
import random as rd 
class random_walks(): 
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        self.rad1=0
        self.rad2=0
        self.b=0
        self.r=1
        self.t=[]
        self.r2ave = [0]*100
    def calculate(self):
        for j in  range(500):
            self.x=0
            self.y=0
            self.z=0
            for i in range(99):
                self.rad1=rd.uniform(0, np.pi)
                self.rad2=rd.uniform(0, 2*np.pi)
                #self.r=rd.uniform(0, 10)
                self.x=self.x+self.r*np.cos(self.rad2)*np.sin(self.rad1)
                self.y=self.y+self.r*np.sin(self.rad2)*np.sin(self.rad1)
                self.z=self.z+self.r*np.cos(self.rad1)
                self.r2ave[i+1]=self.r2ave[i+1]+self.x**2+self.y**2+self.z**2
        self.r2ave=np.array(self.r2ave)/500   
        for k in range(100):
            self.t.append(k)
    def show(self):
        self.a=np.polyfit(self.t,self.r2ave,1)
        self.z=np.polyval(self.a,self.t)
        self.d=np.poly1d(self.a)
        print self.d
        plt.plot(self.t,self.r2ave,'r.',self.t,self.z,'b')
        #plt.plot(self.t,self.r2ave,'r.')
        plt.legend()
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.xlabel(r'step number(=time)') 
        plt.ylabel(r'<r2>') 
        plt.text(5,80,'<r2> versus time(made of spherical coordinates)')
        plt.title('Random walk in random directions of unit length in there dimensions')
        plt.text(60,self.r2ave[56],'%s' % self.d)
        #plt.text(10,3000,'r=random(0, 10)')
        plt.show()
A=random_walks()
A.calculate()
A.show()
