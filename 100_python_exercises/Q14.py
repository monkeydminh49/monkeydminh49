'''Question 14
Level 2

Question: Write a program that accepts a sentence and calculate the number of 
upper case letters and lower case letters. Suppose the following input is 
supplied to the program: Hello world! Then, the output should be: 
UPPER CASE 1 LOWER CASE 9'''

input_sentence = input('Enter a sentence: ')
x = 0
y = 0

for i in input_sentence:
    if i.isupper():
        x += 1
    elif i.islower():
        y += 1
    else:
        break
print('UPPER CASE ' + str(x) + ' LOWER CASE ' + str(y))