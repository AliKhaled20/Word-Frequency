# Word Counter
# This task would involve taking a string of text as input and using a dictionary to keep track of the frequency
# of each word in the text. To do this without loops and conditionals, you can take advantage of Python
# 's built-in string methods and dictionary methods.
import ast
import json
count = {}
input_line = input("Enter a Line : ")
list_of_words = input_line.split()
for word in list_of_words:
    count[word] = count.get(word, 0) + 1
print('Word Frequency')
for key in count.keys():
    print(key, count[key])


