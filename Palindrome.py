a=int(input())
b=a
s=0
while b!=0:
    c=b%10
    b=b//10
    s=s*10+c
if s==a:
    print("Palindrome")
else:
    print("Not Palindrome")