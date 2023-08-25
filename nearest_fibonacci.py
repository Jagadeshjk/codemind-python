a=int(input())
f=0
s=1
n=f+s
while n<=a:
    f=s
    s=n
    n=f+s
if a-s<n-a:
    print(s)
elif a-s>n-a:
    print(n)
else:
    print(s,n)