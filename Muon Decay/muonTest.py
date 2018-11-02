"""
    Test code for a muon decay time dataset object.
    Author: Alexander S. Wheaton
    Date: 4th October 2018
    Updated: 5th October 2018
"""

import math
import matplotlib.pylab as pl

from MuonDecaySet import MuonDecaySet

def main():
    
    print('\nBeginning the first experiment...')
    
    trueTau = float(input('Enter the half-life of the particle: '))
    interval = float(input('Longest decay time to record: '))
    size = int(input('Number of particles to simulate: '))
    muons = MuonDecaySet(trueTau=trueTau, interval=interval, size=size)
    muons.generateSet()
    muons.writeToFile()
    muons.plotHistogram(100)
    
    print('\nBeginning the second experiment...')
    
    # Runs many experiments and records the mean tau from each to a list.
    experimentalTaus = []
    trials = input('Number of experiments to run: ')
    
    for i in range(trials):
        print('\rRunning ' + str(i+1) + ' of ' + str(trials) + ' experiments.'),       
        muons = MuonDecaySet(trueTau=trueTau, interval=interval, size=size)
        muons.generateSet()
        experimentalTaus.append(muons.getExperimentalTau())    
    print('Done!')
    
    meanTau = sum(experimentalTaus) / len(experimentalTaus)
    
    # Calculates a standard deviation of all the experimentally calculated Tau.
    standardDev = 0
    for i in range(len(experimentalTaus)):
        standardDev = standardDev + (experimentalTaus[i] - meanTau)**2
    standardDev = math.sqrt(standardDev / len(experimentalTaus))
    
    # Calculates the standard error on the average value of tau.
    standardErr = standardDev / math.sqrt(len(experimentalTaus))
    
    print('The average experimental tau is ' + str(meanTau) + ' seconds.')
    print('The standard deviation of tau is ' + str(standardDev) + ' seconds.')
    print('The standard error on the average tau is ' + str(standardErr) + ' seconds.')
    
    # Plots a histogram of the recorded mean tau from each experiment.
    pl.hist(experimentalTaus[:], bins=100)
    pl.title('Distribution of Experimental Tau')
    pl.xlabel('Experimental Tau (s)')
    pl.ylabel('Frequency')
    pl.savefig('tauHistogram.pdf')
    pl.show()

main()
