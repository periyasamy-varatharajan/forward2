import plotly.graph_objects as go
import math
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
            self.frame=f
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
    def divide(self,d):
        #it divides the all values of frame by d 
        for i in range(3):
            for j in range(3):
                self.frame[i][j]=self.frame[i][j]/d
    def unitize(self):
        #makes the frame into unit vector frame
        mi=self.minimum()
        self.divide(mi)
    def matmul(x):
        #mat mul is used to multiply rotational matrix to matmul
        if ismatrix(x):
            pass
    def rotate(self,theta,axis):
        axises=['x','y','z']
        if axis not in axises:
            raise Exception('enter axis correctly either x,y,z')
        #rot=[[],[],[]]
        if axis=='x':
            pass
        if axis=='y':
            pass
        if axis=='z':
            pass
        
class joint:
    def __init__(*arg):
        end=arg[0]
        axis=arg[2]
        typ=arg[3]
        
class arm:
    def __init__():
        pass
    
if(__name__=='__main__'):
    s=frm([[0,0,2],[4,0,4],[6,6,6]])
    print(s.frame)
    s.unitize()
    print(s.frame)
    s.rotate(50,'x')
