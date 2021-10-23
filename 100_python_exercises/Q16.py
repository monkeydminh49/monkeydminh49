input_nums = input('Enter numbers: ').split(',')

x = input_nums[0]
y = input_nums[1]
Z = input_nums[2]

if x+y>z and x+z>y and z+y>x:
    print('1')
else:
    print('0')
    