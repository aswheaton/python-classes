"""
    Test code for a muon decay time dataset object.
    Author: Alexander S. Wheaton
    Date: 4th October 2018
    Updated: 4th October 2018
"""

from MuonDecaySet import MuonDecaySet

def main():
    tau = float(2.2e-6) #float(input('Enter the half-life of the particle: '))
    interval = float(100.0e-6) #float(input('Longest decay time to record: '))
    size = 500000 #int(input('Number of particles to simulate: '))
    muons = MuonDecaySet(tau, interval, size)
    muons.generateSet()
    muons.printSet()
    muons.plotHistogram()

main()
