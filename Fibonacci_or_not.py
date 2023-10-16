n=int(input())
a1,a2,b=0,1,0
if n==1 or n==1:
    print(True)
else:
    c=0
    while b<=n:
        b=a1+a2
        a1=a2
        a2=b
        if a2==n:
            c+=1
            break
    if c==0:
        print(False)
    else:
        print(True)