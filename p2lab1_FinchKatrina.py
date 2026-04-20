# Katrina Finch
# April , 2026
# P2LAB1
# The Calculate the diameter, Circumference, and area of a circle

# Import math module to use the constant, math.Pi
import math

# Get radius from user 
radius = float(input("What is the radius of the circle? "))
print()

#calculate diameter
diameter = 2 * radius

# Display the diameter with one decimal point 
print(f"The diameter of the circle is {diameter:.1f}\n")

#calculate circumference
circumference = 2 * math.pi *radius

# Display the circumference with two decimal point 
print(f"The circumference of the circle is {circumference:.2f}\n")

#calculate area
area = math.pi * radius**2

# Display the area with three decimal point 
print(f"The area of the circle is {diameter: .3f}\n")




