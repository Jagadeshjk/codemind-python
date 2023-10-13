a=int(input())
a1=list(map(int,input().split()))
for i in range(a):
    if a1[i]%2==0:
        s=i
print(s)