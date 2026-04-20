# Katrina Finch
# April 14, 2026
# P2LAB2
# Create a dictionary

my_dict = {'Camaro':18.21, 'Prius': 52.36, 'Model S':110, 'Silverado':26}

#Get keys from dict
keys = my_dict.keys ()

print(keys)

print (*keys, sep = ", ")

#Get a car from user
car_name = input("Enter a car: ")

#Display the MPG
car_mpg = my_dict [car_name]

print(f"The {car_name} gets {car_mpg: .2f} mpg.")

#Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}?"))

#Calculate The gallons of gas that are needed to drive the specified vehicle The number of miles
gallons_needed = miles_driven/car_mpg

#Display the results
print (f"{gallons_needed:.2f}: gallon(s) of gas re needed to drive the {car_name} {miles_driven: .2f} miles.")