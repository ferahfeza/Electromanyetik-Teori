
from scipy.special import ellipk, ellipe, ellipkm1
from numpy import pi, sqrt, linspace
from pylab import plot, xlabel, ylabel, suptitle, legend, show
import math
import numpy 
import numpy as np
from scipy.stats import norm
from numpy import linalg
from ipywidgets import widgets
import plotly.express as px

m0 = 4E-7*pi
rho=1; #the ring has a radius of 1.0;
I = 1

P = [0.99,0,0] #the coordinate of point A
vectorP = np.array(P) 

B = [0,0,0] #initialize vector B
vectorB = np.array(B) 

#Number_of_L_Steps=50; #initialize discretization in the L direction
#dLv=Lv/Number_of_L_Steps;##vector of the diffential length
Number_of_Phi_Steps=50000; #initialize the Phi discretization
dPhi=(2*pi)/Number_of_Phi_Steps; #The step in the phi direction
for i in range(Number_of_Phi_Steps):

        Phi=0.5*dPhi+(i-1)*dPhi #Phi of current volume element
        dlength=rho*dPhi#length of current segment of the ring
        x2 = rho * math.cos(0.5*dPhi+(i+1)*dPhi)
        y2 = rho * math.sin(0.5*dPhi+(i+1)*dPhi)
        x1 = rho * math.cos(0.5*dPhi+(i)*dPhi)
        y1 = rho * math.sin(0.5*dPhi+(i)*dPhi)
        v11 = (x2 - x1) / dlength
        v22 = (y2 - y1) / dlength
        x=rho*math.cos(Phi); #x coordinate of current volume element
        y=rho*math.sin(Phi); #y coordinate of current volume element
        z=0; #z coordinate of current volume element
        C=[x, y, z]; #coordinate of volume element
        vectorC = np.array(C) 
        vectorR = vectorP - vectorC;#get distance from the current volume element to the
        # observation point
        RMag=linalg.norm(vectorR)
        R_Hat = vectorR / RMag
        V = [v11,v22,0]
        vectorV = np.array(V) 
        Is = I * vectorV
        #R = RMag * [v1 v2 v3];
        B=B+dlength*m0/(4*pi*RMag**2)*numpy.cross(Is,R_Hat); #get contribution to the elctric field
   
   

if abs(B[0])<1e-10: 
    B[0]=0; 

if abs(B[1])<1e-10:
    B[1]=0; 

if abs(B[2])<1e-10:
    B[2]=0; 

#print ("Br" "%10.3E" % B[0]) 
#print ("%10.3E" % B[1]) 
print ("Bz" "%10.3E" % B[2])

"""
Ban = m0 * I * rho**2 / 2 / (rho**2 + P[2]**2)**(1.5)
print("Ban:""%10.3E" % Ban)
"""


