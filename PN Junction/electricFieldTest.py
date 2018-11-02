"""
    Test code for various numerical integration methods of a charge distribution
    and and electric field.
    Author: Alexander S. Wheaton
    Date: 2nd November 2018
    Updated: 2nd November 2018
"""

from ElectricField import ElectricField
from VoltageField import VoltageField

eField = ElectricField(0.0)
eField.eulerMethod()
eField.show()

eField = ElectricField(0.0)
eField.rungeKetta4th()
eField.show()

vField = VoltageField(eField, 0.0)
vField.eulerMethod()
vField.show()

vField = vField = VoltageField(eField, 0.0)
vField.rungeKetta4th()
vField.show()
