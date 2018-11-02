"""
    Test code for a traffic simulation class object.
    Author: Alexander S. Wheaton
    Date: 06 March 2018
    Updated: 13 March January 2018
"""

import matplotlib.pyplot

from Simulation import Simulation

def main():

    if str(raw_input("Simulate more than one density? (y/n): "))[0] == "y":
        
        # Get a bunch of initial parameters.
        roadLength = input("How long should each road be: ")
        
        print("Over what range of densities should the simulations be run?")
        minimumDensity = float(input("Minimum density? (float 0 < d < 1): "))
        maximumDensity = float(input("Maximum density? (float 0 < d < 1): "))
        simulations = int(input("How many simulations should be run? : "))
        
        iterations = input("To how many iterations should each simulation be run: ")
        
        # Begins the simulation.
        listOfDensities = []
        listOfVelocities = []
        
        density = minimumDensity
        densityStep = (maximumDensity - minimumDensity) / simulations
        
        while density <= maximumDensity:
            
            simulation = Simulation(roadLength, density)
            
            for i in range(iterations):
                simulation.iterate()
            
            listOfDensities.append(simulation.getDensity())
            listOfVelocities.append(simulation.getLastVelocity())
            
            density = density + densityStep
            
            # These lines left for debugging purposes. Displays a graphic for each simulation.
            # matplotlib.pyplot.imshow(simulation.getSimulation(), interpolation="none")
            # matplotlib.pyplot.show()
        
        # Plots the steady state velocity of traffic against the traffic density.
        matplotlib.pyplot.plot(listOfDensities, listOfVelocities, 'b.')
        matplotlib.pyplot.autoscale(enable=True, axis="both", tight=True)
        matplotlib.pyplot.xlabel("Density")
        matplotlib.pyplot.ylabel("Average Velocity, Steady-State")
        matplotlib.pyplot.title("Average Velocity vs. Traffic Density")
        matplotlib.pyplot.show()
        
    else:
        
        # Gets a bunch of initial parameters.
        roadLength = input("How long should the road be: ")
        density = float(input("What should the density of traffic be (float 0 < d < 1): "))
        iterations = input("To how many iterations should the simulation be run: ")
        
        # Begins the simulation.
        simulation = Simulation(roadLength, density)
        
        for i in range(iterations):
            simulation.iterate()
        
        # Outputs the result of the simulation to the console.        
        # simulation.show()
        
        # Displays a graphic illustrating the simulation.
        matplotlib.pyplot.imshow(simulation.getSimulation(), interpolation="none")
        matplotlib.pyplot.show()

main()
