
"""
    A script that plots a fractal for a given function.py file.
    Author: Alexander S. Wheaton
    Date: 12th February 2018
    Updated: 13th February 2018
"""

import cmath

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
        
    iterations = int(input('To how many iterations should the fractal be generated: '))
    
main()
