# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 20:20:44 2017

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
        for i in range(100):
            self.r=rd.random()
            if self.r<0.5:
                self.x=self.x+1
            else:
                self.x=self.x-1
            self.x2ave[i]=self.x2ave[i]+self.x
         
         
            self.t.append(i)
    def show(self):
        #plt.scatter(self.t,self.x2ave,s=4) 
        
        
        #self.a=np.polyfit(self.t,self.x2ave,1)
        #self.z=np.polyval(self.a,self.t);
        plt.plot(self.t,self.x2ave,'o')
        plt.legend()
        plt.xlim(0,100)
        #plt.ylim(0,100)
        
        plt.xlabel(r'step number(=time)') 
        plt.ylabel(r'x') 
       
        #plt.text(20,80,'<x2> versus time')
        plt.title('Random walk in one dimension')
        plt.show()
A=random_walks()
A.calculate()
A.show()
