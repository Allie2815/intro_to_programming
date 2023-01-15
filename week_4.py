# DSC 510
# Week 4
# Programming Assignment Week 4
# Author Allie Dunkel
# 1/4/2023

# Change#: 1
# Change(s) Made: Made a function with two parameters  that will calculate the cost based upon the number
# of feet being ordered.
# Date of Change: 1/4/2023

def welcome():
    print('Welcome to our Cable Company')


def company_name():
    comp_name = input('What is the name of your company? ')
    return comp_name


def find_cost(feet, price):
    total_cost = feet * price
    return total_cost


def calculate_cost(feet):
    if feet > 500:
        price = find_cost(feet, .50)
    elif feet > 250:
        price = find_cost(feet, 0.70)
    elif feet > 100:
        price = find_cost(feet, 0.80)
    elif feet <= 100:
        price = find_cost(feet, 0.87)
    return price


def main():
    welcome()
    comp_name = company_name()
    feet = int(input('How much fiber optic cable will you need (in feet)? '))
    final_cost = calculate_cost(feet)
    print('The company, ' + comp_name + ', will need ' + str(
        feet) + ' feet of fiber optic cable. The total cost will be $' + str(final_cost))


if __name__ == '__main__':
    main()