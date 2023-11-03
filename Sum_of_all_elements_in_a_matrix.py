a,b=map(int,input().split())
mat=[]
for i in range(a):
    in_lt=list(map(int,input().split()))
    mat.append(in_lt)
s=0
for in_lt in mat:
    for ev_val in in_lt:
        s+=ev_val
print(s)