 # addition of digits
no=str(input('enter digits: ' ))
sum=0
i=len(no)-1
while i>=0:
    sum+=int(no[i])
    i-=1
print(sum)