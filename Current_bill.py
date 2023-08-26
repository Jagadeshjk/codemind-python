a=int(input())
if a<=199:
    b=1.20
elif a>=200 and a<400:
    b=1.50
elif a>=400 and a<600:
    b=1.80
else:
    b=2.00
bi=a*b
if bi>=400:
    ts=(bi*0.15)+bi
    print(f"{ts:.2f}")
else:
    ts=bi+100
    print(f"{ts:.2f}")