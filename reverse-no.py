# reverse a number
no=int(input('enter no to reverse: '))
count=0
while no>0:
    print(no%10)#4,3,2,1
    no=no//10#123,12,1,0
    count+=1
    