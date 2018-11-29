"""
    N-parameter fitting object using various methods.
    Author: Alexander S. Wheaton
    Date: 29th November 2018
    Updated: 29th november 2018
"""

from iminuit import Minuit

import numpy as np

class ParameterFit(object):
    
    def __init__(self, dataset, **kwargs):

        """
            N-parameter fitting object using various minimisation methods.
            Syntax:
        """
        
        self.dataset = np.array(dataset)

    def chiSquared(self, **kwargs):
        
        """
            This method is not intended for use other than by the object.
            Calculates and returns the value of chi-squared for the dataset.
        """


    def negLogLikelihood(self, **kwargs):
        
        """
            This method is not intended for use other than by the object.
            Calculates and returns the value of the negative log likelihood for the dataset.
        """
        print(kwargs)
        NLL = -np.sum(np.log(kwargs.get('function')(**kwargs)))

        return(NLL)
   
    def chiMin(self, **kwargs):
        
        """
            Parameter estimation using the chi-squared minimisation method.
        """
        
    def maxLikelihood(self, **kwargs):
        
        """
            Parameter estimation using the maximum likelihood method.
        """
        print(kwargs.iteritems())
        m = Minuit(self.negLogLikelihood, kwargs.iteritems())
        fmin, param = m.migrad()        
        return(param)













