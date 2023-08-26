a=int(input())
flag=0
s=0
b=a
if a<0:
    flag=1
    b=abs(a)
while b!=0:
    c=b%10
    b=b//10
    s=s*10+c
if flag == 1:
    s=-s
print(s)