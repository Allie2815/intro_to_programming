# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Allie Dunkel
# 12/17/2022

# Change#: 2
# Change(s) Made: Added lines 26-62 following assignment 3.1 - changed the format to match the assignment
# and make more readable and added the if and elif statements
# Date of Change: 12/17/2022

# Change#: 3
# Change(s) Made: Condensed code and made it more readable: Took professors advice
# Date of Change: 1/4/2023


name = input('What is your name? ')
# This will display a welcome message using the users name
print('Welcome ' + name)
# This will get the users companies name
company_name = input('What is your companies name? ')
# This will get the amount of optic cable the company, and I changed the data type to an integer, so I can multiply
# it on line 16
cable_amount = int(input('How much fiber optic cable will you need (in feet)? '))
# This will figure out how much to charge them based on the amount of cable they need. I needed to start with the
# highest number because the program goes in order
if cable_amount > 500:
    price = 0.50
elif cable_amount > 250:
    price = 0.70
elif cable_amount > 100:
    price = 0.80
elif cable_amount <= 100:
    price = 0.87

regular_cost = cable_amount * price
print('The company, ' + company_name + ', will need ' + str(
    cable_amount) + ' feet of fiber optic cable. The total cost will be ' + str(regular_cost) + ' dollars.')