n=int(input())
sq=n*n
r=0
while n:
    r=r*10+n%10
    n//=10
sr=r*r
a=0
while sr:
    a=a*10+sr%10
    sr//=10
if a==sq:
    print(True)
else:
    print(False)