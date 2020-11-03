#!/usr/bin/python

import sys
from bmi_calculator import calculate_bmi

# Program that calculates BMI
# Required Arguemnts: Height, Weight

if (len(sys.argv) == 2) and (sys.argv[1] == "--help"):
    print('BMI Calculator Program:')
    print('         --help  Provide information about the program.')
    print('    Arguments')
    print('         Weight  Weight of the person')
    print('         Height Height of the person')
    quit(1) # Quitting
if (len(sys.argv) < 3):
    print('Number of argument is less than 2.')

weight = float(sys.argv[1])
height = float(sys.argv[2])

print("Your BMI is: %.2f"%(calculate_bmi(weight, height)))