a=int(input())
n=0
while a!=1:
    if a%2==0:
        a//=2
    elif a%3==0:
        a//=3
    elif a%5==0:
        a//=5
    else:
        n+=1
        break
if n==0:
    print("Ugly Number")
else:
    print("Not Ugly Number")