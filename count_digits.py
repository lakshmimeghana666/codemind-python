n=int(input())
l=list(map(int,input().split()))
for i in l:
    x=str(i)
    a=len(x)
    if(i<0):
        a-=1
    print(a,end=" ")