"""
    Voltage field for an electric field calculated from three different
    methods of numerical integration. 
    Author: Alexander S. Wheaton
    Date: 2nd November 2018
    Updated: 2nd November 2018
"""

import matplotlib.pyplot as plt
from ElectricField import ElectricField

class VoltageField(object):
    
    def __init__(self, eField, initialCondition):
            
        self.eField = eField
        self.xValues = self.eField.get()[0]
        self.initialCondition = initialCondition
    
    def eulerMethod(self):
    
        self.yValues = []
        
        for i in range(len(self.xValues)):
            if i == 0:
                self.yValues.append(self.initialCondition)
            else:
                slope = - self.eField.evaluate(self.xValues[i-1])
                self.yValues.append(self.yValues[i-1] + (self.xValues[i]-self.xValues[i-1]) * slope)
    
    def rungeKetta2nd(self):
    
        self.yValues = []
        
        for i in range(len(self.xValues)):
            if i == 0:
                self.yValues.append(self.initialCondition)
            else:
                midpointSlope = - self.eField.evaluate(self.xValues[i-1] + (self.xValues[i]-self.xValues[i-1]) / 2.0)
                self.yValues.append(self.yValues[i-1] + (self.xValues[i]-self.xValues[i-1]) * midpointSlope)
    
    def rungeKetta4th(self):
    
        self.yValues = []
        
        for i in range(len(self.xValues)):
            if i == 0:
                self.yValues.append(self.initialCondition)
            else:
                k1 = - self.eField.evaluate(self.xValues[i-1])
                k2 = - self.eField.evaluate(self.xValues[i-1] + (self.xValues[i]-self.xValues[i-1]) / 2.0)
                k3 = - self.eField.evaluate(self.xValues[i])
                self.yValues.append(self.yValues[i-1] + (self.xValues[i]-self.xValues[i-1]) * (k1 / 6.0 + 2.0 * k2 / 3.0 + k3 / 6.0))
    
    def show(self):
    
        plt.plot(self.xValues, self.yValues)
        plt.title('Voltage Field due to Varying Electric Field')
        plt.xlabel('Position')
        plt.ylabel('Voltage')
        plt.show()
