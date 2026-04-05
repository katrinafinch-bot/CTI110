# Katrina Finch
# April 5, 2026
# P1LAB1
# How to write code that collect information from user, processes information collected and display results to user.  Complete basic math 

# calculate exponents

print('This program calculates and displays travel expenses')
print()

# There will be 5 inputs: BUDGET, DEST, GAS, PLACE, and FOOD.  Using these variable, the result will be calculated.


budget  = int(input("Enter budget: "))
dest = str(input("Enter your travel destination: "))
gas = int(input("How much do you think you will spend on gas? "))
place = int(input("Approximately, how much do Will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
result = budget - gas - place - food

print('-------Travel Expenses------')
print("Location: ", dest)
print("Initial Budget ", budget)
print()
print("Fuel: ", gas)
print("Accommodation: ", place)
print("Food: ", food)
print()
print("Remaining Balance: ", result)