a=int(input())
sum=0
pro=1
while a!=0:
    s=a%10
    sum=sum+s
    pro=pro*s
    a=a//10
if sum==pro:
    print("Spy Number")
else:
    print("Not Spy Number")