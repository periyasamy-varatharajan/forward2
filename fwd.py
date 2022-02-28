import plotly.graph_objects as go
import math
import numpy as np
'''
 class called joint for joinst
 it contains method for joints and using them
'''
class frm:
    '''
        output frame
        it is the class for frame
        it should provide funtions for rotation and end effectors
      '''
    def __str__(self):
        return np.array_str(self.frame)
    def __repr__(self):
        return self.frame
    def isframematrix(a):
        flag=True
        if type(a)==type([]):
            if len(a)==3:
                for i in a:
                    if len(i)==3:
                        for j in i:
                            if(type(j)==type(1) or type(j)==type(1.0)):
                                pass
                            else:
                                flag=False
                                print('not int or float')
                    else:
                            flag=False
                            print('size of sub vector is small')
            else:
                        flag=False
                        print('not enough size')
        else:
                    flag=False
                    print('not a list')
        return flag
    def __init__(self,f=[[1,0,0],[0,1,0],[0,0,1]]):
        if frm.isframematrix(f):
            self.frame=np.array(f)
        else:
            raise Exception("not a square matrix")
    def minimum(self):
        #finds the minimum value and not zero
        #and returns it
        mi=None
        for i in range(3):
            for j in range(3):
                temp=self.frame[i][j]
                if temp: #checks the current value is zero
                    if mi: #checks the mi is value
                        if(mi>temp):
                            mi=temp
                    else:
                        mi=temp
        return mi
    '''
    def divide(self,d):
        #it divides the all values of frame by d
        temp=self.frame
        for i in range(3):
            for j in range(3):
                temp[i][j]=self.frame[i][j]/d
    '''
    def unitize(self):
        #makes the frame into unit vector frame
        mi=self.minimum()
        return self.frame/mi
        '''
    def frmmul(x):
        #mat mul is used to multiply rotational matrix to matmul
        temp=self.frame
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    temp[i][j]+=x[i][k]*self.frame[k][j]
        if ismatrix(x):
            pass
            '''
        
    def rotate(self,theta,axis):
        axises=['x','y','z']
        t=np.deg2rad(theta)
        c=np.cos
        s=np.sin
        if axis not in axises:
            raise Exception('enter axis correctly either x,y,z')
        if axis=='z':
            rot=np.array([[c(t),-s(t),0],[s(t),c(t),0],[0,0,1]])
        if axis=='x':
            rot=[[1,0,0],[0,c(t),-s(t)],[0,s(t),c(t)]]
        if axis=='y':
            rot=[[c(t),0,s(t)],[0,1,0],[-s(t),0,c(t)]]
        return np.trunc(rot@np.transpose(self.frame))
    def locate(self,point):
        #locate the value of the poin in the frame
        #returns the ouput vector in this frame
        pass
    
class point:
    #A class used for 3d points
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.point=np.array([x,y,z])
    def rotate(self,axis,theta):
        axises=['x','y','z']
        t=np.deg2rad(theta)
        c=np.cos
        s=np.sin
        if axis not in axises:
            raise Exception('enter axis correctly either x,y,z')
        if axis=='z':
            rot=np.array([[c(t),-s(t),0],[s(t),c(t),0],[0,0,1]])
        if axis=='x':
            rot=[[1,0,0],[0,c(t),-s(t)],[0,s(t),c(t)]]
        if axis=='y':
            rot=[[c(t),0,s(t)],[0,1,0],[-s(t),0,c(t)]]
        return np.trunc(rot@np.transpose(self.point))
        
        
        
class joint:
    def __init__(*arg):
        end=arg[0]
        axis=arg[2]
        typ=arg[3]
        
class arm:
    def __init__():
        pass
def frmtest():
    s=frm([[0,0,2],[4,0,4],[6,6,6]])
    print(s.frame)
    #s.unitize()
    print(s.unitize())
    print(s.rotate(50,'z'))
    print(s)
def pointtest():
    p=point(3,3,0)
    s=p.rotate('x',90)
    print(s)
if(__name__=='__main__'):
    pointtest()
