import plotly.graph_objects as go
from plotly.graph_objects import Figure
import numpy as np
class figure(Figure):
    def add_frame(self,frame):
        for i in frame.get_trace():
            self.add_trace(i)
class point3d:
    #A class used for 3d points
    def __repr__(self):
        return self.point
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.point=np.array([x,y,z])
    def __getitem__(self,key):
        return self.point[key]
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
        nmp=np.around(rot@np.transpose(self.point),decimals=4)
        return point3d(nmp[0],nmp[1],nmp[2])
    def visualize(self):
        #used to visualize files 
        fig=figure()
        point_trace=go.Scatter3d(x=[0,self.x],y=[0,self.y],z=[0,self.z])
        fig.add_trace(point_trace)
        fig.show()
    def get_trace(self,o=np.array([0,0,0])):
        return go.Scatter3d(x=[o[0],o[0]+self.x],y=[o[1],o[1]+self.y],z=[o[2],o[2]+self.z])

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
    '''def __repr__(self):
        return self.frame
        '''
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
    def __init__(self,f=[[1,0,0],[0,1,0],[0,0,1]],origin=point3d(0,0,0)):
        if isinstance(f,type(np.array([]))):
            if(f.shape==(3,3)):
                self.frame=f
                self.origin=origin
            else:
                raise Exception("not a 3*3 matrix")
        else:
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
        #print((np.around(rot@np.transpose(self.frame))).shape)
        return frm(np.transpose(np.around(rot@np.transpose(self.frame),decimals=4)))
    def locate(self,p):
        #locate the value of the poin in the frame
        #returns the ouput vector in this frame
        if not isinstance(p,point3d):
            raise Exception("locate requires argument instance of point p")
        #print(self.frame.shape)
        #print(type(p))
        return self.frame@np.transpose(p.point)
        
    def get_trace(self,origin=point3d(0,0,0)):
        o=origin
        #print(o)
        f=self.frame
        ax1=go.Scatter3d(x=[o[0],o[0]+f[0][0]],y=[o[1],o[1]+f[0][1]],z=[o[2],o[2]+f[0][2]])
        ax2=go.Scatter3d(x=[o[0],o[0]+f[1][0]],y=[o[1],o[1]+f[1][1]],z=[o[2],o[2]+f[1][2]])
        ax3=go.Scatter3d(x=[o[0],o[0]+f[2][0]],y=[o[1],o[1]+f[2][1]],z=[o[2],o[2]+f[2][2]])
        return [ax1,ax2,ax3]
    def visualize(self):
        fig=figure()
        fig.add_traces(self.get_trace())
        fig.add_traces(frm().get_trace())
        fig.show()
class joint:
    def __init__(self,link,endframe,axis):
        if not isinstance(link,point3d):
            raise Exception("pass points in point format")
        if not isinstance(endframe,type(frm())):
            raise Exception("pass frame in frm format")
        self.link=link
        self.endframe=endframe
        self.axis=axis
    def set_angle(self,theta):
         new_link=self.link.rotate(self.axis,theta)
         new_endframe=self.endframe.rotate(self.axis,theta)
         return joint(new_link,new_endframe,self.axis)
    def visualize(self):
        f=frm()
        fig=figure()
        fig.add_traces(f.get_trace())
        fig.add_traces(self.link.get_trace())
        fig.add_traces(self.endframe.get_trace(self.link))
        fig.show()
    def get_trace(self,origin=point3d(0,0,0)):
        print("inside joint self.link.gert_trace",[self.link.get_trace(origin)])
        print("self.link.point:",self.link.point)
        print(origin.point)
        return([self.link.get_trace(origin)]+self.endframe.get_trace(origin.point+self.link.point))
class arm:
    def __init__(self,joints):
        if not isinstance(joints,list):
            raise Exception("Enter joints in list formats")
        self.joints=joints
        self.current_joints=joints
        self.angles=[0]*len(joints)
        self.length=len(self.angles)
    def visualize(self):
        fig=figure()
        print(self.current_joints[0].get_trace())
        fig.add_traces(self.current_joints[0].get_trace())
        for i in range(1,len(self.joints)):
            temp=self.current_joints[i].get_trace(self.current_joints[i-1].link)
            fig.add_traces(temp)
        fig.show()
    def set_angles(self,angles):
        self.angles=angles[:]
        for i in range(self.length):
            self.current_joints[i]=self.joints[i].set_angle(angles[i])
            
        
        
def frmtest():
    s=frm([[0,0,2],[4,0,4],[6,6,6]])
    print(s.frame)
    #s.unitize()
    print(s.unitize())
    print(s.rotate('z',50))
    print(s)
def pointtest():
    p=point3d(3,3,3)
    #s=p.rotate('x',90)
    #print(s)
    p.visualize()
    fig=figure()
    fig.add_trace(p.get_trace([1,1,1]))
    fig.show()
def testing_mm():
    f=frm(origin=point3d(2,2,2))
    fig=figure(f.get_trace())
    #fig.add_trace(f.get_trace())
    fig.show()
def testing_locate():
    p=point3d(1,1,1)
    f=frm()
    f1=f.rotate('y',90)
    print(f.locate(p))
    print(f1.locate(p))
def testing_frame_rotation():
    flag=True
    f=frm()
    f1=frm()
    while(flag):
        print('1 to change frame')
        print('q to quit ')
        temp=input('enter values to chage frame :').split()
        if(len(temp)==1):
            if(temp[0]==1):
                pass
            elif(temp[0]=='q'):
                flag=False
            else:
                print('enter correctly')
        elif(len(temp)==2):
            axis=temp[0]
            theta=int(temp[1])
            f1=f.rotate(axis,theta)
            fig=figure()
            fig.add_traces(f.get_trace())
            fig.add_traces(f1.get_trace())
            fig.show()
        else:
            print('enter correct values')
def testing_joint():
    j=joint(point3d(1,1,1),frm(),'x')
    j.visualize()
    j1=j.set_angle(90)
    j1.visualize()
def frm_test():
    n=frm([[1.,0.,0.],[ 0.,0.7071,0.7071],[ 0.,-0.7071,0.7071]])
    n.visualize()
def arm_test1():
    j1=joint(point3d(0,0,0),frm(),'x')
    j2=joint(point3d(1,1,1),frm(),'y')
    j3=joint(point3d(-1,1,0),frm(),'z')
    a=arm([j1,j2,j3])
    a.visualize()
def arm_test2():
    j1=joint(point3d(0,0,0),frm(),'x')
    j2=joint(point3d(1,1,1),frm(),'x')
    j3=joint(point3d(1,1,1),frm(),'x')
    a=arm([j1,j2,j3])
    #a.visualize()
    a.set_angles([90,0,0])
    a.visualize()
    
    
        
if(__name__=='__main__'):
    #pointtest()
    #testing_mm()
    #testing_locate()
    #testing_frame_rotation()
    #testing_joint()
    #frm_test()
    #arm_test1()
    arm_test2()
