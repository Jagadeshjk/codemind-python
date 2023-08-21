w,x,y,z=map(int,input().split())
i=x+y
j=x+z
k=y+z
if w==x or w==y or w==z or w==i or w==j or w==k:
    print("YES")
else:
    print("NO")