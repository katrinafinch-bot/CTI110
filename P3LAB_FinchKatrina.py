# Katrina Finch
# April 20, 2026
# P3LAB
# How to write code that allows the user to enter a money (float) value with two places after the decimal

# Get value from user 
change = float(input("Enter an amount of money :  $"))

print(f"Change Amount: {change}")

# Converting the value to an integer 
change = round(change * 100)

print(f"Change Amount: {change}")

# Determine how many dollars/coins are needed 
n_dol = change // 100
change = change - (n_dol * 100)

# Determine how many quarters are needed 
n_quar = change // 25
change = change - (n_quar * 25)

# Determine how many dimes are needed 
n_dime = change // 10
change = change - (n_dime * 10)

# Determine how many nickels are needed 
n_nick = change // 5
change = change - (n_nick * 5)

# Determine how many nickels are needed 
n_pen = change // 1
change = change - (n_pen * 1)

if n_dol > 0:
    if n_dol == 1:
        print (f"{n_dol} Dollar")
    else:
        print (f"{n_dol} Dollars")

if n_quar > 0:
    if n_quar == 1:
        print (f"{n_quar} Quarter")
    else:
        print (f"{n_quar} Quarters")

if n_dime > 0:
    if n_quar == 1:
        print (f"{n_dime}  Dime")
    else:
        print (f"{n_dime}  Dimes")

if n_nick > 0:
    if n_nick == 1:
        print (f"{n_nick}  Nickel")
    else:
        print (f"{n_nick}  Nickels")

if n_pen > 0:
    if n_pen == 1:
        print (f"{n_pen}  Penny")
    else:
        print (f"{n_pen}  Pennies")