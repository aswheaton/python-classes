"""
    A simple polynomial class. Supports differentiation, indefinite integration, and console output with class methods.
    Author: Alexander S. Wheaton
    Date: 16 January 2018
    Updated: 29 January 2018
"""

import math

class Polynomial(object):

    # Initialises two class variables: the coefficients of the polynomial as a list the its order as an integer.
    def __init__(self, coefficients):
        self.coefficients = coefficients

    # Returns the order of the polynomial as an integer.
    def getOrder(self):
        return len(self.coefficients) - 1

    # Recieves a second Polynomial object and returns the sum of the two polynomials as a third Polynomial object.
    def addPolynomial(self, polynomial):

        summedCoefficients = []

        # Second Polynomial object has fewer terms than the first.
        if len(polynomial.coefficients) < len(self.coefficients):
            for n in range(0, len(polynomial.coefficients)):
                summedCoefficients.append(self.coefficients[n] + polynomial.coefficients[n])
            for n in range(len(polynomial.coefficients), len(self.coefficients)):
                summedCoefficients.append(self.coefficients[n])

        # Second Polynomial object has the same number of terms as the first.
        if len(polynomial.coefficients) == len(self.coefficients):
            for n in range(0, len(self.coefficients)):
                summedCoefficients.append(self.coefficients[n] + polynomial.coefficients[n])

        # Second Polynomial object has more terms than the first.
        if len(polynomial.coefficients) > len(self.coefficients):
            for n in range(0, len(self.coefficients)):
                summedCoefficients.append(self.coefficients[n] + polynomial.coefficients[n])
            for n in range(len(self.coefficients), len(polynomial.coefficients)):
                summedCoefficients.append(polynomial.coefficients[n])

        # Initialises and returns the sum of the two polynomials as a third Polynomial object.
        return Polynomial(summedCoefficients)

    # Returns a list of the coeffiecients of the derivative of the polynomial.
    def derivative(self):
        differentiatedCoefficients = []
        for n in range(1, len(self.coefficients)):
                differentiatedCoefficients.append(n * self.coefficients[n])
        return Polynomial(differentiatedCoefficients)

    # Returns a list of the coefficients of the indefinite integral of the polynomial.
    def integral(self):
        integratedCoefficients = ["C"]
        for n in range(0, len(self.coefficients)):
            integratedCoefficients.append(self.coefficients[n] / (n+1))
        return Polynomial(integratedCoefficients)

    # Returns the polynomial as a formatted string.
    def show(self):
        polynomialAsString = "P(x) = " + str(self.coefficients[0])
        for n in range(1, len(self.coefficients)):
            polynomialAsString = polynomialAsString + " + " + str(self.coefficients[n]) + "x^" + str(n)
        return polynomialAsString
