"""
    A simple class holding the nucleus of an atom and its properties.
    Author: Alexander S. Wheaton
    Date: 23rd January 2018
    Updated: 11th February 2018
"""

import random

class Nucleus(object):

    # Initialises the object with a decay constant in an undecayed state.
    def __init__(self, decayConstant):
        self.decayConstant = decayConstant
        self.decayed = False
    
    # Returns a boolean value of whether the nucleus object is decayed.
    def isDecayed(self):
        return self.decayed

    # Randomly does or does not change the state of the object to decayed.
    def randomDecay(self, timeInterval):
        if self.decayed != True:
            if random.random() < (self.decayConstant * timeInterval):
                self.decayed = True
