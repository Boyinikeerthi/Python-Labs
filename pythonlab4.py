#1. Python program to check leap year

def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

# Get input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")


  
#2. Python Program to Find the Largest Among Three Numbers

def find_largest(num1, num2, num3):
  if (num1 >= num2) and (num1 >= num3):
    largest = num1
  elif (num2 >= num1) and (num2 >= num3):
    largest = num2
  else:
    largest = num3
  return largest

# Get input from the user
try:
  number1 = float(input("Enter the first number: "))
  number2 = float(input("Enter the second number: "))
  number3 = float(input("Enter the third number: "))

  # Find the largest number
  largest_number = find_largest(number1, number2, number3)

  # Display the result
  print(f"The largest number among {number1}, {number2}, and {number3} is {largest_number}")

except ValueError:
  print("Invalid input. Please enter valid numbers.")

  
#3. Python Program to Check if a Number is Positive, Negative or 0

def check_number(number):
  if number > 0:
    print(f"{number} is a positive number.")
  elif number < 0:
    print(f"{number} is a negative number.")
  else:
    print(f"{number} is zero.")

# Get input from the user
try:
  num = float(input("Enter a number: "))
  check_number(num)
except ValueError:
  print("Invalid input. Please enter a valid number.")

  
#4. 4. Atoy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given,
    #and a discount of 10% is given on orders for electrical charging base toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3are used for battery based toys, key-based toys, and electrical charging based
    #toys respectively. Write a program that reads the product code and the order  amount and prints out the net amount that the customer is required to pay after the discount.

def calculate_net_amount(product_code, order_amount):
    discount = 0
  if product_code == 1:  # Battery Based Toys
    if order_amount > 1000:
      discount = 0.10  # 10% discount
  elif product_code == 2:  # Key-based Toys
    if order_amount > 100:
      discount = 0.05  # 5% discount
  elif product_code == 3:  # Electrical Charging Based Toys
    if order_amount > 500:
      discount = 0.10  # 10% discount
  else:
    print("Invalid product code.")
    return order_amount  # No discount applied for invalid code

  net_amount = order_amount * (1 - discount)
  return net_amount

# Get input from the user
try:
  product = int(input("Enter the product code (1 for Battery Based, 2 for Key-based, 3 for Electrical Charging Based): "))
  amount = float(input("Enter the order amount (in Rs.): "))

  # Calculate the net amount
  final_amount = calculate_net_amount(product, amount)

  # Print the net amount
  print(f"The net amount to be paid is Rs. {final_amount:.2f}")

except ValueError:
  print("Invalid input. Please enter a valid numeric product code and order amount.")


#5. Atransport company charges the fare according to following table:
 Distance
 1-50
 51-100
 Charges
 8 Rs./Km
 10 Rs./Km
 > 100
 12 Rs/K

def calculate_fare(distance):
    if 1 <= distance <= 50:
    fare = distance * 8
  elif 51 <= distance <= 100:
    fare = distance * 10
  elif distance > 100:
    fare = distance * 12
  else:
    return "Invalid distance. Please enter a positive distance."
  return fare

# Get the distance traveled from the user
try:
  travelled_distance = float(input("Enter the distance traveled in kilometers: "))

  # Calculate the fare
  total_fare = calculate_fare(travelled_distance)

  # Print the calculated fare
  if isinstance(total_fare, str):
    print(total_fare)
  else:
    print(f"The total fare for the journey is Rs. {total_fare:.2f}")

except ValueError:
  print("Invalid input. Please enter a valid numeric distance.")
