#1. Print the first 10 natural numbers using for loop

print("The first 10 natural numbers are:")
for i in range(1, 11):  #it will repeat the statement multiple times
  print(i)


#2. Python program to check if the given string is a palindrome

def is_palindrome_string(input_string):
  processed_string = ''.join(filter(str.isalnum, input_string)).lower()
  reversed_string = processed_string[::-1]
  return processed_string == reversed_string

text = input("Enter a string: ") # Get input from the user
if is_palindrome_string(text):  # Check if the string is a palindrome
  print(f"'{text}' is a palindrome.")
else:
  print(f"'{text}' is not a palindrome.")


#3. Python program to check if a given number is an Armstrong number

def is_armstrong(num):
  num_str = str(num)
  num_digits = len(num_str)
  armstrong_sum = 0
  for digit in num_str:
    armstrong_sum += int(digit) ** num_digits
  return armstrong_sum == num
number = int(input("Enter an integer: "))
if is_armstrong(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")




#4. Python program to get the Fibonacci series between 0 to 50

def fibonacci_series(limit):
  fib_series = []
  a, b = 0, 1
  while a < limit:
    fib_series.append(a)
    a, b = b, a + b
  return fib_series
fib_numbers = fibonacci_series(50)
print("Fibonacci series between 0 and 50:")
print(fib_numbers)




#5. Python program to check the validity of password input by user

import re

def is_valid_password(password):
  if len(password) < 8:
    return False
  if not re.search(r"[A-Z]", password):
    return False
  if not re.search(r"[a-z]", password):
    return False
  if not re.search(r"[0-9]", password):
    return False
  if not re.search(r"[!@#$%^&*]", password):
    return False
  return True
password = input("Enter your password: ")
# Check the validity of the password
if is_valid_password(password):
  print("Password is valid.")
else:
  print("Password is not valid. Please ensure it meets the following criteria:")
  print("- At least 8 characters long")
  print("- Contains at least one uppercase letter")
  print("- Contains at least one lowercase letter")
  print("- Contains at least one digit")
  print("- Contains at least one special character (!@#$%^&*)")
