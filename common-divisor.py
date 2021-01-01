# common divisor of two no
no=int(input('enter no: '))
no1=int(input('enter no: '))
if no<no1:
    i=no
elif no1<no:
    i=no1
while i>=2:
    if no%i==0 and no1%i==0:
        print('common divisor is',i)
        break
    i-=1