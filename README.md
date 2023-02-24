# intro_to_programming
All the assignments from my Introduction to Programming class


## Week 2 [Week 2 Code](week_3.py)
Create a program with the following requirements:
Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Refer to the submission instructions for an example of a header.
Display a welcome message for your user.
Retrieve the company name from the user.
Retrieve the number of feet of fiber optic cable to be installed from the user.
Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
Include appropriate comments throughout the program.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.

## Week 3 [Week 3 Code](week_2.py)
This week we will implement “if statements” in a program. Your program will calculate the cost of fiber optic cable installation by multiplying the number of feet needed by $0.87. We will also evaluate a bulk discount. You will prompt the user for the number of fiber optic cable they need installed. Using the default value of $0.87 calculate the total expense. If the user purchases more than 100 feet they are charged $0.80 per foot. If the user purchases more than 250 feet they will be charged $0.70 per foot. If they purchase more than 500 feet, they will be charged $0.50 per foot.
Your program must have a header. See below for an example of what must be included with each assignment. 
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
Display a welcome message for your program.
Get the company name from the user.
Get the number of feet of fiber optic cable to be installed from the user.
Evaluate the total cost based upon the number of feet requested.
Display the calculated information including the number of feet requested and company name.

## Week 4 [Week 4 Code](week_4.py)
This week we will modify our IF Statement program to add a function to do the heavy lifting.
Modify your IF Statement program to add a function. This function will perform the cost calculation. The function will have two parameters (feet and price). When you call the function, you will pass two arguments to the function; feet of fiber to be installed and the cost (remember that price is dependent on the number of feet being installed). You should have the following:
Your program must have a header. 
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
A welcome message.
A function with two parameters.
A call to the function.
The application should calculate the cost based upon the number of feet being ordered.
A printed message displaying the company name and the total calculated cost.
All costs should display in USD Currency Format Ex: $123.45.
Your program must have a properly defined main method and a properly defined call to main.

## Week 5 [Week 5 Code](week_5.py)
Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
This function will print the calculated value for the end user.
Define a function named calculateAverage which takes no parameters.
This function will ask the user how many numbers they wish to input.
This function will use the number of times to run the program within a for loop in order to calculate the total and average.
This function will print the calculated average.

## Week 6 [Week 6 Code](week_6.py)
Create an empty list called temperatures.
Allow the user to input a series of temperatures along with a sentinel value (do not use a number for a sentinel value) which will stop the user input.
Evaluate the temperature list to determine the largest and smallest temperature.
Print the largest temperature.
Print the smallest temperature.
Print a message that tells the user how many temperatures are in the list.

## Week 8 [Week 8 Code](week_8.py)
We will create a program which performs three essential operations. It will process this .txt file: Gettysburg.txt. Calculate the total words, and output the number of occurrences of each word in the file.
Open the file and process each line.
Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.

## Week 9 [Week 9 Code](week_9.py)
For this week we will modify our Gettysburg processing program from week 8 in order to generate a text file from the output rather than printing to the screen. Your program should have a new function called process_file which prints to the file (this method should almost be the same as the pretty_print function from last week. Keep in mind that we have print statements in main as well. Your program must modify the print statements from main as well.

## Week 10 [Week 10 Code](week_10.py)
Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.  By default the API will deliver random jokes however you should choose category Science for your category and only generate jokes of this category unless you give the user to select a category which is also feasible.  I'll leave this up to you since it’s your program however defaulting to random is not acceptable.
If you would prefer you can also use an alternative API from https://www.boredapi.com to generate a list of random things to do when you're bored or https://catfact.ninja/fact to generate a random cat fact.
The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to obtain the “value” key.
If you choose the chuck Norris API you should output the “Value”.
 If you choose boreapi you should output the "Activity" and the "Type". 
If you choose Catfact you should output the "fact.  The following Requirements are the same regardless of which API you use.
Your program should allow the user to request a joke, activity, or catfact as many times as they would like. You should make sure that your program does error checking at this point. If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user. There are other ways to handle this. Think about included string functions you might be able to call.

## Week 11 [Week 11 Code](week_11.py)
This week we’re going to demonstrate our knowledge of Python object oriented programming concepts by creating a simple cash register program.
Your program must have one class called CashRegister.
Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
Your program should have two getter methods.
getTotal – returns totalPrice
getCount – returns the itemCount of the cart
Your program must have a properly defined main function and a call to main.
Your program must create an instance of the CashRegister class within your main function.
Your program should have a loop in main which allows the user to continue to add items to the cart until they request to quit.
Your program should print the total number of items in the cart.
Your program should print the total $ amount of the cart.
The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.


## Week 12 - Final Project [Week 12 Code](week_12_final_project.py)
Create a header for your program just as you have in the past.
Create a Python Application which asks the user for their zip code or city (Your program must perform both a city and a zip lookup). You must ask the user which they want to perform with each iteration of the program.
Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
Display the weather forecast in a readable format to the user. Do not display the weather data in Kelvin, since this is not readable to the average person.  You should allow the user to choose between Celsius and Fahrenheit and ideally also Kelvin.
Use comments within the application where appropriate in order to document what the program is doing. Comments should add value to the program and describe important elements of the program.
Use functions including a main function and a properly defined call to main. You should have multiple functions.
Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
Validate whether the user entered valid data. If valid data isn’t presented notify the user. Your program should never crash with bad user input.
Use the Requests library in order to request data from the webservice.
Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
