n,r=map(int,input().split())
l=[int(i) for i in input().split()]
x=[]
for i in range(r,n):
    x.append(l[i])
for j in range(r):
    x.append(l[j])
for i in x:
    print(i,end=" ")