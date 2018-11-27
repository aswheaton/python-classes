"""
    Test code for the Numerical Recipes final project.
    Author: Alexander S. Wheaton
    Date: 27th November 2018
    Updated: 27th November 2018
"""

from DecaySet import DecaySet
import math as m

def main():

    dataset = DecaySet()
    dataset.generateSet(10, 2*m.pi, tau1=1.0, tau2=2.0, frac=0.5, pdfMax=0.16, size=1000)
    dataset.plotHistogram(100, write=False)

main()
