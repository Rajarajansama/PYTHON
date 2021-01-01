#palindrome  
no=int(input('enter number:'))
no2=no
count=0
sum=0
while no>0:
    no%10
    sum=(sum*10)+(no%10)
    no=no//10
    count+=1
print(no2)
if sum==no2:
    print('palindrome')
else:
    print('not palindrom')
    