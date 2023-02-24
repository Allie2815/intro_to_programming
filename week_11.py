# DSC 510
# Week 11
# Programming Assignment Week 11
# Author Allie Dunkel
# 2/23/2023

# Change#: 1
# Change(s): Made a simple cash register program
# Date of Change: 2/23/2023

import locale


def welcome_message():
    print('Welcome to my cash register!')


class CashRegister:

    def __init__(self):
        self.total_price = 0
        self.count = 0

    # adding items to cart
    def add_item(self, price):
        self.total_price += price
        self.count += 1

    # getting the total price of items in cart
    def get_total(self):
        return self.total_price

    # getting the number of items in cart
    def get_count(self):
        return self.count


def main():
    welcome_message()

    # creating the CashRegister object
    cart = CashRegister()

    while True:
        users_price = input("Enter the price of the item you would like to add. If done, type 'done' to end the "
                            "transaction: ")
        users_input = users_price.lower()

        if users_input == 'done':
            print('Thank you! Please come again!')
            break
        try:
            users_price = float(users_price)
            cart.add_item(users_price)
        except ValueError:
            print('Invalid input. Please try again.')

        # setting the locale to US
        locale.setlocale(locale.LC_ALL, 'us')

        print('You have %d items in your cart.' % cart.get_count())
        print('Your total price comes out to be %s' % locale.currency(cart.get_total()))


if __name__ == '__main__':
    main()
