# amstrong no  
no=int(input('enter number:'))
no2=no
count=0
armstrong=0
while no>0:
    rem=no%10
    armstrong=armstrong+(rem*rem*rem)
    no=no//10
    count+=1
print(armstrong)
if armstrong==no2: 
    print('armstrong')
else:
    print('not amstrong')
 
output:
enter number:153
153
armstrong
