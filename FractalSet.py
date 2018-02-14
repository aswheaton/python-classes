"""
    This is a fractal set object, which contains an array-like list of lists of 
    mathematical set objects associated a particular initial parameter and a 
    range of complex parameters.

    Author: Alexander S. Wheaton
    Date: 14th February 2018
    Updated: 14th February 2018
"""

from MathematicalSet import MathematicalSet

class FractalSet(object):

    # Initialises a array like list of lists containing mathematical sets.
    
    def __init__(self, minimum, maximum, step, initialParameter, thresholdValue, maxIterations):
        
        self.set = []
        
        for realComponent in range(minimum.real, maximum.real, step.real):
            self.set.append([])
            for imaginaryComponent in range(minimum.imag, maximum.imag, step.imag):
                self.set.append(MathematicalSet(initialParameter, realComponent + imaginaryComponent, thresholdValue, maxIterations))
    
    # Returns the array-like list of lists so that the mathematical set object elements may be accessed.
    
    def getSet(self):
        return self.set

