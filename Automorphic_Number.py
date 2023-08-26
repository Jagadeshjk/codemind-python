a=int(input())
sq=a*a
temp=c=a
d=0
r1=r2=0
while temp:
    d+=1
    temp//=10
while d:
    r1=r1*10+sq%10
    sq//=10
    d-=1
while r1:
    r2=r2*10+r1%10
    r1//=10
if r2==c:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")