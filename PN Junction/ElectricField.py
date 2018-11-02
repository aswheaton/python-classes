"""
    Electric field for a charge distribution calculated from three different
    methods of numerical integration. 
    Author: Alexander S. Wheaton
    Date: 2nd November 2018
    Updated: 2nd November 2018
"""
import matplotlib.pyplot as plt
from ChargeDistribution import ChargeDistribution

class ElectricField(object):
    
    def __init__(self, initialCondition):
            
        self.rho = ChargeDistribution()
        self.xValues = self.rho._get()[0]
        self.initialCondition = initialCondition

    def eulerMethod(self):
    
        self.yValues = []
        
        for i in range(len(self.xValues)):
            if i == 0:
                self.yValues.append(self.initialCondition)
            else:
                slope = self.rho.evaluate(self.xValues[i-1])
                self.yValues.append(self.yValues[i-1] + (self.xValues[i]-self.xValues[i-1]) * slope)
    
    def rungeKetta2nd(self):
    
        self.yValues = []
        
        for i in range(len(self.xValues)):
            if i == 0:
                self.yValues.append(self.initialCondition)
            else:
                midpointSlope = self.rho.evaluate(self.xValues[i-1] + (self.xValues[i]-self.xValues[i-1]) / 2.0)
                self.yValues.append(self.yValues[i-1] + (self.xValues[i]-self.xValues[i-1]) * midpointSlope)
    
    def rungeKetta4th(self):
    
        self.yValues = []
        
        for i in range(len(self.xValues)):
            if i == 0:
                self.yValues.append(self.initialCondition)
            else:
                k1 = self.rho.evaluate(self.xValues[i-1])
                k2 = self.rho.evaluate(self.xValues[i-1] + (self.xValues[i]-self.xValues[i-1]) / 2.0)
                k3 = self.rho.evaluate(self.xValues[i])
                self.yValues.append(self.yValues[i-1] + (self.xValues[i]-self.xValues[i-1]) * (k1 / 6.0 + 2.0 * k2 / 3.0 + k3 / 6.0))
    
    def get(self):
        return(self.xValues, self.yValues)
    
    def evaluate(self, x):
        for i in range(len(self.xValues)):
            if x > self.xValues[i-1] and x < self.xValues[i]:
                return (self.yValues[i-1] + self.yValues[i]) / 2.0
            elif x == self.xValues[i]:
                return self.yValues[i]
    
    def show(self):
    
        plt.plot(self.xValues, self.yValues)
        plt.title('Electric Field Due to a Charge Distribution')
        plt.xlabel('Position')
        plt.ylabel('Electric Field')
        plt.show()
