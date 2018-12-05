"""
    N-parameter fitting object using various methods.
    Author: Alexander S. Wheaton
    Date: 29th November 2018
    Updated: 30th november 2018
"""

from iminuit import Minuit

import numpy as np

class ParamFit(object):
    
    def __init__(self, **kwargs):

        """
            N-parameter fitting object using various minimisation methods.
            Syntax:
        """
        
        self.dataset = np.array(kwargs.get('dataset'))
        self.function = kwargs.get('function')

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
            varParams = [self.m.values[0], self.m.values[1], self.m.values[2]]
            # Vary the currently selected parameter until the NLL > 0.5 then store the parameter.
            print('Finding simple errors for {} of {} parameters...\r'.format(i+1, len(minParams))),
            while self.NLL(*varParams) - self.NLL(*minParams) < 0.5:
                varParams[i] += kwargs.get('step')
            errors.append(varParams[i] - minParams[i])
        print('\n'),
        return(tuple(errors))
        
    def properErrors(self, **kwargs):
        
        """
            Returns the proper errors of the fit given a particular step size.
        """
        
        # Create list of the minimised parameters from Minuit's "dictionary-like" object.
        minParams = [self.m.values[0], self.m.values[1], self.m.values[2]]
        # Create empty list for storing the calculated errors.
        errors = []

        for i in range(len(minParams)):
            # Create (or reset) list of varying parameters from Minuit's "dictionary-like" object.            
            varParams = [self.m.values[0], self.m.values[1], self.m.values[2]]
            # Vary the currently selected parameter and reminimise until the NLL > 0.5 then store the parameter.
            print('Finding proper errors for {} of {} parameters:'.format(i+1, len(minParams)))
            
            while (self.NLL(*varParams) - self.NLL(*minParams)) < 0.5:
                # Increments the varying parameter by the step.
                varParams[i] += kwargs.get('step')
                # Re-minimises the NLL with the incremented parameter fixed.
                if i == 0:
                    m = Minuit(self.NLL, tau1=varParams[i], tau2=2.0, frac=0.5, limit_frac=(0,1), print_level=-1, errordef=0.5, pedantic=False, fix_tau1=True)     
                if i == 1:
                    m = Minuit(self.NLL, tau1=1.0, tau2=varParams[i], frac=0.5, limit_frac=(0,1), print_level=-1, errordef=0.5, pedantic=False, fix_tau2=True)
                if i == 2:
                    m = Minuit(self.NLL, tau1=1.0, tau2=2.0, frac=varParams[i], limit_frac=(0,1), print_level=-1, errordef=0.5, pedantic=False, fix_frac=True)           
                fmin, param = m.migrad()
                # Replaces the other parameters with re-minimised ones before the condition is checked again.
                for j in range(len(varParams)):
                    if i != j:
                        varParams[j] = m.values[j]
                print('Trying parameters {}...\r'.format(varParams)),
            print('\n'),
            errors.append(varParams[i] - minParams[i])
        print('\n'),
        return(tuple(errors))
