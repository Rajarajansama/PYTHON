# palindrome
no=input('enter no:')
reverse=''
i=len(no)-1
while i>=0:
    reverse+=no[i]
    print(no[i])
    i-=1
print(reverse)
if reverse==no:
    print('palindrome')
else:
    print('not plindrome')