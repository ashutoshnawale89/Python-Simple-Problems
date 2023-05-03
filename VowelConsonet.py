#Program to check if a character is a vowel or a consonant

value = input("Enter character value")
value=value.lower()
if (value=="a" or value=="e" or value=="i" or  value=="o" or value=="u"):
    print("Vowel")
else:
    print("Consonant")