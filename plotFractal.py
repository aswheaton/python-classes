"""
    A script that plots a fractal image of iterations to a given threshold for a
    particular initial parameter (normally 0) and over a given range of complex
    parameters.

    Author: Alexander S. Wheaton
    Date: 12th February 2018
    Updated: 13th February 2018
"""

import cmath

from FractalSet import FractalSet
from FractalImage import FractalImage

def main():
    
    # Gets initial parameters for generation of the fractal image.
    
    initialParameter = input('For what initial parameter should the fractal be generated? (0 for Mandelbrot Set): ')
    print('Over what range of complex parameters should the fractal be generated?')
    minimumComplexParameter = input('Minimum complex parameter (A + B * 1j): ')
    maximumComplexParameter = input('Maximum complex parameter (A + B * 1j): ')
    thresholdValue = input('What is the threshold value for divergence: ')
    imageRowSize = input('How many pixels wide should the generated image be: ')
    imageColSize = input('How many pixels tall should the generated image be: ')
    
    # Permits the user to center the fractal image a particular coordinate in the complex plane. Defaults to (0, 0).
    
    if raw_input('Center image on the origin of the complex plane (y/n): ') == 'y':
        imageCenter = 0 + 0 * 1j
    else:
        realCenter = float(input('Real center coordinate: '))
        imaginaryCenter = float(input('Imaginary center coordinate: '))
        imageCenter = realCenter + imaginaryCenter * 1j
    
    # Gets more initial parameters for the generation of the fractal image.
      
    maxIterations = int(input('To how many iterations should the fractal be generated: '))
    
    print('Generating image...')
    
    # Calculates the step size as a complex number.

    # step = (maximumComplexParameter - minimumComplexParameter) / (imageRowSize + imageColSize * 1j)
    
    # Generates a fractal set from the given parameters.

    fractalSet = FractalSet(imageRowSize, imageColSize, minimumComplexParameter, maximumComplexParameter, initialParameter, thresholdValue, maxIterations)
    
    # Generates a fractal image object from the fractal set and displays it.

    fractalImage = FractalImage(fractalSet, minimumComplexParameter, maximumComplexParameter)
    fractalImage.show()
    
main()
