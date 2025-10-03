#largest of 3 numbers
a=float(input('enter the a value'))
b=float(input ('enter the b value'))
c=float(input('enter the c value'))
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print('the biggest number is',c)
