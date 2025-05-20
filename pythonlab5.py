#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(num1, num2):
  if num2 == 0:
    print("Error: Cannot divide by zero.")
  else:
    result = num1 / num2
    print(f"The division of {num1} by {num2} is: {result}")
div(10, 2)
div(15, 3)
div(8, 0)



#2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .

def square(number):
  squared_number = number * number
  print(f"The square of {number} is: {squared_number}")
square(5)
square(12)



#3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
print(f"The random numbers are: {random_numbers}")
maximum_number = max(random_numbers)
minimum_number = min(random_numbers)
print(f"The maximum number is: {maximum_number}")
print(f"The minimum number is: {minimum_number}")




#4. Accept a namefromthe user and display that in lower case using lower()function.


name = input("Please enter your name: ") # taking input from the user
lower_case_name = name.lower()
print(f"Your name in lower case is: {lower_case_name}")
