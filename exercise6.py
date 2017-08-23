word = input("Please give a word to check if it is a palindrome: ")
if word == word[::-1]:
    print("It is a palindrome")
else: 
    print("It is not a palindrome")
