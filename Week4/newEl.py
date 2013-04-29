from math import sqrt
import numpy as np

def pointPotential(x,y,q1,posx,posy):
	"""defining constants and finds potential using distance to particle for a positive e"""       
	k=8.98e9; q1=1.6e-19                         
        PointP = (k*q)/np.sqrt((x-posx)**2+(y-posy)**2)
        return PointP


def dipolePotential(x,y,qd, d):
    """finds the potential between two charges"""
    k=8.98e9; qd = int()                          
    Vdipole = (k*q1/np.sqrt(x**2+(y-(d/2))**2)) - (k*q1/np.sqrt(x**2+(y+(d/2))**2)) 
    return Vdipole                                                           
