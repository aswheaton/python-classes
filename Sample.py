"""
    A class holding a sample of radioactive nuclei.
    Author: Alexander S. Wheaton
    Date: 23rd January 2018
    Updated: 11th February 2018
"""

from Nucleus import Nucleus

class Sample(object):

    # Initialises the the object instance with size and decay constant and fills an N*N list with Nucleus objects.
    def __init__(self, size, decayConstant):

        self.size = size
        self.decayConstant = decayConstant

        # Initialises an array-like list of lists, filled with Nucleus class objects.
        self.sample = [ [ Nucleus(decayConstant) ] * size ] * size

    # Returns the number of decayed nuclei in the sample.
    def getDecayedNuclei(self):

        numberOfDecayedNuclei = 0

        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.sample[row][col].isDecayed() == True:
                    numberOfDecayedNuclei = numberOfDecayedNuclei + 1

        return numberOfDecayedNuclei

    # Returns the number of undecayed nuclei in the sample.
    def getUndecayedNuclei(self):

        numberOfUndecayedNuclei = 0

        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.sample[row][col].isDecayed() == False:
                    numberOfUndecayedNuclei = numberOfUndecayedNuclei + 1

        return numberOfUndecayedNuclei

    # Simulates the passage of a given time interval in the sample.
    def stepForward(self, timeInterval):

        for row in range(0, self.size):
            for col in range(0, self.size):
                self.sample[row][col].randomDecay(timeInterval)

    # Prints out a visual representation of the Nucleus objects making up the sample.
    def show(self):
        
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.sample[row][col].isDecayed() == False:
                    print(1),
                else:
                    print(0),
            print('\n'),
