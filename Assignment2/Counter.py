from collections import Counter

user_input = input("Enter the string: ")
char_counter = Counter(user_input)
print("Character counter: ",dict(char_counter))