word = input("Please enter a word: ")

reverse = word[::-1]

print(reverse)

if word == reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")