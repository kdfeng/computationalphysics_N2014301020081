# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 18:18:09 2017

@author: john
"""

import matplotlib.pyplot as plt 
import numpy as np 
import random as rd 
class random_walks(): 
    def __init__(self):
        self.x=0
        self.r=0
        self.b=0
        self.t=[]
        self.x2ave = [0]*100
    def calculate(self):
        for j in  range(500):
            self.x=0
            for i in range(100):
                self.r=rd.random()
                if self.r<0.5:
                    self.x=self.x+1
                else:
                    self.x=self.x-1
                self.x2ave[i]=self.x2ave[i]+self.x**2
        self.x2ave=np.array(self.x2ave)/500   
        for k in range(100):
            self.t.append(k)
    def show(self):
        #plt.scatter(self.t,self.x2ave,s=4) 
        
        
        self.a=np.polyfit(self.t,self.x2ave,1)
        self.z=np.polyval(self.a,self.t)
        self.d=np.poly1d(self.a)
        print self.d
        plt.plot(self.t,self.x2ave,'r.',self.t,self.z,'b')
        plt.legend()
        plt.xlim(0,100)
        plt.ylim(0,100)
        
        plt.xlabel(r'step number(=time)') 
        plt.ylabel(r'<x2>') 
        
        plt.text(20,80,'<x2> versus time')
        plt.title('Random walk in one dimension')
        plt.text(60,self.x2ave[56],'%s' % self.d)
        plt.show()
A=random_walks()
A.calculate()
A.show()
