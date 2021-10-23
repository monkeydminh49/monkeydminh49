x = int(input("Nhập số nguyên: "))

def result(x):
  print(f'Đáp án là: {x}')

y = 1

if x == 0:
  result(1)
elif x < 0:
  print('Invalid number')
else:
  for i in range(1, x+1):
    y = y*i
  result(y)