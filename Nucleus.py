"""
    A simple class holding the nucleus of an atom and its properties.
    Author: Alexander S. Wheaton
    Date: 23rd January 2018
"""

import random

class Nucleus(object):

    # Initialises the object with a decay constant in an undecayed state.
    def __init__(self, decayConstant):
        self.decayConstant = decayConstant
        self.isDecayed = False

    # Randomly does or does not change the state of the object to decayed.
    def randomDecay(self, timeInterval):
        if self.isDecayed != True:
            if random.uniform(0, 1) < (self.decayConstant * timeInterval):
                self.isDecayed = True
