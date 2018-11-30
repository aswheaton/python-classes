"""
    Class for generating datasets from a given PDF using various Monte Carlo methods.
    Author: Alexander S. Wheaton
    Date: 27th November 2018
    Updated: 27th November 2018
"""

import numpy as np
import matplotlib.pylab as pl

class DecaySet(object):

    def __init__(self, **kwargs):
        
        """
            Decay event dataset object. Either loads a dataset from a file or generates one from parameters.
            Syntax: variable = DecaySet(load=True,filename=filename.txt,column=int)
        """

        if kwargs.get('load') == True:
            self.dataset = np.loadtxt(open(kwargs.get('filename'),'r'))
            if 'column' in kwargs:
                self.dataset = self.dataset[:,kwargs.get('column')-1]
        
    def generateSet(self, maxTime, maxTheta, **kwargs):
        
        """
            Generates a data set from given parameters and given probability density functions.
            Syntax variable.generateSet(time
        """
        
        self.dataset = np.zeros((kwargs.get('size'),3))
        
        for row in range(kwargs.get('size')):

            print('Generating ' + str(row) + ' of ' + str(kwargs.get('size')) + ' data points...\r'),
            
            while True:
                
                time = np.random.uniform() * maxTime
                theta = np.random.uniform() * maxTheta
                probability = kwargs.get('function')(time, theta, **kwargs)
                
                if np.random.uniform() * kwargs.get('pdfMax') < probability:
                    self.dataset[row][0], self.dataset[row][1], self.dataset[row][2] = time, theta, probability
                    break
                
    def get(self):
        
        """
            Returns a numpy array of the dataset.
        """
        
        return(self.dataset)
        
    def show(self):
        
        """
            Prints the dataset, if it exists, to the console.
        """
        
        if len(self.dataset) != 0:
            print(self.dataset)

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
            Plots the histogram of different observables in the dataset.
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
