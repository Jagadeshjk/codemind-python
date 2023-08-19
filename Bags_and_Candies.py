a,b,c=map(int,input().split())
d=b*c
if a%d==0:
    print(a//d)
else:
    print(a//d+1)