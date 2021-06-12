# The Area of Circle = 3.14 * Radius * Radius

import math

def calculateAreaOfCircle():
    radius = float(input('Please enter the Radius of a Circle : '))
    area = math.pi * radius * radius
    print('The Area of a Circle is {:.2f}'.format(area))