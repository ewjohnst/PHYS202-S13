import numpy as np


def finiteDifference(x,y):
    """Returns the derivative of y with respect to x"""
    #dy = diff(y) #y(n+1)-y(n)
    #dx = diff(x)
    #dydx = dy/dx these three aren't necessary but set up our derivative concept
    dydx2 = zeros(y.shape,float) # we know it will be this size
    dydx2[1:-1] = (y[2:]-y[:-2])/(x[2:]-x[:-2]) #center difference
    dydx2[-1] = (y[-1]-y[-2])/(x[-1]-x[-2]) #backward difference because it added the tail to the data
    dydx2[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference, not really needed here
    return dydx2

def fourPtFiniteDiff(x,y):
    "Returns the numerical derivative of y with respect to x using the four-point center differencing method. Inputs x and y are arrays\"\"\"\n",
    dydx3 = zeros(y.shape, float)
    dydx3[2:-2] = (y[0:-4]-8*y[1:-3]+8*y[3:-1]-y[4:])/(x[:-4]-8*x[1:-3]+8*x[3:-1]-x[4:])
    dydx3[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx3[1] = (y[2]-y[1])/(x[2]-x[1])
    dydx3[-2] = (y[-2]-y[-3])/(x[-2]-x[-3])
    dydx3[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx3