#1. Write a Python program to Count all letters, digits, and special symbols from the given string
#Input = “P@#yn26at^&i5ve”
#Output: Chars = 8 Digits = 3 Symbol = 4

input_str = "P@#yn26at^&i5ve"  # Input string
letters = 0
digits = 0
symbols = 0
for char in input_str:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
# Output 
print(f"Chars = {letters} Digits = {digits} Symbol = {symbols}")


#2. Write a Python program to remove duplicate characters of a given string.
#Input = “String and String Function”
#Output: String and Function



input_str = "String and String Function"
words = input_str.split()
seen = set()
output_words = []
for word in words:
    if word not in seen:
        seen.add(word)
        output_words.append(word)
output = ' '.join(output_words)
print("Output:", output)


#3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
#Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
#Output:UpperCase : 5, LowerCase : 18, NumberCase : 5, SpecialCase : 11

input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"  # Input string
uppercase = 0
lowercase = 0
numbers = 0
special = 0
for char in input_str:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    elif not char.isspace():
        special += 1
# Output 
print(f"UpperCase : {uppercase}")
print(f"LowerCase : {lowercase}")
print(f"NumberCase : {numbers}")
print(f"SpecialCase : {special}")


#4. Write a Python Count vowels in a string
#input= “Welcome to Python Assignment”
#Output: Total vowels are: 8


input_str = "Welcome to Python Assignment"
# Define vowels
vowels = "aeiouAEIOU"
vowel_count = 0
# Count vowels
for char in input_str:
    if char in vowels:
        vowel_count += 1
# Output 
print("Total vowels are:", vowel_count)
