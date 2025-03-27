from collections import Counter

user_input = input("Enter the string: ")
char_counter = Counter(user_input)
print("Character counter: ",dict(char_counter))

# Enter the string: sarthak
# Character counter:  {'s': 1, 'a': 2, 'r': 1, 't': 1, 'h': 1, 'k': 1}