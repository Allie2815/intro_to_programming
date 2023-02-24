# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Allie Dunkel
# 2/16/2023

# Change#: 1
# Change(s): Made a program that generates a cat fact from the cat fact API as many times as the user likes.
# Date of Change: 2/16/2023

import requests

url = "https://catfact.ninja/fact"


def welcome_message():
    print('Welcome to my cat fact generator!')


def display_jokes():
    while True:
        user_input = input('Would you like to see a cat fact? (Y/N):  ')
        if user_input == 'Y' or user_input == 'y':
            response = requests.request("GET", url)
            cat_fact = response.json()
            print(cat_fact["fact"])
        elif user_input == 'N' or user_input == 'n':
            print('Come again for more cat facts!')
            break
        else:
            print("Something went wrong. Please try again")


def main():
    welcome_message()
    display_jokes()


if __name__ == '__main__':
    main()
