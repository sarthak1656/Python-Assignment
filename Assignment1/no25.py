with open("sample.txt", "w") as file:
    file.write("This is a sample text file. This file is for testing word count.")

with open("sample.txt", "r") as file:
    text = file.read().lower()

words = text.split()
word_count={}

for i in words:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
        

print(word_count)


