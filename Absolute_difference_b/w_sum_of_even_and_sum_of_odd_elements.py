a=int(input())
a1=list(map(int,input().split()))
s1=s2=0
for i in a1:
    if i%2==0:
        s1=s1+i
    else:
        s2=s2+i
d=s1-s2
print(abs(d))