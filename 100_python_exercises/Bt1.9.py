import math

C = 50
H = 30
A = input('Nhập chuỗi giá trị: ').split(',')
x = len(A)
Q = []

for i in range(0,x): #Lấy từng giá trị nhập vào
  D = int(A[i])
  Q.append(str(round(math.sqrt((2*C*D)/H)))) #Q sau tối ưu

print(','.join(Q)) #ngăn cách các giá trị bằng dấu phẩy


#Code mẫu

import math
c=50
h=30
value = []
items=[x for x in input("Nhập giá trị của d: ").split(',')]
for d in items:
  value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# Code by Quantrimang.com
print (','.join(value))