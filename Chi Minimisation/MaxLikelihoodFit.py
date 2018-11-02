"""
    Chi-Squared calculation for a linear data set and its errors given 
    Author: Alexander S. Wheaton
    Date: 19th October 2018
    Updated: 19th October 2018
"""

import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit

class MaxLikelihoodFit(object):

    def __init__(self, filename):
        
        data = np.loadtxt(open(filename,"r"))
        
        self.x = data[:,0]
        self.y = data[:,1]
        self.e = data[:,2]
        
    def getChiSquared(self, m, c):

        """
            Method used by Minuit object to get values of chi-squared.
        """
        
        chiSquared = np.sum(((self.y - (m * self.x + c)) / 2.0)**2.0)
        return chiSquared
        
    def minimiseChiSquared(self):
        
        """
            Minimises chi-squared for a given object method and determines
            the minimising parameters: m and c.
        """
        
        # Initialises a Minuit object for the dataset and calculates the minimim
        # chi-squared, associated parameters, and errors.
        m = Minuit(self.getChiSquared, print_level=0, pedantic=False, errordef=1)
        fmin, param = m.migrad()
        m.minos()
        
        # Outputs the calculated parameters to the console.
        m.print_param()
        
        # Generates a plot for the varying of the parameter 'm'.        
        plt.figure()
        m.draw_profile('m')
        c, fa = m.profile('m')
        plt.show()

        # Generates a plot for the varying of the parameter 'c'.
        plt.figure()
        m.draw_profile('c')
        c, fa = m.profile('c')
        plt.show()
