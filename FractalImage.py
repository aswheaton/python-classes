"""
    This is a fractal image object, which contains an array-like list of lists 
    of iterations to a threshold associated with a fractal set of a particular 
    initial parameter and range of complex parameters.

    Author: Alexander S. Wheaton
    Date: 14th February 2018
    Update: 14th February 2018 
"""

from FractalSet import FractalSet

class FractalImage(object):
    
    # Initialises an array-like list of lists containing the iterations to the threshold value of a fractal set object.
    
    def __init__(self, fractalSet, minumimComplexParameter, maximumComplexParameter):
    
        self.fractalImage = []
        
        for row in range(0, len(fractalSet.getSet())):
            self.fractalImage.sappend([])
            for col in range(0, len(fractalSet.getSet()[row])):
                fractalImage[row][col].append(fractalSet.getSet[row][col].getIterationsToThreshhold())
        
        self.minimum = minimumComplexParameter
        self.maximum = maximumComplexParameter
        
    # Plots the generated image.
    
    def show(self):
    
        matplotlib.pyplot.imshow(self.fractalImage, aspect=1.1, extent=(minimum.real, maximum.real, minimum.imag, maximum.imag))
        matplotlib.pyplot.xlabel('Real Axis')
        matplotlib.pyplot.ylabel('Imaginary Axis')
        matplotlib.pyplot.title('Mandelbrot Fractal')

