# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Allie Dunkel
# 1/21/2023

# Change#: 1
# Change(s) Made: Created an empty list of temperatures that the user can use to find out the smallest, the largest and
# the quantity they entered quickly and easily.
# Date of Change: 1/21/2023

def temperature_list():
    # Create an empty list called temperatures.
    temperatures = []
    # Allow the user to input a series of temperatures along with a sentinel value (do not use a number for a sentinel
    # value) which will stop the user input.
    while True:
        enter_temps = input("List the temperatures in your area and type 'done' when done: ")
        try:
            if enter_temps == 'done':
                break
            elif int(enter_temps) in range(-200, 200):
                temperatures.append(enter_temps)
        except ValueError:
            print('That was not a temperature. Please try again.')
    # Print the largest temperature.
    print('The warmest temperature was' + ' ' + max(temperatures))
    # Print the smallest temperature.
    print('The coldest temperature was' + ' ' + min(temperatures))
    # Print a message that tells the user how many temperatures are in the list.
    print('You entered ' + str(len(temperatures)) + ' ' + 'temperatures')


def main():
    temperature_list()


if __name__ == '__main__':
    main()
