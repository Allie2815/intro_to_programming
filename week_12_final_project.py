# DSC 510
# Week 12
# Programming Assignment Week 12
# Author Allie Dunkel
# 2/19/2023

# Change#: 1 Change(s): Made a program that will allow the user to input either there zip code or there city name to
# see the weather for that area
# Date of Change: 2/19/2023

import json
import requests


def welcome_message():
    print('Welcome to my WeatherMap program!')


def zip_or_city():
    zip_vs_city = input('Would you like to use your zipcode or your city name to look up the weather? ').lower()
    if zip_vs_city == 'city name' or zip_vs_city == 'city' or zip_vs_city == 'city-name':
        print('Please enter your city name: ')
    elif zip_vs_city == 'zipcode' or zip_vs_city == 'zip code' or zip_vs_city == 'zip':
        print('Please enter your zipcode: ')
    else:
        print("Invalid response. Please enter either 'zipcode' or 'city name'.")


def display_weather():
    pass


def main():
    welcome_message()
    zip_or_city()


if __name__ == '__main__':
    main()
