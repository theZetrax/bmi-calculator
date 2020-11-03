''' bmi_calculator.py '''
# Module Calculates BMI of a person

import math
def calculate_bmi(weight, height):
    return weight / pow(height, 2)