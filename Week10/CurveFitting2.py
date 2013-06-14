import numpy as np

def LinearLeastSquaresFit(x,y):
    """Take in arrays representing (x,y) values for a set of linearly varying data
    and perform a linear least squares regression. Returns the resulting slope and
    intercept parameters of the best fit line with their uncertainties."""
    
    Xavg = sum(x)/len(x)
    Yavg = sum(y)/len(y)
    XsquarAvg = sum(x**2)/len(x**2)
    XYavg = sum(x*y)/len(x*y)
    
    bottom = ((len(x)-2)*(XsquarAvg - Xavg**2))
    slope = (XYavg - (Xavg*Yavg))/(XsquarAvg - (Xavg**2))
    intercept = ((XsquarAvg*Yavg)-(Xavg*XYavg))/(XsquarAvg - Xavg**2)
    slerr = np.sqrt(((sum((y-(slope*x + intercept))**2))/len(x))/bottom)
    interror = np.sqrt(((sum(  (y - (slope*x + intercept))**2))/len(x))*(XsquarAvg)/((len(x)-2)*(XsquarAvg - Xavg**2)))
    
    return slope, intercept, slerr, interror


def WeightedLinearLeastSquaresFit(x,y,weight):
    """Take in arrays representing (x,y) values for a set of linearly varying data and an array
    of weights w. Performs a weighted linear least squares regression. Return the resulting
    slope and intercept parameters of the best fit line with their uncertainties.
    If the weights are all equal to one, the uncertainties are calculated using the 
    LinearLeastSquaresFit function defined above."""
    if sum(weight)/len(weight)==1:
        return LinearLeastSquaresFit(x,y)
    else:
        w = sum(weight)/len(weight)
        wxy = sum(w*x*y)/len(weight)
        wx = sum(w*x)/len(weight)
        wy = sum(w*y)/len(weight)
        wxsquared = sum(w*(x**2))/len(weight)
    
        slope = ((w*wxy)-(wx*wy))/((w*wxsquared) - (wx**2))
        intercept = ((wxsquared*wy)-(wx*wxy))/(w*wxsquared - (wx**2))
        slerr = np.sqrt((w)/((w*wxsquared) - (wx**2)))
        interror = np.sqrt((wxsquared)/(w*wxsquared - (wx**2)))
        
    return slope, slerr, intercept, interror