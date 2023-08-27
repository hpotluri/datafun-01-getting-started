"""

Purpose: Calculate the max, min, sum, avg for user input.

Author: Harinya Potluri

This script illustrates importing modules and using constants.

It illustrates the built-in functions max(), min(), avg().

When we install Python, it comes with the Python standard library.
Nearly all scripts will import at least one module from the standard library.

We can install additional, third-party modules using pip.
We'll do that later. 

All scripts in this repository use only the standard library.


"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
# from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
# logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library
import math
import statistics

# get the radius from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
input_one = int(input("\nEnter the 1st number: "))
input_two = int(input("\nEnter the 2nd number: "))
input_three = int(input("\nEnter the 3rd number: "))

# convert the radius_string to a number
sum = sum([input_one,input_two,input_three])
average = statistics.mean([input_one,input_two,input_three])
product = math.prod([input_one,input_two,input_three])
min = min([input_one,input_two,input_three])
max = max([input_one,input_two,input_three])

# calculate the max min avg and sum for given numbers

# Print the results
print()
print(f"Sum of given numbers is {sum}.")
print(f"Average of given numbers is {average:.2f}.")
print(f"Product of given numbers is {product}.")
print(f"Minimum of given numbers is {min}.")
print(f"Maximum of given numbers is {max}.")

