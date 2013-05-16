from math import sqrt
import numpy as np

def pointPotential(x,y,q,posx,posy):
	"""defining constants and finds potential using distance to particle for a positive e"""       
	k=8.98e9; q = 1.6e-19                       
        PointP = (k*q/np.sqrt((x-posx)**2+(y-posy)**2))
        return PointP


def dipolePotential(x,y,q,d):
    """finds the potential between two charges"""
    k=8.98e9                       
    Vdipole = (k*q/np.sqrt(y**2+(x-(d/2))**2)) - (k*q/np.sqrt(y**2+(x+(d/2))**2)) 
    return Vdipole                                                           
