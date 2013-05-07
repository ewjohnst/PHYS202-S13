import numpy as np
import numpy as numpy

def finiteDifference(x,y):
    """This will differentiate a function by using the center average
    carefull to make sure arrays are same size for x and y."""    

    
    dydx = zeros(y.shape,float) # we know it will be this size
    dydx[1:-1] = (y[2:]-y[:-2])/(x[2:]-x[:-2]) #center difference, works for most
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2]) #backward difference because it added the tail to the data
    return dydx




def fourPtFiniteDiff(x,y):
    """This code will do a 4-point differentiation which is more
    accurate than the center difference method, still need to use
    the forward and backward differenes to get the ends though."""
    
    dydx = zeros(y.shape,float)

    #for the start and end use forward and backward difference
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2]) #backward difference

    #for middle, use formula given in the notes
    for i, m in enumerate(y[2:-2]):
        i+=2 #this is done because we're starting at 2, not zero
        dydx[i] = (y[i-2] - 8*y[i-1] + 8*y[i+1] - y[i+2]) / (12 * (x[i+1] - x[i]))
    return dydx

    
    
