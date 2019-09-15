x=int(input ("please input a value x:  "))
y=int(input ("please input a value y:  "))
z=int(input ("please input a value z:  "))
if x<y and x<z:
    print('x is least')
elif y<z:
    print('y is least')
elif x==y and y==z:
    print('all are the same')
elif x==y:
    print('x is equal to y')
elif x==z:
    print('x is equal to z')
elif y==z:
    print('y is equal to z')
else:
    print('z is least')
