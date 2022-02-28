import plotly.graph_objects as go
import math
import numpy as np
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
            rot=np.array([[1,0,0],[0,c(t),-s(t)],[0,s(t),c(t)]])
        if axis=='y':
            rot=np.array([[c(t),0,s(t)],[0,1,0],[-s(t),0,c(t)]])
        return np.around(rot@np.transpose(self.point),decimals=4)
    def visualize(self):
        #used to visualize files 
        fig=go.Figure()
        point_trace=go.Scatter3d(x=[0,self.x],y=[0,self.y],z=[0,self.z])
        fig.add_trace(point_trace)
        fig.show()
    def get_trace(self):
        return go.Scatter3d(x=[0,self.x],y=[0,self.y],z=[0,self.z])

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
    #origin=point(0,0,0)
    def __str__(self):
        return np.array_str(self.frame)
    def __repr__(self):
        return self.frame
    def __getitem__(self,argument):
        return self.frame[argument]
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
    def __init__(self,f=[[1,0,0],[0,1,0],[0,0,1]],origin=point(0,0,0)):
        if frm.isframematrix(f):
            self.frame=np.array(f)
            self.origin=origin
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
            rot=np.array[[1,0,0],[0,c(t),-s(t)],[0,s(t),c(t)]]
        if axis=='y':
            rot=np.array[[c(t),0,s(t)],[0,1,0],[-s(t),0,c(t)]]
        return np.around(rot@np.transpose(self.frame),decimals=4)
    def locate(self,point):
        #locate the value of the poin in the frame
        #returns the ouput vector in this frame
        pass
    def get_trace(self):
        o=self.origin
        f=self.frame
        ax1=go.Scatter3d(x=[o.x,f[0][0]],y=[o.y,f[0][1]],z=[o.z,f[0][2]])
        ax2=go.Scatter3d(x=[o.x,f[1][0]],y=[o.y,f[1][1]],z=[o.z,f[1][2]])
        ax3=go.Scatter3d(x=[o.x,f[2][0]],y=[o.y,f[2][1]],z=[o.z,f[2][2]])
        return [ax1,ax2,ax3]
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
    p=point(3,3,3)
    s=p.rotate('x',90)
    print(s)
    p.visualize()
    fig=go.Figure()
    fig.add_trace(p.get_trace())
    fig.show()
def testing_mm():
    f=frm(origin=point(2,2,2))
    fig=go.Figure(f.get_trace())
    #fig.add_trace(f.get_trace())
    fig.show()
if(__name__=='__main__'):
    #pointtest()
    testing_mm()
