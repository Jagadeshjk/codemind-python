n=int(input())
temp=n
s,r=0,0
while n:
    r=r*10+n%10
    n//=10
i = 1
while r:
    s+=(r%10)**i
    r//=10
    i+= 1
if s==temp:
    print(True)
else:
    print(False)