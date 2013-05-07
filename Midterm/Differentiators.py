import numpy as np

def finiteDifference(x,y):
    """This will differentiate a function by using the center average
    carefull to make sure arrays are same size for x and y."""    
    
    dydx = np.zeros(y.shape,float) # we know it will be this size
    dydx[1:-1] = (y[2:]-y[:-2])/(x[2:]-x[:-2]) #center difference, works for most
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2]) #backward difference because it added the tail to the data
    return dydx



def fourPtFiniteDiff(x,y):
    '''Returns the numerical derivative of y with respect to x using
    the four-point center differencing method. Inputs x and y are arrays.
    More accurate than the center difference method!'''
    dydx1 = np.zeros(y.shape, float)
    
    dydx1[2:-2] = (y[0:-4]-8*y[1:-3]+8*y[3:-1]-y[4:])/(x[:-4]-8*x[1:-3]+8*x[3:-1]-x[4:])
    dydx1[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx1[1] = (y[2]-y[1])/(x[2]-x[1])
    dydx1[-2] = (y[-2]-y[-3])/(x[-2]-x[-3])
    dydx1[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx1
    
    
