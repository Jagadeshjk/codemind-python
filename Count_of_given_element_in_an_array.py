a=int(input())
a1=list(map(int,input().split()))
b=int(input())
c=0
for i in range(a):
    if a1[i]==b:
        c+=1
print(c)