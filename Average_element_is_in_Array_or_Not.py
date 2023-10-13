a=int(input())
a1=list(map(int,input().split()))
s=sum(a1)
q=s//a
print(q in a1)