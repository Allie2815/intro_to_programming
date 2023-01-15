# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Allie Dunkel
# 1/14/2023

# Change#: 1
# Change(s) Made: Made a program where the user can get the sum, difference, product or quotient of their
# friends cats. The user can also find the total and average ages of their cats. And the loop will continue so all
# the friends can find the total and average ages of their cats and once they are done they can type 'done' and the loop
# will stop.
# Date of Change: 1/14/2023

def perform_calculation(operation):
    # This function will prompt the user for two numbers
    cat_amount1 = int(input('Enter how many cats does friend 1 has: '))
    cat_amount2 = int(input('Enter how many cats does friend 2 has: '))
    # The function will then perform the expected operation depending on the parameter that's passed into the function
    # And then the function will print the calculated value for the user.
    if operation == '+':
        print('The sum of both of their cats is ' + str(cat_amount1 + cat_amount2))
    elif operation == '-':
        print('The difference between both of their cats is ' + str(cat_amount1 - cat_amount2))
    elif operation == '*':
        print('The product of both of their cats is ' + str(cat_amount1 * cat_amount2))
    elif operation == '/':
        print('The quotient of both of their cats is ' + str(cat_amount1 / cat_amount2))


def calculate_average():
    total_ages = 0
    # This function will ask the user how many numbers they wish to input.
    number_of_cats = int(input('How many cats do you have? '))
    # This function will use the number of times to run a for loop in order to calculate the total and average.
    for cats in range(number_of_cats):
        ages = int(input('Enter cat\'s ' + str(cats + 1) + ' age in years: '))
        total_ages = ages + total_ages
    # This function will print the calculated average and total.
    print('The total of all of your cats ages are ' + str(total_ages))
    print('The average age of your cats are ' + str(total_ages / number_of_cats))


def main():
    # prompt the user for the operation they wish to perform.

    # The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
    while True:
        operation = input('Do you want to find the sum, difference, product or quotient of your friends cats? '
                          'Type "+", "-", "*", or "/" or "done" to quit: ')
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            perform_calculation(operation)
            calculate_average()
        elif operation == 'done':
            print('Thank you! Please come again!')
            break
        else:
            print('Please try again!')


if __name__ == '__main__':
    main()