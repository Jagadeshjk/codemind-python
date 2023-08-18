a=int(input())
if a<=10000:
    b=(a*80)/100
    c=(a*20)/100
elif a<=20000:
    b=(a*90)/100
    c=(a*25)/100
elif a>20000:
    b=(a*95)/100
    c=(a*30)/100
d=a+b+c
print("%.2f"%d)