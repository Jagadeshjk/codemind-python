a=int(input())
a1=list(map(int,input().split()))
c=0
for i in range(1,a-1):
    if a1[i]%2!=0 and a1[i+1]%2!=0 and a1[i-1]%2!=0:
        c+=1
print(c)