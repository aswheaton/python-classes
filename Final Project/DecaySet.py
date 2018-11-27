"""
    Class for generating datasets from a given PDF using various Monte Carlo methods.
    Author: Alexander S. Wheaton
    Date: 27th November 2018
    Updated: 27th November 2018
"""

import math
import numpy as np
import matplotlib.pylab as pl

from PDF import PDF

class DecaySet(object):

    def __init__(self, **kwargs):
        
        """
            Decay event dataset object. Either loads a dataset from a file or generates one from parameters.
            Syntax: variable = DecaySet(load=True,datafile=filename.txt)
        """

        if kwargs.get('load') == True:
            self.dataset = np.loadtext(open(kwargs.get('datafile'),'r'))
        
    def generateSet(self, timeInterval, thetaInterval, **kwargs):
        
        """
            Generates a data set from given parameters and given probability density functions.
            Syntax variable.generateSet(
        """
        
        self.dataset = np.zeros((kwargs.get('size'),3))
        
        for row in range(kwargs.get('size')):
            while True:
                time = np.random.uniform() * timeInterval
                theta = np.random.uniform() * thetaInterval
                probability = PDF(time, theta, kwargs.get('tau1'), kwargs.get('tau2'), kwargs.get('frac'))
                if  probability < np.random.uniform() * kwargs.get('pdfMax'):
                    self.dataset[row][0], self.dataset[row][1], self.dataset[row][2] = time, theta, probability
                    break
                
    def write(self, filename):
        
        """
            Exports a datafile of simulated decay times, if they exist.
        """
        
        if len(self.dataset) != 0:
            datafile = open(filename, 'w')
            datafile.write(str(self.dataset))
            datafile.close()

    def plotHistogram(self, bins, **kwargs):
        
        """
            Plots the histogram of different 
        """
        
        pl.figure()
        pl.hist(self.dataset[:,0], bins=bins)
        pl.title('Frequency of Decay Events vs. Lifetime')
        pl.xlabel('Time Elapsed after Capture (s)')
        pl.ylabel('Frequency of Decay Events')
        if kwargs.get('write') == True:
            pl.savefig('lifetimeHistogram.pdf')

        pl.figure()
        pl.hist(self.dataset[:,1], bins=bins)
        pl.title('Frequency of Decay Events vs. Decay Angle')
        pl.xlabel('Decay Angle (rad)')
        pl.ylabel('Frequency of Decay Events')
        if kwargs.get('write') == True:
            pl.savefig('decayAngleHistogram.pdf')

        pl.figure()
        pl.hist(self.dataset[:,2], bins=bins)
        pl.title('Frequency of Decay Events vs. Probability Density Function')
        pl.xlabel('Probability Density Function')
        pl.ylabel('Frequency of Decay Events')
        if kwargs.get('write') == True:
            pl.savefig('PDFHistogram.pdf')
        
        pl.show()
