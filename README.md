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
