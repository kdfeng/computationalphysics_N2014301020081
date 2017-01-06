# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 23:04:39 2017

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
        self.r=0
        self.b=0
        self.t=[]
        self.x2 = 0
        self.y2 = 0
        self.z2 = 0
        
    def calculate1(self):
        self.r2ave=[0]*100
        for j in  range(500):
            self.x=0
            self.y=0
            self.z=0
            
            for i in range(99):
                self.r=rd.random()
                if self.r<2.0/6:
                    if self.r>=1.0/6:
                        self.x=self.x+1
                    else:
                        self.x=self.x-1
                    
                elif 4.0/6>self.r>=2.0/6:
                    if 4.0/6>self.r>=3.0/6:
                        self.y=self.y+1
                    else:
                        self.y=self.y-1
                    
                else: 
                    if self.r>=5.0/6:
                        self.z=self.z+1
                    else:
                        self.z=self.z-1
                self.r2ave[i+1]=self.r2ave[i+1]+self.x**2+self.y**2+self.z**2
        self.r2ave=np.array(self.r2ave)/500
        for k in range(100):
            self.t.append(k)
         
            
    def show1(self):
        self.a=np.polyfit(self.t,self.r2ave,1)
        self.z=np.polyval(self.a,self.t)
        self.d=np.poly1d(self.a)
        #print self.d
        plt.subplot(221)
        plt.plot(self.t,self.r2ave,'r.',self.t,self.z,'b')
        plt.legend()
        #plt.xlabel(r'step number(=time)') 
        plt.ylabel(r'<r2>')
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.text(20,80,'<r2> versus time')
        plt.title(' simple-cubic lattice there-dimensions')
        plt.text(40,self.r2ave[50],'%s' % self.d)
        plt.show()
    def calculate2(self):
        self.r2ave=[0]*1000
        for j in  range(500):
            self.x=0
            self.y=0
            self.z=0
            
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
                self.r2ave[i+1]=self.r2ave[i+1]+self.x**2+self.y**2+self.z**2      
        self.r2ave=np.log(np.array(self.r2ave)/500)
        for k in range(1000):
            self.t.append(k)
        self.t=np.log(np.array(self.t))
        self.t=list(self.t)#array-list#
        self.r2ave=list(self.r2ave)#array-list?# 
        del self.r2ave[0]
        del self.t[0]
         
            
    def show2(self):
        self.a=np.polyfit(self.t,self.r2ave,1)
        self.z=np.polyval(self.a,self.t)
        plt.subplot(222)
        plt.loglog(np.e**np.array(self.t),np.e**np.array(self.r2ave),'r.',np.e**np.array\
        (self.t),np.e**np.array(self.z),'b')
        plt.legend()
        self.d=np.poly1d(self.a)
        print self.d
        plt.legend()
        plt.xlabel(r'step number(=time)') 
        plt.ylabel(r'<r2>')
        #plt.xlim(0,100)
        plt.ylim(0,10**5)
        plt.text(10,10**4,'<r2> versus time')
        plt.title(' face-centered cubic lattice')
        plt.text(10,100,'%s' % self.d)
        plt.show()
    def calculate3(self):
        self.r2ave=[0]*1000
        for j in  range(500):
            self.x=0
            self.y=0
            self.z=0
            
            for i in range(999):
                self.r=rd.random()
                if self.r<2.0/14:
                    if self.r>=1.0/14:
                        self.x=self.x+1
                    else:
                        self.x=self.x-1
                    
                elif 4.0/14>self.r>=2.0/14:
                    if self.r>=3.0/14:
                        self.y=self.y+1
                    else:
                        self.y=self.y-1
                    
                elif 6.0/14>self.r>=4.0/14: 
                    if self.r>=5.0/14:
                        self.z=self.z+1
                    else:
                        self.z=self.z-1
                    
                elif 10.0/14>self.r>=6.0/14:
                    self.x=self.x+0.5
                    if self>=8.0/14:
                        self.y=self.y+0.5
                        if self>=9.0/14:
                            self.z=self.z+0.5
                        else:
                            self.z=self.z-0.5      
                    else:
                        self.y=self.y-0.5
                        if self>=7.0/14:
                            self.z=self.z+0.5
                        else:
                            self.z=self.z-0.5
                else:
                    self.x=self.x-0.5
                    if self>=12.0/14:
                        self.y=self.y+0.5
                        if self>=13.0/14:
                            self.z=self.z+0.5
                        else:
                            self.z=self.z-0.5      
                    else:
                        self.y=self.y-0.5
                        if self>=11.0/14:
                            self.z=self.z+0.5
                        else:
                            self.z=self.z-0.5
                self.r2ave[i+1]=self.r2ave[i+1]+self.x**2+self.y**2+self.z**2      
        self.r2ave=np.log(np.array(self.r2ave)/500)
        for k in range(1000):
            self.t.append(k)
        self.t=np.log(np.array(self.t))
        self.t=list(self.t)#array-list#
        self.r2ave=list(self.r2ave)#array-list?# 
        del self.r2ave[0]
        del self.t[0]
         
            
    def show3(self):
        self.a=np.polyfit(self.t,self.r2ave,1)
        self.z=np.polyval(self.a,self.t)
        plt.subplot(223)
        plt.loglog(np.e**np.array(self.t),np.e**np.array(self.r2ave),'r.',np.e**np.array\
        (self.t),np.e**np.array(self.z),'b')
        plt.legend()
        self.d=np.poly1d(self.a)
        print self.d
        plt.legend()
        plt.xlabel(r'step number(=time)') 
        plt.ylabel(r'<r2>')
        #plt.xlim(0,100)
        plt.ylim(0,10**5)
        plt.text(10,10**4,'<r2> versus time')
        plt.title('body-centered cubic lattice')
        plt.text(10,100,'%s' % self.d)
        plt.show()
A=random_walks()
A.calculate1()
A.show1()
B=random_walks()
B.calculate2()
B.show2()
C=random_walks()
C.calculate3()
C.show3()
