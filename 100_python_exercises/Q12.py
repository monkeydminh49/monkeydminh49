'''Question 12
Level 2

Question: Write a program, which will find all such numbers between 1000 
and 3000 (both included) such that each digit of the number is an even 
number. The numbers obtained should be printed in a comma-separated sequence 
on a single line.'''

value = []

for i in range(1000, 3000+1):
    x = True
    i = str(i)
    ls = list(i)
    for j in ls:
        j = int(j)
        if j%2 != 0: x = False
    if x == False: continue
    value.append(i)

print(','.join(value))    

class Student(object):
    def __init__(self, name, id, description):
        self.name = name
        self.id = id
        self.description = description




'''Solution:

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))'''