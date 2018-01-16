"""
    A simple polynomial class. Supports differentiation, indefinite integration, and console output with class methods.
    Author: Alexander S. Wheaton
    Date: 16 January 2018
"""

import math

class Polynomial(object):

    # Initialises two class variables: the coefficients of the polynomial as a list the its order as an integer.
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.order = len(coefficients) - 1

    # Returns the order of the polynomial as an integer.
    def returnOrder(self):
        return self.order

    # Recieves a second Polynomial object and returns the sum of the two polynomials as a third Polynomial object.
    def addPolynomial(self, polynomial):

        summedCoefficients = []

        # Second Polynomial object has fewer terms than the first.
        if polynomial.order < self.order:
            for n in range(0, polynomial.order):
                summedCoefficients.append(self.coefficients[n] + polynomial.coefficients[n])
            for n in range(polynomial.order + 1, self.order):
                summedCoefficients.append(self.coefficients[n])

        # Second Polynomial object has the same number of terms as the first.
        if polynomial.order == self.order:
            for n in range(0, self.order):
                summedCoefficients.append(self.coefficients[n] + polynomial.coefficients[n])

        # Second Polynomial object has more terms than the first.
        if polynomial.order > self.order:
            for n in range(0, self.order):
                summedCoefficients.append(self.coefficients[n] + polynomial.coefficients[n])
            for n in range(self.order + 1, polynomial.order):
                summedCoefficients.append(polynomial.coefficients[n])

        # Initialises and returns the sum of the two polynomials as a third Polynomial object.
        return Polynomial(summedCoefficients)

    # Returns a list of the coeffiecients of the derivative of the polynomial.
    def derivative(self):
        differentiatedCoefficients = []
        for n in range(0, self.order):
                differentiatedCoefficients.append((n+1) * self.coefficients[n+1])
        return Polynomial(differentiatedCoefficients)

    # Returns a list of the coefficients of the indefinite integral of the polynomial.
    def integral(self):
        integratedCoefficients = ["C"]
        for n in range(0, self.order):
            integratedCoefficients.append(self.coefficients[n] / (n+1))
        return Polynomial(integratedCoefficients)

    # Outputs the polynomial as a string.
    def show(self):
        polynomialAsString = "P(x) = " + str(self.coefficients[0])
        for n in range(0, self.order):
            polynomialAsString = polynomialAsString + " + " + str(self.coefficients[n+1]) + "x^" + str(n+1)
        return polynomialAsString
