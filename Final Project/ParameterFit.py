"""
    N-parameter fitting object using various methods.
    Author: Alexander S. Wheaton
    Date: 29th November 2018
    Updated: 29th november 2018
"""

from iminuit import Minuit

import numpy as np

class ParameterFit(object):
    
    def __init__(self, **kwargs):

        """
            N-parameter fitting object using various minimisation methods.
            Syntax:
        """
        
        self.dataset = np.array(kwargs.get('dataset'))
        self.function = kwargs.get('function')

    def chiSquared(self, **kwargs):
        
        """
            This method is not intended for use other than by the object.
            Calculates and returns the value of chi-squared for the dataset.
        """

    def NLL(self, tau1, tau2, frac):
        
        """
            This method is not intended for use other than by the object.
            Calculates and returns the value of the negative log likelihood for the dataset.
        """               

        try:
            NLL = -np.sum(np.log(self.function(*tuple(np.hsplit(self.dataset,np.size(self.dataset,1))), tau1=tau1, tau2=tau2, frac=frac)))
        except IndexError:
            NLL = -np.sum(np.log(self.function(self.dataset, tau1=tau1, tau2=tau2, frac=frac)))
        return(NLL)
   
    def chiMin(self, **kwargs):
        
        """
            Parameter estimation using the chi-squared minimisation method.
        """
        
    def maxLikelihood(self, **kwargs):
        
        """
            Parameter estimation using the maximum likelihood method.
        """

        self.m = Minuit(self.NLL, **kwargs)
        fmin, param = self.m.migrad()
        return(self.m.values[0], self.m.values[1], self.m.values[2])
        
    def simpleErrors(self, **kwargs):
        
        """
            Returns the simple errors of parameters passed to the method.
        """
        
        # Create list of the minimised parameters from Minuit's "dictionary-like" object.
        minParams = [self.m.values[0], self.m.values[1], self.m.values[2]]
        # Create empty list for storing the calculated errors.
        errors = []

        for i in range(len(minParams)):
            # Create (or reset) list of varying parameters from Minuit's "dictionary-like" object.            
            varParams = minParams
            # Vary the currently selected parameter until the NLL > 0.5 then store the parameter.
            print('Minimising ' + str(i) + ' of ' + str(len(minParams)) + ' parameters...\r')
            while self.NLL(*varParams) - self.NLL(*minParams) < 0.5:
                varParams[i] += kwargs.get('step')
            errors.append(varParams[i])

        return(tuple(errors))
        
    def properErrors(self):
        
        """
            Returns the proper errors of parameters passed to the method.
        """
