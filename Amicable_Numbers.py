a1=int(input())
a2=int(input())
b1=0
b2=0
for i in range(1,a1):
    if a1%i==0:
        b2=b2+i
for j in range(1,a2):
    if a2%j==0:
        b1=b1+j
if b1==a1 and b2==a2:
    print("Amicable")
else:
    print("Not Amicable")