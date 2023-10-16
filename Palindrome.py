n=int(input())
r=0
temp=n
while temp:
    r=r*10+temp%10
    temp//=10
if r==n:
    print(True)
else:
    print(False)