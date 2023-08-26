a=int(input())
b=0
c=0
while b*(b+1)<=a:
    if b*(b+1)==a:
        print("YES")
        c+=1
        break
    b+=1
if c==0:
    print("NO")