"""
    Test code for the Polynomial class.
    Author: Alexander S. Wheaton
    Date: 16 January 2018
"""

from Polynomial import Polynomial

def main():

    # Initialises two Polynomial objects of the Polynomial class.
    polynomialA = Polynomial([2, 0, 4, -1, 0, 6])
    polynomialB = Polynomial([-1, -3, 0, 4.5])

    # Prints the order of the first polynomial.
    print("The order of Polynomial A is " + str(polynomialA.returnOrder()) + "\n")

    # Initialises a third Polynomial object that is the sum of the first two.
    polynomialC = polynomialA.addPolynomial(polynomialB)

    # Prints the third polynomial as a formatted string.
    print("The sum of Polynomial A and Polynomial B is:\n" + polynomialC.show() + "\n")

    # Initialises a fourth polynomial that is the derivative of the first.
    polynomialD = polynomialA.derivative()

    # Prints the fourth polynomial as a formatted string.
    print("The derivative of Polynomial A is:\n" + polynomialD.show() + "\n")

    # Initialises a fifth polynomial that is the antiderivative of the fourth.
    polynomialE = polynomialD.integral()

    # Prints the fifth polynomial as a formatted string.
    print("This is the antiderivative of the expression above:\n" + polynomialE.show() + "\n")

main()
