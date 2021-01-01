# addtion of digits
no=int(input('enter digits to add: '))
count=0
sum=0
while no>0:
    no%10#4,3,2,1
    sum+=no%10
    no=no//10#123,12,1,0
    count+=1
print(sum)
