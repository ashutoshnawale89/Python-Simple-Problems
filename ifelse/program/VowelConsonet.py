#Program to check if a character is a vowel or a consonant

count = input("Enter character value")
count=count.lower()
if (count== "a" or count== "e" or count== "i" or  count== "o" or count== "u"):
    print("Vowel")
else:
    print("Consonant")