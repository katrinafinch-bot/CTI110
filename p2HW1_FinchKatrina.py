# Katrina Finch
# April 14, 2026
# P2HW1
# How to write code that collect information from user, processes information collected and display results to user.  Complete basic math 

# calculate exponents

print('This program calculates and displays travel expenses')
print()

# There will be 5 inputs: BUDGET, DEST, GAS, PLACE, and FOOD.  Using these variable, the result will be calculated.


budget  = int(input("Enter budget: "))
print()
dest = str(input("Enter your travel destination: "))
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
place = int(input("Approximately, how much do Will you need for accommodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
result = budget - gas - place - food
print()

print(f'------------Travel Expenses-----------')
print(f'{'Location: ':<25} ${dest:<25}')
print(f'{'Initial Budget: ':<25} ${budget:<25,.2f}')
print(f'{'Fuel: ':<25} ${gas:<25,.2f}')
print(f'{'Accomodation: ':<25} ${place:<25,.2f}')
print(f'{'Food: ':<25} ${food:<25,.2f}')
print(f'--------------------------------------')
print()
print(f'{'Remaining Balance: ':<25} ${result:<25.2f}')