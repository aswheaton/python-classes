"""
    Test code for the Numerical Recipes final project.
    Author: Alexander S. Wheaton
    Date: 27th November 2018
    Updated: 27th November 2018
"""

from DecaySet import DecaySet
from ParameterFit import ParameterFit

import numpy as np

def PDF(time, theta, **kwargs):
    
    tau1, tau2, frac = kwargs.get('tau1'), kwargs.get('tau2'), kwargs.get('frac')
    
    norm1 = (3*np.pi*(1-np.exp(-10.0/tau1))*tau1)**-1
    norm2 = (3*np.pi*(1-np.exp(-10.0/tau2))*tau2)**-1
    
    PDF1 = norm1 * (1+np.cos(theta)**2) * np.exp(-time/tau1)
    PDF2 = norm2 * 3 * np.sin(theta)**2 * np.exp(-time/tau2)

    return(frac*PDF1 + (1-frac)*PDF2)

def PDF_t(time, **kwargs):
    
    tau1, tau2, frac = kwargs.get('tau1'), kwargs.get('tau2'), kwargs.get('frac')
    
    norm1 = (3*np.pi*(1-np.exp(-10.0/tau1))*tau1)**-1
    norm2 = (3*np.pi*(1-np.exp(-10.0/tau2))*tau2)**-1

    PDF1 = norm1 * 3 * np.pi * np.exp(-time/tau1)
    PDF2 = norm2 * 3 * np.pi * np.exp(-time/tau2)

    return(frac*PDF1 + (1-frac)*PDF2)

def main():

    #dataset1 = DecaySet(load=False)
    #dataset1.generateSet(10, 2*np.pi, function=PDF, pdfMax=0.13, size=10000, tau1=1.0, tau2=2.0, frac=0.5)
    #dataset1.plotHistogram(100, write=False)
    
    dataset2 = DecaySet(load=True, filename='datafile-Xdecay.txt', column=1)
    paramFit = ParameterFit(dataset=dataset2.get(), function=PDF_t)
    tau1, tau2, frac = paramFit.maxLikelihood(tau1=1.0, tau2=2.0, frac=0.5, limit_tau1=(0.001,10), limit_tau2=(0.001,10), limit_frac=(0,1), errordef=0.5, pedantic=False)
    print('The fitted parameters are tau1={}, tau2={}, frac={}'.format(tau1, tau2, frac))

    dataset3 = DecaySet(load=True, filename='datafile-Xdecay.txt')
    paramFit = ParameterFit(dataset=dataset3.get(), function=PDF)
    tau1, tau2, frac = paramFit.maxLikelihood(tau1=1.0, tau2=2.0, frac=0.5, limit_tau1=(0.001,10), limit_tau2=(0.001,10), limit_frac=(0,1), errordef=0.5, pedantic=False)
    print('The fitted parameters are tau1={}, tau2={}, frac={}'.format(tau1, tau2, frac))

main()





