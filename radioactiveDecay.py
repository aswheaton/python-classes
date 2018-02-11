"""
    Test program for the Nucleus class, Sample class, and Radioactive Decay Checkpoint.
    Author: Alexander S. Wheaton
    Date: 23rd January 2018
    Updated: 11th February 2018
"""

from Sample import Sample
        
def main():

    decayConstant = input('What is the value of the decay constant: ')
    size = input('What size should the list of nuclei be: ')
    timeInterval = input('At what time interval should the simulation be run (mins): ')

    sample = Sample(size, decayConstant)

    elapsedTime = 0.0

    while sample.getUndecayedNuclei() <= sample.getDecayedNuclei():

        sample.stepForward(timeInterval)
        elapsedTime = elapsedTime + timeInterval

    sample.show() 
    print('\nThe total elapsed time is ' + str(elapsedTime) + ' minutes.')

main()
