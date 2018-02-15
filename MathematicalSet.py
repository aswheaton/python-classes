"""
    This is a mathematical set object, which contains an array of the iterated 
    values associated with a particular function (in this case, the Mandelbrot 
    function), an initial parameter, and a complex parameter up to a maximum 
    number of iterations. Records and returns the number of iterations required 
    to reach a given threshold value.

    Author: Alexander S. Wheaton
    Date: 14th February 2018
    Updated: 14th February 2018
"""

import cmath

class MathematicalSet(object): 
    
    # Initialises a mathematical set in a list and an iterations to threshold attribute.
    
    def __init__(self, initialParameter, complexParameter, thresholdValue, maxIterations):
        
        # Iterates over the function, generating a mathematical set, and stores it in a list.
        
        z = initialParameter
        self.set = []
        
        for iterations in range(0, maxIterations):
            self.set.append(z**2 + complexParameter)
        
        # Calculates the number of iterations to the given threshold value. 
        # If the set does not diverge in the given number of iterations, remains 0.
        
        self.iterationsToThreshold = 0
            
        for iterations in range(0, maxIterations): 
            if abs(self.set[iterations])**2 > thresholdValue:
                self.iterationsToThreshold = iterations
                break
    
    def getIterationsToThreshold(self):
        return self.iterationsToThreshold
