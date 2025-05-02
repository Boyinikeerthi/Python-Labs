#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

a=int(input("Enter a number= ")) #taking user input
print("Even"if a%2==0 else "odd") #ternary operator



# 2. Using input function take two number and then swap the number


b=int(input("Enter the number= "))
c=int(input("Enter the number= ")) #taking user input
b, c = c, b
print("After swapping")
print("First number= ",b)
print("Second number= ",c) #swapping the two numbers



# 3. Write a Program to Convert Kilometers to Miles


kilometers = float(input("Enter distance in kilometers= ")) #taking user input
conversion_factor = 0.621371 # Conversion factor
miles = kilometers * conversion_factor # Calculate miles
print(f"{kilometers} kilometers is equal to miles")



# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year

# Define the values
Amount = 200  # Amount in Rs.
perc = 5         # Rate of interest in percentage
time = 5         # Time in years
simple_interest = (Amount * perc * time) / 100 # Calculate simple interest
print(f"Simple Interest = Rs. {simple_interest}") # Print the result
