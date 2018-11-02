"""
    This is a fractal image object, which contains an array-like list of lists 
    of iterations to a threshold associated with a fractal set of a particular 
    initial parameter and range of complex parameters.

    Author: Alexander S. Wheaton
    Date: 14th February 2018
    Update: 14th February 2018 
"""

import cmath

import matplotlib.pyplot

from FractalSet import FractalSet

class FractalImage(object):
    
    # Initialises an array-like list of lists containing the iterations to the threshold value of a fractal set object.
    
    def __init__(self, fractalSet, minimumComplexParameter, maximumComplexParameter):
    
        self.fractalImage = []
        
        for row in range(0, len(fractalSet.getFractalSet())):
            self.fractalImage.append([])
            for col in range(0, len(fractalSet.getFractalSet()[row])):
                self.fractalImage[row].append(fractalSet.getFractalSet()[row][col].getIterationsToThreshold())
        
        self.minimum = minimumComplexParameter
        self.maximum = maximumComplexParameter
        
    # Plots the generated image.
    
    def show(self):
    
        matplotlib.pyplot.imshow(self.fractalImage, cmap='magma', aspect='auto', extent=(self.minimum.real, self.maximum.real, self.minimum.imag, self.maximum.imag))
        matplotlib.pyplot.xlabel('Real Axis')
        matplotlib.pyplot.ylabel('Imaginary Axis')
        matplotlib.pyplot.title('Mandelbrot Fractal')
        matplotlib.pyplot.show()

        print(self.fractalImage)
