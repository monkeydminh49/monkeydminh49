'''Question 7
Level 2

Question: Write a program which takes 2 digits, X,Y as input and generates
a 2-dimensional array. The element value in the i-th row and j-th column 
of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose
the following inputs are given to the program: 3,5 Then, the output of the 
program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''


input_values = input('Enter values: ')

ls = [int(x) for x in input_values.split(',')]
x = ls[0]
y = ls[1]

a = []
r = []

for j in range(0, x):          #row
    for i in range(0, y):      #column
        r.append(j*i)
        if i == y-1:
            a.append(r[:])
            r = []
print(a)