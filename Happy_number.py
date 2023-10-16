a=int(input())
s=0
while True:
    while a!=0:
        s+=(a%10)**2
        a//=10
    if s==1 or s==7:
        print(True)
        break
    elif s<10:
        print(False)
        break
    else:
        a=s
        s=0