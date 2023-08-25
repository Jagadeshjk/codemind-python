a=int(input())
if a<199:
    b=a*1.20
elif a>=200 and a<400:
    b=a*1.40
elif a>=400 and a<600:
    b=a*1.60
elif a>=600 and a<800:
    b=a*1.80
else:
    b=a*2.00
c=b/a
print(f"Units Consumed: {a}")
print(f"Cost per Unit: {c:.2f}")
print(f"Bill: {b:.2f}")
if b>=400:
    s=b*0.15
    b=b+s
    print(f"Surcharge: {s:.2f}")
    print(f"Total Amount: {b:.2f}")
else:
    print("Surcharge: 0.00")
    print(f"Total Amount: {b:.2f}")