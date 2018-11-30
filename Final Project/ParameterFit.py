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

    def negLogLikelihood(self, tau1, tau2, frac, **kwargs):
        
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

        m = Minuit(self.negLogLikelihood, **kwargs)
        fmin, param = m.migrad()
        return(m.values[0], m.values[1], m.values[2])













