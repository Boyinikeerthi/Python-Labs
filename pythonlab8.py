#1. Write a Python program to count the occurrences of each word in a given sentence
  #string = “To change the overall look of your document. To change the look available in the gallery”

string1 = "To change the overall look of your document. To change the look available in the gallery"
word_list = string1.lower().replace('.', '').split()
word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1
print("Word occurrences:\n", word_count)



#2. Write a Python program to remove a newline in Python
  #String = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"
cleaned_string = string.replace('\n', '')
print(cleaned_string)



#3. Write a Python program to reverse words in a string
 #String = “Deeptech Python Training”

string = "Deeptech Python Training"
reversed_string = " ".join(string.split()[::-1])
print(reversed_string)




#4. Write a Python program to count and display the vowels of a given text
 #String=”Welcome to python Training

def count_and_display_vowels(text):
  vowels = "aeiouAEIOU"
  vowel_counts = {}
  for char in text:
    if char in vowels:
      vowel_counts[char] = vowel_counts.get(char, 0) + 1

  print("Vowel counts:")
  for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")

string = "Welcome to python Training"
count_and_display_vowels(string)

