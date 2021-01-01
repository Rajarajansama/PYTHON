# prime number
no=int(input('enter no:'))
div=2
while div<no:
    if no%div==0:
        print(no,'is not a prime number')
        break
    div+=1
else:
    print(no,'is a prime number')