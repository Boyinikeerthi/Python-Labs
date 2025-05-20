#1. Write a python program to reverse a number using a while loop.

def reverse_number(num):
  reversed_num = 0
  while num > 0:
    remainder = num % 10  # To get the last digit
    reversed_num = (reversed_num * 10) + remainder  #To Build the reversed number
    num //= 10  # To Remove the last digit from the original number
  return reversed_num
number = int(input("Enter an integer: ")) # Taking input from the user
reversed_number = reverse_number(number) # To reverse the number
# Display the reversed number
print(f"The reversed number is: {reversed_number}")



#2. Write a python program to check whether a number is palindrome or not?

def is_palindrome(num):
  original_num = num
  reversed_num = 0
  while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num //= 10
  return original_num == reversed_num
number = int(input("Enter an integer: "))  # Taking input from the user
if is_palindrome(number): # Check if the number is a palindrome
  print(f"{number} is a palindrome.")
else:
  print(f"{number} is not a palindrome.")




#3. Write a python program finding the factorial of a given number using a while loop.

def factorial_while_loop(n):
  if n < 0:
    return "Factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    factorial = 1
    while n > 0:
      factorial *= n
      n -= 1
    return factorial
num = int(input("Enter a non-negative integer: "))  #Taking input from the user
result = factorial_while_loop(num) # Calculate and display the factorial
print(f"The factorial of {num} is: {result}")



#4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers

total_sum = 0
while True:
  try:
    user_input = int(input("Enter a number (enter 0 to stop): ")) #Taking user input
    if user_input == 0:
      break  
    total_sum += user_input
  except ValueError:
    print("Invalid input. Please enter a valid integer.")

print(f"The sum of all the entered numbers is: {total_sum}")
