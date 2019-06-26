x = (1,2,'3',[4,'one'],5)
y = [1,2,'3',[4,'one'],5]


print(type(x))
print(type(y))
print(id(x))
print(id(y))
print('x is {}'.format(x))
print('y is {}'.format(y))

if x[0] is y[0]:
    print('the item is same')
else:
    print('the item is not same')

if x is y:
    print('the same object')
else:
    print("it's the another object")