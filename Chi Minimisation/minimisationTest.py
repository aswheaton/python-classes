"""
    Test code for a Chi-Squared minimisation class.
    Author: ALexander S. Wheaton
    Date: 19th October 2018
    Updated 19th October 2018
"""

from LinearChiSquared import LinearChiSquared

def main():
    
    minimisation = LinearChiSquared("testData.txt")
    minimisation.minimiseChiSquared()

main()
