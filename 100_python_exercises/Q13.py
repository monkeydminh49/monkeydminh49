'''Question 13
Level 2

Question: Write a program that accepts a sentence and calculate the number of 
letters and digits. Suppose the following input is supplied to the program: 
hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3'''

import re

input_sentence = input('Enter a sentence: ')
input_sentence = input_sentence.rstrip()
ls = re.findall('[A-Za-z+]', input_sentence)
ls1 = re.findall('[0-9+]', input_sentence)
print('LETTERS: ' + str(len(ls)) + ' DIGITS: ' + str(len(ls1)))

'''Solution:

s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])'''