j = []
for i in range(2000, 3000):
  if i%7 == 0 and i%5 > 0:
    j.append(str(i))  #thêm giá trị vào string
print(','.join(j))  #ngăn cách các giá trị bằng dấu phẩy