# Katrina Finch
# April 14, 2026
# P2HW2
# How to write code that will collect information and present an understanding of Lists

#Empty list
test_list = []

#Create a list of 6 Module tests 
mod1  = float(input("Enter your grade for Module 1: "))
test_list.append(mod1)
mod2  = float(input("Enter your grade for Module 2: "))
test_list.append(mod2)
mod3  = float(input("Enter your grade for Module 3: "))
test_list.append(mod3)
mod4  = float(input("Enter your grade for Module 4: "))
test_list.append(mod4)
mod5  = float(input("Enter your grade for Module 5: "))
test_list.append(mod5)
mod6  = float(input("Enter your grade for Module 6: "))
test_list.append(mod6)

#Calculate the lowest grade
lgrade = min(test_list)
#Calculate the highest grade
hgrade = max(test_list)
#Calculate the sum of all grades
sgrade = sum(test_list)
#Calculate the average of all grades
num_items = len(test_list)
agrade = (sgrade)/(num_items)

print()
print(f'------------Results-----------')
print(f'{'Lowest Grade: ':<25} {lgrade:<25}')
print(f'{'Highest Grade: ':<25} {hgrade:<25}')
print(f'{'Sum of Grades: ':<25} {sgrade:<25}')
print(f'{'Average: ':<25} {agrade:<25,.2f}')
