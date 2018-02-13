
"""
    A script that plots a fractal for a given function.py file.
    Author: Alexander S. Wheaton
    Date: 12th February 2018
    Updated: 13th February 2018
"""

import cmath
import matplotlib

def class MathematicalSet(object): 
    
    def __init__(self, initialParameter, complexParameter, thresholdValue, maxIterations):
    
        self.set = []
        z = initialParameter
        
        for iterations in range(0, maxIterations):
            self.set.append(z**2 + complexParameter)
            
        for iterations in range(0, maxIterations): 
            if abs(self.set[iterations])**2 > thresholdValue:
                self.iterationsToThreshold = iterations
                break
    
    def getIterationsToThreshold():
        return iterationsToThreshold

# Initialises a array like list of lists containing mathematical sets.
# This will be a class, later on, that recieves a particular function.

def class FractalSet(object):
    
    def __init__(self, minimum, maximum, step, initialParameter, thresholdValue, maxIterations):
        
        self.set = []
        
        for realComponent in range(minimum.real, maximum.real, step):
            self.set.append([])
            for imaginaryComponent in range(minimum.imag, maximum.imag, step):
                self.set.append()

# Initialises an array-like list of lists containting the iterations to a threshold value for a particular complex parameter.

def class FractalImage(object):

    def __init__(self):
    
    self.fractalImage = []
    
    for row in range(imageCenter.real-imageRowSize/2, imageCenter.real+imageRowSize/2):
        self.fractalImage.sappend([])
        for col in range(imageCenter.imag-imageColSize/2, imageCenter.imag+imageRowSize/2):
            fractalImage[row][col].append(fractalSet[row][col].iterationsToThreshhold())
    
    # Plots the generated image.
    def show(self):
    
        matplotlib.pyplot.imshow(self.fractalImage, aspect=1.1, extent=(xvals.min(),xvals.max(),yvals.min(),yvals.max()))
        matplotlib.pyplot.xlabel('Real Axis')
        matplotlib.pyplot.ylabel('Imaginary Axis')
        matplotlib.pyplot.title('Mandelbrot Fractal')

def main():
    
    # Gets initial parameters for generation of the fractal image.
    
    initialParameter = input('For what initial parameter should the set be calculated? (0 for Mandelbrot Set): ')
    imageRowSize = input('How many pixels wide should the generated image be: ')
    imageColSize = input('How many pixels tall should the generated image be: ')
    
    # Permits the user to center the fractal image a particular coordinate in the complex plane. Defaults to (0, 0).
    
    if input('Center image on the origin of the complex plane (y/n): ') == 'y':
        imageCenter = 0 + 0 * 1j
    else:
        realCenter = float(input('Real center coordinate: '))
        imaginaryCenter = float(input('Imaginary center coordinate: '))
        imageCenter = realCenter + imaginaryCenter * 0j
    
    # Gets more initial parameters for the generation of the fractal image.
    
    maxIterations = int(input('To how many iterations should the fractal be generated: '))
    
    print('Generating image...')
    fractalImage = FractalImage(initialParameter, imageRowSize, imageColSize, imageCenter, maxIterations)
    fractalImage.show()
    
main()
