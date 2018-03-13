"""
    Traffic simulation class object.
    Author: Alexander S. Wheaton
    Date: 06 March 2018
    Updated: 13 March January 2018
"""

import random

class Simulation(object):
    
    # Initialises a single road and populates it randomly.
    def __init__(self, roadLength, density):
        
        self.roadLength = roadLength
        self.density = density
        self.simulation = [[]]
        
        self.totalCars = 0
        self.averageVelocities = []
        
        for col in range(self.roadLength):
            if random.random() <= density:
                self.simulation[0].append(1)
                self.totalCars = self.totalCars + 1
            else:
                self.simulation[0].append(0)
    
    # Generates the next iteration of the road and appends it to the simulation.
    def iterate(self):
        
        nextIteration = []
        
        for col in range(self.roadLength):
            nextIteration.append(0)
        
        carsMoved = 0
        
        for col in range(self.roadLength):
                       
            # Is there a car in the position?
            if self.simulation[len(self.simulation)-1][col] == 1:
                # Is the position the in the last column?
                if col == self.roadLength - 1:
                    # Is the position in front empty?
                    if nextIteration[0] == 0:
                        # Places a car in the next position.
                        nextIteration[0] = 1
                        # Increments the number of cars moved.
                        carsMoved = carsMoved + 1
                    # The car stays in its position.
                    else:
                        nextIteration[col] = 1
                        
                # The car is not in the last column.
                else:
                    # Is the position in front empty?
                    if self.simulation[len(self.simulation)-1][col+1] == 0:
                        # Places a car in the next position.
                        nextIteration[col+1] = 1
                        # Increments the number of cars moved.
                        carsMoved = carsMoved + 1
                    # The car stays in its position.
                    else:
                        nextIteration[col] = 1
        
        # Makes sure the total number of cars isn't zero, and records the average velocity.
        if self.totalCars == 0:
            self.averageVelocities.append(0)
        else:
            self.averageVelocities.append(float(carsMoved) / float(self.totalCars))
        
        # Records the next iteration of the traffic simulation to the array-like list of lists.
        self.simulation.append(nextIteration)
        
    # Prints a visual representation of the array to the console.
    def show(self):
    
        for row in range(len(self.simulation)):
            for col in range(self.roadLength):
                print(self.simulation[row][col]),
            print("\n"),
    
    # Returns the list of lists.
    def getSimulation(self):
        return self.simulation
    
    # Returns the number of cars moved.
    def getCarsMoved(self):
        return carsMoved
    
    # Returs the last velocity (steady-state velocity).
    def getLastVelocity(self):
        return self.averageVelocities[len(self.averageVelocities)-1]
    
    # Returns the traffic density for a particular simulation.
    def getDensity(self):
        return float(self.totalCars) / float(self.roadLength)
