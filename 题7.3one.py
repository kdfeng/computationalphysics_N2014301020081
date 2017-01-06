# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 21:39:24 2017

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
        self.x2ave = [0]*1000
    def calculate(self):
        for j in  range(500):
            self.x=0
            for i in range(1000):
                self.r=rd.random()
                if self.r<0.75:
                    self.x=self.x+1
                else:
                    self.x=self.x-1
                self.x2ave[i]=self.x2ave[i]+self.x**2
        self.x2ave=np.log(np.array(self.x2ave)/500)   
        for k in range(1000):
            self.t.append(k)
        self.t=np.log(np.array(self.t))
        self.t=list(self.t)#array-list#
        self.x2ave=list(self.x2ave)#array-list?# 
        del self.x2ave[0]
        del self.t[0]
        
    def show(self):
        self.a=np.polyfit(self.t,self.x2ave,1)
        self.z=np.polyval(self.a,self.t)
        plt.loglog(np.e**np.array(self.t),np.e**np.array(self.x2ave),'r.',np.e**np.array\
        (self.t),np.e**np.array(self.z),'b')
        plt.legend()
        self.d=np.poly1d(self.a)
        print self.d
        
        
       
        
        plt.xlabel(r'step number(=time)') 
        plt.ylabel(r'<x2>') 
        
        plt.text(2,10**5,'<x2> versus time')
        plt.title('Random walk in one dimension   Pleft=0.25,Pright=0.75')
        plt.text(100,1000,'%s' % self.d)
        plt.show()
A=random_walks()
A.calculate()
A.show()
