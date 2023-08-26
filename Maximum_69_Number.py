a=int(input())
r=0
while a:
    r=r*10+a%10
    a//=10
max=0
b=0
while r:
    if r%10==6 and b==0:
        max=max*10+9
        b=1
    else:
        max=max*10+r%10
    r//=10
print(max)