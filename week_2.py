# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Allie Dunkel
# 12/9/2022

# Change#: 1
# Change(s) Made: Added lines 15-28 following assignment 2.1
# Date of Change: 12/9/2022

# This will get the users name
name = input('What is your name? ')
# This will display a welcome message using the users name
print('Welcome ' + name)
# This will get the users companies name
company_name = input('What is your companies name? ')
# This will get the amount of optic cable the company, and I changed the data type to an integer, so I can multiply
# it on line 16
cable_amount = int(input('How much fiber optic cable will you need (in feet)? '))
# This will calculate the total cost
total_cost = cable_amount * 0.87
# This will print the recipe using all the info from above, I need to change the previous numbers to strings because
# you cannot concatenate a string and an integer
print('The company, ' + company_name + ', will need ' + str(cable_amount) + ' feet of fiber optic cable. The total cost will be ' + str(total_cost) + ' dollars.')