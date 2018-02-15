"""
    This is a fractal set object, which contains an array-like list of lists of 
    mathematical set objects associated a particular initial parameter and a 
    range of complex parameters.

    Author: Alexander S. Wheaton
    Date: 14th February 2018
    Updated: 14th February 2018
"""

import cmath

from MathematicalSet import MathematicalSet

class FractalSet(object):

    # Initialises a array like list of lists containing mathematical sets.
    
    def __init__(self, rowSize, colSize, minimum, maximum, initialParameter, thresholdValue, maxIterations):
        
        self.set = []

        realComponent = minimum.real

        step = ( (maximum.real - minimum.real) / rowSize ) + ( (maximum.imag - minimum.imag) / colSize ) * 1j
        
        for row in range(0, rowSize):
            self.set.append([])
            imaginaryComponent = minimum.imag
            for col in range(0, colSize):
                self.set[row].append(MathematicalSet(initialParameter, realComponent + imaginaryComponent, thresholdValue, maxIterations))
                imaginaryComponent = imaginaryComponent + step.imag
            realComponent = realComponent + step.real

    # Returns the array-like list of lists so that the mathematical set object elements may be accessed.
    
    def getFractalSet(self):
        return self.set
